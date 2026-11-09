# 🛡️ Protection & Extraction Toolkit

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@lapsusdev-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/lapsusdev)
[![GitHub](https://img.shields.io/badge/GitHub-Don84848-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Don84848)

<p align="center">
  A lightweight, high-performance CLI security suite for <b>Termux</b>, <b>Linux</b>, and <b>Windows</b>.
</p>

</div>

---

## ⚡ Overview

**Protection Toolkit** contains two powerful security & scraping tools:

1. **📥 Source Extractor (`extract.py`):** Download and extract the full front-end source code (HTML, CSS, JS) of any website using its URL.
2. **🔐 Code Protector (`protect.py`):** Obfuscate and protect your client-side code using advanced Deflate compression and Base64 encoding to prevent unauthorized code inspection via *"View Page Source"*.

---

## ✨ Features

- 🌐 **Web Scraper (Extract):** Instantly downloads the complete source code of any webpage directly into your terminal.
- 🔐 **Fast & Secure Obfuscation (Protect):** Encodes client-side code with zlib/deflate compression and Base64 wrapping.
- 📱 **Mobile & Termux Friendly:** Optimized layout and typography specifically tuned for narrow mobile terminal screens.
- ⚡ **Auto-Decoding in Browser:** The browser dynamically decompresses and renders the page in real-time with zero impact on user experience.
- 🎨 **Modern Terminal UI:** Built with Python's `rich` library for an elegant, interactive CLI experience with animated progress bars.

---

## 🚀 Installation

### On Termux / Linux / macOS:
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/Don84848/Protection.git
cd Protection
pip install -r requirements.txt
```

### On Windows:
```powershell
git clone https://github.com/Don84848/Protection.git
cd Protection
pip install -r requirements.txt
```

---

## 📖 Usage

### 1. Extract Website Source Code:
```bash
python extract.py
```
Enter the target URL when prompted. The extracted source will be saved as `[domain]_source.html`.

### 2. Protect / Obfuscate HTML Files:
```bash
python protect.py
```
Select the file ID to obfuscate. The protected output will be saved as `protected_[filename].html`.

---

## ⚠️ Disclaimer

This tool is designed for front-end code obfuscation and educational purposes. While it prevents casual inspection and direct "View Page Source" copying, experienced reverse engineers can inspect runtime DOM elements. Do not place private API keys or sensitive backend credentials in client-side code.

---

<div align="center">
  <b>Developed by <a href="https://t.me/lapsusdev">AD (@lapsusdev)</a></b><br>
  <sub>⭐ If you find this toolkit helpful, feel free to drop a star on the repo! ⭐</sub>
</div>

<!-- Verified by AD Security Lab -->
