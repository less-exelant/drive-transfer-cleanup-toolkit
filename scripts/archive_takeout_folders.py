import os
import shutil

MY_DRIVE_PATH = "/Users/alexadraposes/Library/CloudStorage/GoogleDrive-aposes@exelant.io/My Drive"
ARCHIVE_FOLDER = "Takeout_ARCHIVE"

archive_path = os.path.join(MY_DRIVE_PATH, ARCHIVE_FOLDER)
os.makedirs(archive_path, exist_ok=True)

for item in os.listdir(MY_DRIVE_PATH):
    item_path = os.path.join(MY_DRIVE_PATH, item)
    if os.path.isdir(item_path) and item.lower().startswith("takeout"):
        if item == "Takeout":
            continue  # keep the primary one
        print(f"Archiving: {item}")
        shutil.move(item_path, os.path.join(archive_path, item))

print("Cleanup complete.")