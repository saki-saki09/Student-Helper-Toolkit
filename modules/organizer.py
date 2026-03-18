import os
import shutil
from utils.helpers import title, error, success, info


def run():
    title("📂 File Organizer")
    info("Tip: Press Enter to use demo files")
    folder = input("Enter folder path (or press Enter for demo): ").strip()

    if folder == "":
        folder = "assets/demo_files"
        info("Using demo folder: assets/demo_files")
    

    if not os.path.exists(folder):
        error("Folder not found!")
        return

    files = os.listdir(folder)

    if not files:
        error("No files to organize!")
        return

    moved = 0

    for filename in files:
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1][1:].lower()

            if not ext:
                ext = "others"

            target_folder = os.path.join(folder, ext)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(file_path, os.path.join(target_folder, filename))
            moved += 1

    success(f"{moved} files organized into folders!")