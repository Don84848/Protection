# 🔐 WebEncryptor: Client-Side Obfuscation & Source Extraction Toolkit

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@lapsusdev-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/lapsusdev)
[![GitHub](https://img.shields.io/badge/GitHub-Don84848-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Don84848)

<p align="center">
  A professional, lightweight CLI suite for client-side HTML, CSS, & JavaScript code obfuscation and URL source code extraction.
</p>

</div>

---

## ⚡ Overview

**WebEncryptor** provides two essential developer & security utilities:

1. **🔐 Web Encryptor (`protect.py`):** Obfuscates and encrypts client-side frontend code (HTML, CSS, JS) using advanced compression and Base64 wrapping, preventing unauthorized code inspection via *"View Page Source"*.
2. **📥 Source Extractor (`extract.py`):** Downloads and extracts the full frontend source code of any web page directly into a clean HTML file.

---

## ✨ Features

- 🔐 **Zero-Dependency Browser Runtime:** Encrypted web pages decompress and render automatically inside modern browsers using native `DecompressionStream`.
- 🌐 **Instant URL Extractor:** Fetch complete HTML source code from any URL with a single command.
- 📱 **Cross-Platform:** Optimized for **Termux (Android)**, **Linux**, and **Windows**.
- 🎨 **Rich Terminal Interface:** High-contrast, interactive CLI with live progress bars powered by Python's `rich` library.

---

## 🚀 Quick Installation

### On Termux / Linux:
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/Don84848/WebEncryptor.git
cd WebEncryptor
pip install -r requirements.txt
```

### On Windows / macOS:
```bash
git clone https://github.com/Don84848/WebEncryptor.git
cd WebEncryptor
pip install -r requirements.txt
```

---

## 📖 Usage

### 1. Obfuscate / Encrypt HTML Files:
```bash
python protect.py
```
Select the file ID to encrypt. The protected output is saved as `protected_[filename].html`.

### 2. Extract Webpage Source Code:
```bash
python extract.py
```
Enter the target URL when prompted. The extracted source is saved as `[domain]_source.html`.

---

<div align="center">
  <b>Developed by <a href="https://t.me/lapsusdev">AD (@lapsusdev)</a></b><br>
  <sub>⭐ If you find WebEncryptor helpful, please drop a star on the repo! ⭐</sub>
</div>
<!-- Build tag: v1.0.4 -->
