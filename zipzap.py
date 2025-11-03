# it works on mac now! your welcome :)
#!/usr/bin/env python3
import os
import sys
import zipfile
import tkinter as tk
from tkinter import filedialog

def zip_folder(folder_path, output_path):
    """
    Compresses a folder (including all subfolders and files) into a .zip archive.
    """
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print(f"Zipped {folder_path} -> {output_path}")

def main():
    if len(sys.argv) == 3:
        folder_path = sys.argv[1]
        output_path = sys.argv[2]
    else:
        # Set up hidden Tkinter root
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)  # make sure dialogs appear on top

        # Ask for a folder, not a file
        folder_path = filedialog.askdirectory(
            title="Select a folder to zip",
            mustexist=True
        )
        if not folder_path:
            print("No folder selected. Exiting.")
            sys.exit(1)

        # Default zip filename = folder name
        default_name = os.path.basename(folder_path.rstrip(os.sep)) + ".zip"

        output_path = filedialog.asksaveasfilename(
            title="Save zip file as...",
            initialfile=default_name,
            defaultextension=".zip",
            filetypes=[("Zip files", "*.zip")]
        )
        if not output_path:
            print("No output file chosen. Exiting.")
            sys.exit(1)

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid folder")
        sys.exit(1)

    zip_folder(folder_path, output_path)
    print("You have finised. Goodbye!")

if __name__ == "__main__":
    main()
# zipzap.py - A simple script to zip a folder into a .zip file