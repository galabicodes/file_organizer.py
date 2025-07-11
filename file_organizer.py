import os
import shutil

folder_path = os.path.expanduser("~/Desktop/organize_me")

file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "videos": [".mp4", ".mov", ".avi"],
    "documents": [".pdf", ".docx", ".txt"],
    "music": [".mp3", ".wav"],
    "archives": [".zip", ".rar", ".tar"],
    "scripts": [".py", ".sh", ".bat"]
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if not os.path.isfile(file_path):
        continue
    _, extension = os.path.splitext(filename)
    for folder, extensions in file_types.items():
        if extension.lower() in extensions:
            target_folder = os.path.join(folder_path, folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved {filename} to {folder}/")
            break
