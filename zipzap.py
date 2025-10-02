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
        # Use Tkinter file dialog to select folder
        root = tk.Tk()
        root.withdraw()  # hide the root window
        folder_path = filedialog.askdirectory(title="Select a folder to zip")
        if not folder_path:
            print("No folder selected. Exiting.")
            sys.exit(1)

        # Ask where to save the zip
        output_path = filedialog.asksaveasfilename(
            title="Save zip file as...",
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

if __name__ == "__main__":
    main()
