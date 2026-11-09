# WebEncryptor

A command line tool to obfuscate client side HTML, CSS, and JavaScript code and extract source files from web pages.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@lapsusdev-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/lapsusdev)
[![GitHub](https://img.shields.io/badge/GitHub-Don84848-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Don84848)

---

## Overview

WebEncryptor includes two simple scripts:

1. **protect.py**: Obfuscates HTML, CSS, and JavaScript using compression and Base64 encoding. The protected output decompresses directly inside the browser using native browser APIs.
2. **extract.py**: Fetches and saves the full frontend source of any webpage into an HTML file.

---

## Features

- **Browser Friendly:** Encrypted files run directly in modern browsers without needing external libraries.
- **Source Extractor:** Download complete HTML markup from any URL with one command.
- **Cross-Platform:** Works on Android Termux, Linux, macOS, and Windows.
- **Terminal UI:** Clean interactive menus and status output using Python Rich.

---

## Installation

### Termux or Linux
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/Don84848/WebEncryptor.git
cd WebEncryptor
pip install -r requirements.txt
```

### Windows or macOS
```bash
git clone https://github.com/Don84848/WebEncryptor.git
cd WebEncryptor
pip install -r requirements.txt
```

---

## Usage

### 1. Obfuscate HTML Files
```bash
python protect.py
```
Select the file you want to protect. The output will be saved as `protected_[filename].html`.

### 2. Extract Webpage Source
```bash
python extract.py
```
Enter the target URL when prompted. The extracted source will be saved as `[domain]_source.html`.

---

Developed by [AD (@lapsusdev)](https://t.me/lapsusdev)
