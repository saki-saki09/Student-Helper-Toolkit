import os
from utils.helpers import title, error, success, info


def run():
    title("📁 File Renamer")
    info("Tip: Press Enter to use demo files")
    folder = input("Enter folder path (or press Enter for demo): ").strip()

    if folder == "":
        folder = "assets/demo_files"
        info("Using demo folder: assets/demo_files")


    if not os.path.exists(folder):
        error("Folder not found!")
        return

    prefix = input("Enter prefix (e.g., file_): ").strip()

    files = os.listdir(folder)

    if not files:
        error("No files found in folder!")
        return

    count = 0

    for i, filename in enumerate(files, start=1):
        old_path = os.path.join(folder, filename)

        if os.path.isfile(old_path):
            extension = os.path.splitext(filename)[1]
            new_name = f"{prefix}{i}{extension}"
            new_path = os.path.join(folder, new_name)

            os.rename(old_path, new_path)
            count += 1

    success(f"{count} files renamed successfully!")