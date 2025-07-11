# file_organizer.py
# 🗂️ File Organizer

The **File Organizer** is a Python script that automatically organizes files in a folder based on their file type. It helps you keep your folders clean by sorting files into categories like images, videos, documents, music, archives, and scripts.

---

## 📁 How It Works

1. Set the path of the folder you want to organize.
2. The script looks at each file's extension.
3. It moves the file into a folder based on its type (e.g. `.jpg` goes to `images/`).

If a folder for the file type doesn’t exist, it will be created automatically.

---

## 🔧 Supported File Types

```python
{
  "images": [".jpg", ".jpeg", ".png", ".gif"],
  "videos": [".mp4", ".mov", ".avi"],
  "documents": [".pdf", ".docx", ".txt"],
  "music": [".mp3", ".wav"],
  "archives": [".zip", ".rar", ".tar"],
  "scripts": [".py", ".sh", ".bat"]
}
