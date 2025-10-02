# zipzap

⚡ A lightweight Python utility to quickly zip folders into `.zip` archives.  

## Features
- Zip entire folders (including subdirectories and files).  
- Preserves folder structure inside the archive.  
- Simple, minimal, and dependency-free (uses Python’s built-in `zipfile` module).  

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/zipzap.git
cd zipzap
```

No external dependencies needed—works with any standard Python 3 installation.

## Usage

### As a script
Run directly from the command line:
```bash
python zipzap.py my_folder output.zip
```
- `my_folder` → the folder you want to compress.  
- `output.zip` → the resulting archive file name.  

### As a module
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

## Roadmap
- [ ] Add unzip support  
- [ ] Add progress bar for large folders  
- [ ] Add support for excluding files by pattern  

## License
MIT License © 2025 Your Name
