# Vintage Diary App

A beautiful, animated digital diary that looks like an old book. Features smooth animations for opening/closing the book and flipping pages.

## 📸 Images Required

Download these images and place them in the same folder as `main.py`:

1. **Parchment Texture** (for pages): [Download](https://mistralaichatupprodswe.blob.core.windows.net/chat-images/assistant/24/11/12/241112c8-cd2a-478e-9716-865b8166d7fe/dbb345e3-5d74-42cc-a8b3-2e1457894a1f/f7f5b81e-4f7a-4fd1-86cc-ba7021eae8a9/e4356fb1-d7de-4418-9a3c-36aaf3a2c202.jpg) → Save as `parchment.jpg`

2. **Leather Texture** (for cover): [Download](https://mistralaichatupprodswe.blob.core.windows.net/chat-images/assistant/24/11/12/241112c8-cd2a-478e-9716-865b8166d7fe/dbb345e3-5d74-42cc-a8b3-2e1457894a1f/dfd31c1e-a511-4331-890f-f9c0bc2edf69/eaecca12-21b0-4114-8d44-e0adb6810e94.jpg) → Save as `leather.jpg`

3. **Ornate Border** (optional): [Download](https://mistralaichatupprodswe.blob.core.windows.net/chat-images/assistant/24/11/12/241112c8-cd2a-478e-9716-865b8166d7fe/dbb345e3-5d74-42cc-a8b3-2e1457894a1f/4f660835-f5e0-4f2f-bde5-4a3d756bf19d/b435ed9a-f72d-4d61-8f26-ba60f05bf9dd.jpg) → Save as `border.png`

4. **App Icon** (optional): [Download](https://mistralaichatupprodswe.blob.core.windows.net/chat-images/assistant/24/11/12/241112c8-cd2a-478e-9716-865b8166d7fe/dbb345e3-5d74-42cc-a8b3-2e1457894a1f/a057124f-4016-4276-9526-bbb064375cfb/21379fed-5d05-4d5b-9085-94ea45dc4453.jpg) → Save as `diary_icon.ico`

## 🚀 How to Run

### Run as Python Script
```bash
pip install PyQt5
python main.py
```

### Build as Executable

#### Windows:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name VintageDiary main.py
```
Executable will be in `dist/VintageDiary.exe`

#### Linux/Mac:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name VintageDiary main.py
```
Executable will be in `dist/VintageDiary`

## ✨ Features

- **Book Animations**: Smooth opening/closing animation
- **Page Flipping**: Animated page transitions (forward and backward)
- **Editable Cover**: Customize the diary title and your name
- **Auto-Save**: Data is saved to `diary_data.json` automatically
- **Unlimited Pages**: Add as many pages as you want
- **Vintage Design**: Beautiful book-like interface

## 🎭 Controls

- **Open/Close Diary**: Click the toggle button
- **Add Page**: Click "Add Page" button
- **Navigate**: Use Previous/Next buttons
- **Save**: Click Save button (also auto-saves)

## 📦 Files

- `main.py` - Main application
- `requirements.txt` - Dependencies
- `diary_data.json` - Saved data (auto-created)
- `parchment.jpg` - Page texture
- `leather.jpg` - Cover texture
- `border.png` - Ornate border (optional)
- `diary_icon.ico` - App icon (optional)