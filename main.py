"""Vintage Diary App - PyQt5 with animations"""
import sys
import json
import os
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QTextEdit, QLabel, QPushButton, QFrame, QSizePolicy)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt, QRect, QTimer
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont

class DiaryPage(QWidget):
    def __init__(self, date, content="", page_num=1, parent=None):
        super().__init__(parent)
        self.date = date
        self.page_num = page_num
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)
        try:
            parchment = QPixmap("parchment.jpg")
            if not parchment.isNull():
                p = QPalette()
                p.setBrush(QPalette.Background, QBrush(parchment.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
                self.setPalette(p)
                self.setAutoFillBackground(True)
        except:
            self.setStyleSheet("background: #f5e7d3;")
        header = QHBoxLayout()
        self.date_label = QLabel(date)
        self.date_label.setStyleSheet("font-family: Times New Roman; font-size: 16px; color: #5a2d0c; font-weight: bold;")
        self.page_label = QLabel(f"Page {page_num}")
        self.page_label.setStyleSheet("font-family: Times New Roman; font-size: 14px; color: #5a2d0c; font-style: italic;")
        header.addWidget(self.date_label)
        header.addStretch()
        header.addWidget(self.page_label)
        layout.addLayout(header)
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(content)
        self.text_edit.setStyleSheet("background: transparent; border: none; font-family: Georgia; font-size: 14px; color: #333;")
        self.text_edit.setFrameShape(QFrame.NoFrame)
        layout.addWidget(self.text_edit)
        self.setStyleSheet("border: 1px solid #8b4513;")
    def resizeEvent(self, event):
        try:
            p = QPixmap("parchment.jpg")
            if not p.isNull():
                pal = QPalette()
                pal.setBrush(QPalette.Background, QBrush(p.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
                self.setPalette(pal)
        except: pass
        super().resizeEvent(event)
    def getContent(self): return self.text_edit.toPlainText()

class BookCover(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)
        try:
            leather = QPixmap("leather.jpg")
            if not leather.isNull():
                p = QPalette()
                p.setBrush(QPalette.Background, QBrush(leather.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
                self.setPalette(p)
                self.setAutoFillBackground(True)
        except:
            self.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #5a2d0c,stop:0.5 #8b4513,stop:1 #a0522d);")
        self.title_label = QLabel("My Diary")
        self.title_label.setStyleSheet("font-family: Times New Roman; font-size: 48px; color: #d4af37; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)
        subtitle = QLabel("A Personal Journal")
        subtitle.setStyleSheet("font-family: Georgia; font-size: 24px; color: #d4af37; font-style: italic; opacity: 0.8;")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)
        self.owner_input = QLabel("Enter your name...")
        self.owner_input.setStyleSheet("font-family: Georgia; font-size: 18px; color: #d4af37; background: rgba(0,0,0,0.3); border: 2px solid #d4af37; border-radius: 8px; padding: 12px;")
        self.owner_input.setAlignment(Qt.AlignCenter)
        self.owner_input.setFrameShape(QFrame.Panel)
        self.owner_input.setMinimumHeight(50)
        layout.addWidget(self.owner_input)
        self.setMinimumSize(800, 500)
    def resizeEvent(self, event):
        try:
            l = QPixmap("leather.jpg")
            if not l.isNull():
                p = QPalette()
                p.setBrush(QPalette.Background, QBrush(l.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
                self.setPalette(p)
        except: pass
        super().resizeEvent(event)

class DiaryBook(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pages = []
        self.current_page_index = 0
        self.is_open = False
        self.is_animating = False
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.cover_container = QWidget()
        self.cover_container.setMinimumSize(800, 500)
        self.cover_layout = QVBoxLayout(self.cover_container)
        self.cover_layout.setContentsMargins(0, 0, 0, 0)
        self.cover = BookCover()
        self.cover_layout.addWidget(self.cover)
        self.main_layout.addWidget(self.cover_container)
        self.pages_container = QWidget()
        self.pages_container.setVisible(False)
        self.pages_layout = QVBoxLayout(self.pages_container)
        self.pages_layout.setContentsMargins(0, 0, 0, 0)
        self.pages_layout.setSpacing(0)
        self.main_layout.addWidget(self.pages_container)
        self.addPage()
        self.setMinimumSize(820, 550)
    def addPage(self, date=None, content=""):
        if date is None: date = datetime.now().strftime("%B %d, %Y")
        page_num = len(self.pages) + 1
        page = DiaryPage(date, content, page_num)
        self.pages.append(page)
        self.pages_layout.addWidget(page)
        for i, p in enumerate(self.pages): p.setVisible(i == 0)
        return page
    def openBook(self):
        if self.is_open or self.is_animating: return
        self.is_animating = True
        self.is_open = True
        self.pages_container.setVisible(True)
        self.cover_animation = QPropertyAnimation(self.cover_container, b"geometry")
        self.cover_animation.setDuration(800)
        self.cover_animation.setEasingCurve(QEasingCurve.OutBack)
        self.cover_animation.setStartValue(self.cover_container.geometry())
        self.cover_animation.setEndValue(QRect(-self.width(), 0, self.width(), self.height()))
        self.cover_animation.finished.connect(self.onOpenFinished)
        self.cover_animation.start()
    def onOpenFinished(self):
        self.is_animating = False
        self.cover_container.setVisible(False)
        if self.pages: self.showPage(0)
    def closeBook(self):
        if not self.is_open or self.is_animating: return
        self.is_animating = True
        self.cover_container.setVisible(True)
        self.cover_container.setGeometry(QRect(-self.width(), 0, self.width(), self.height()))
        self.cover_animation = QPropertyAnimation(self.cover_container, b"geometry")
        self.cover_animation.setDuration(800)
        self.cover_animation.setEasingCurve(QEasingCurve.InBack)
        self.cover_animation.setStartValue(QRect(-self.width(), 0, self.width(), self.height()))
        self.cover_animation.setEndValue(QRect(0, 0, self.width(), self.height()))
        self.pages_container.setVisible(False)
        self.cover_animation.finished.connect(self.onCloseFinished)
        self.cover_animation.start()
    def onCloseFinished(self):
        self.is_animating = False
        self.is_open = False
        self.cover_container.setGeometry(QRect(0, 0, self.width(), self.height()))
    def showPage(self, index):
        if index < 0 or index >= len(self.pages): return
        if self.current_page_index < len(self.pages): self.pages[self.current_page_index].setVisible(False)
        self.pages[index].setVisible(True)
        self.current_page_index = index
    def nextPage(self):
        if self.current_page_index >= len(self.pages) - 1 or self.is_animating: return
        self.is_animating = True
        cur = self.pages[self.current_page_index]
        nxt = self.pages[self.current_page_index + 1]
        a1 = QPropertyAnimation(cur, b"geometry")
        a1.setDuration(400)
        a1.setEasingCurve(QEasingCurve.OutCubic)
        a1.setStartValue(cur.geometry())
        a1.setEndValue(QRect(self.width(), 0, self.width(), self.height()))
        nxt.setGeometry(QRect(self.width(), 0, self.width(), self.height()))
        nxt.setVisible(True)
        a2 = QPropertyAnimation(nxt, b"geometry")
        a2.setDuration(400)
        a2.setEasingCurve(QEasingCurve.OutCubic)
        a2.setStartValue(QRect(self.width(), 0, self.width(), self.height()))
        a2.setEndValue(QRect(0, 0, self.width(), self.height()))
        a1.start()
        a2.start()
        QTimer.singleShot(400, lambda: self.onNextFinished())
    def onNextFinished(self):
        self.is_animating = False
        self.current_page_index += 1
        if self.current_page_index > 0: self.pages[self.current_page_index - 1].setVisible(False)
    def prevPage(self):
        if self.current_page_index <= 0 or self.is_animating: return
        self.is_animating = True
        cur = self.pages[self.current_page_index]
        prev = self.pages[self.current_page_index - 1]
        a1 = QPropertyAnimation(cur, b"geometry")
        a1.setDuration(400)
        a1.setEasingCurve(QEasingCurve.OutCubic)
        a1.setStartValue(cur.geometry())
        a1.setEndValue(QRect(-self.width(), 0, self.width(), self.height()))
        prev.setGeometry(QRect(-self.width(), 0, self.width(), self.height()))
        prev.setVisible(True)
        a2 = QPropertyAnimation(prev, b"geometry")
        a2.setDuration(400)
        a2.setEasingCurve(QEasingCurve.OutCubic)
        a2.setStartValue(QRect(-self.width(), 0, self.width(), self.height()))
        a2.setEndValue(QRect(0, 0, self.width(), self.height()))
        a1.start()
        a2.start()
        QTimer.singleShot(400, lambda: self.onPrevFinished())
    def onPrevFinished(self):
        self.is_animating = False
        self.current_page_index -= 1
        if self.current_page_index < len(self.pages) - 1: self.pages[self.current_page_index + 1].setVisible(False)
    def saveData(self):
        data = {"owner_name": self.cover.owner_input.text(), "title": self.cover.title_label.text(), "pages": []}
        for page in self.pages: data["pages"].append({"date": page.date, "content": page.getContent()})
        with open("diary_data.json", "w") as f: json.dump(data, f, indent=2)
    def loadData(self):
        if not os.path.exists("diary_data.json"): return
        try:
            with open("diary_data.json", "r") as f: data = json.load(f)
            if "owner_name" in data: self.cover.owner_input.setText(data["owner_name"])
            if "title" in data: self.cover.title_label.setText(data["title"])
            for page in self.pages: self.pages_layout.removeWidget(page); page.deleteLater()
            self.pages = []
            if "pages" in data:
                for pd in data["pages"]: self.addPage(pd.get("date"), pd.get("content", ""))
        except Exception as e: print(f"Error: {e}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vintage Diary")
        self.setGeometry(100, 100, 850, 600)
        mw = QWidget()
        self.setCentralWidget(mw)
        layout = QVBoxLayout(mw)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        self.diary_book = DiaryBook()
        layout.addWidget(self.diary_book)
        cl = QHBoxLayout()
        cl.setSpacing(10)
        self.toggle_btn = QPushButton("📖 Open Diary")
        self.toggle_btn.setStyleSheet("QPushButton{background:#5a2d0c;color:#d4af37;border:1px solid #d4af37;border-radius:5px;padding:10px 20px;font-family:Georgia;font-size:14px;min-width:120px;}QPushButton:hover{background:#8b4513;}QPushButton:pressed{background:#3a1e0c;}")
        self.toggle_btn.clicked.connect(self.toggleBook)
        cl.addWidget(self.toggle_btn)
        ap = QPushButton("➕ Add Page")
        ap.setStyleSheet("QPushButton{background:#5a2d0c;color:#d4af37;border:1px solid #d4af37;border-radius:5px;padding:10px 20px;font-family:Georgia;font-size:14px;min-width:120px;}QPushButton:hover{background:#8b4513;}")
        ap.clicked.connect(self.addPage)
        cl.addWidget(ap)
        pb = QPushButton("← Previous")
        pb.setStyleSheet("QPushButton{background:#5a2d0c;color:#d4af37;border:1px solid #d4af37;border-radius:5px;padding:10px 20px;font-family:Georgia;font-size:14px;min-width:120px;}QPushButton:hover{background:#8b4513;}QPushButton:disabled{background:#4a2d0c;color:#6a4d2c;border-color:#6a4d2c;}")
        pb.clicked.connect(self.prevPage)
        cl.addWidget(pb)
        nb = QPushButton("Next →")
        nb.setStyleSheet("QPushButton{background:#5a2d0c;color:#d4af37;border:1px solid #d4af37;border-radius:5px;padding:10px 20px;font-family:Georgia;font-size:14px;min-width:120px;}QPushButton:hover{background:#8b4513;}QPushButton:disabled{background:#4a2d0c;color:#6a4d2c;border-color:#6a4d2c;}")
        nb.clicked.connect(self.nextPage)
        cl.addWidget(nb)
        sb = QPushButton("💾 Save")
        sb.setStyleSheet("QPushButton{background:#5a2d0c;color:#d4af37;border:1px solid #d4af37;border-radius:5px;padding:10px 20px;font-family:Georgia;font-size:14px;min-width:120px;}QPushButton:hover{background:#8b4513;}")
        sb.clicked.connect(self.saveData)
        cl.addWidget(sb)
        layout.addLayout(cl)
        self.diary_book.loadData()
        self.setStyleSheet("QMainWindow{background:#1a1a1a;}")
    def toggleBook(self):
        if self.diary_book.is_open: self.diary_book.closeBook(); self.toggle_btn.setText("📖 Open Diary")
        else: self.diary_book.openBook(); self.toggle_btn.setText("📕 Close Diary")
    def addPage(self):
        self.diary_book.addPage()
        if self.diary_book.is_open: self.diary_book.showPage(len(self.diary_book.pages) - 1)
    def nextPage(self):
        if self.diary_book.is_open: self.diary_book.nextPage()
    def prevPage(self):
        if self.diary_book.is_open: self.diary_book.prevPage()
    def saveData(self): self.diary_book.saveData()
    def closeEvent(self, event):
        self.diary_book.saveData()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Georgia", 12))
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
