# ZipZap

ZipZap is a simple Python tool that lets you quickly compress entire folders into `.zip` archives.  
You can use it either from the **command line** or with a **file explorer dialog**.

---

## ✨ Features
- Select a **folder** (not files) and compress it into a `.zip`.
- Automatically names the zip file after your folder (you can change it).
- Works with **nested subfolders** and files.
- Cross-platform (Windows, macOS, Linux).

---

## 🚀 Installation
1. Make sure you have **Python 3.7+** installed:
   ```bash
   python --version
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/Dearingk1121/zipzap.git
   cd zipzap
   ```
3. (Optional) Make it executable on Linux/macOS:
   ```bash
   chmod +x zipzap.py
   ```

---

## 🖥️ Usage

### Method 1: File Explorer (no arguments)
Just run:
```bash
python zipzap.py
```

- You’ll be prompted to **choose a folder**.  
- Then choose where to save the resulting `.zip` file.  
- The zip file will contain the folder and all its subfolders/files.

---

### Method 2: Command Line (with arguments)
```bash
python zipzap.py <folder_path> <output_zip>
```

Example:
```bash
python zipzap.py ./MyProject ./MyProject.zip
```

This will create `MyProject.zip` containing everything inside the `MyProject` folder.

---

## 📂 Example
If you choose a folder called `MathToolbox/` with this structure:
```
MathToolbox/
 ├── MathToolbox.java
 └── README.md
```

ZipZap will create:
```
MathToolbox.zip
   ├── MathToolbox.java
   └── README.md
```

---

## 📝 Notes
- Always select a **folder** in the first dialog (not individual files).
- Works great for quickly packaging projects or assignments.
- The zipped folder keeps its structure when extracted.

---

## 📜 License
MIT License — feel free to use, modify, and share.
