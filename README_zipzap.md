# zipzap

⚡ A lightweight Python utility to quickly zip folders into `.zip` archives.  

## Features
- Zip entire folders (including subdirectories and files).  
- Preserves folder structure inside the archive.  
- Simple, minimal, and dependency-free (uses Python’s built-in `zipfile` + `tkinter`).  
- Supports **interactive mode** with a file explorer dialog (no need to type paths).  

## Installation
Clone the repository:
```bash
git clone https://github.com/DearingK1121/zipzap
cd zipzap
```

No external dependencies needed—works with any standard Python 3 installation.

## Usage

### 1. Command-line mode
Run directly from the terminal:
```bash
python zipzap.py my_folder output.zip
```
- `my_folder` → the folder you want to compress.  
- `output.zip` → the resulting archive file name.  

### 2. Interactive mode
If you run without arguments:
```bash
python zipzap.py
```
- A **file explorer window** will open where you can choose the folder to zip.  
- Then another dialog will let you pick where to save the `.zip` file.  

### 3. As a module
You can also import `zipzap` in your own Python projects:
```python
from zipzap import zip_folder

zip_folder("my_folder", "my_folder.zip")
```

## Example
```bash
python zipzap.py test_folder test_folder.zip
```
Output:
```
Zipped test_folder -> test_folder.zip
```

Or, run without arguments and select the folder + save location via dialog.

## Roadmap
- [ ] Add unzip support  
- [ ] Add support for selecting multiple folders in interactive mode  
- [ ] Add progress bar for large folders  
- [ ] Add support for excluding files by pattern  

## License
MIT License © 2025 Your Name
