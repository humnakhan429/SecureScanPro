# 🔒 SecureScanPro v2.0

<div align="center">

![SecureScanPro Banner](https://img.shields.io/badge/SecureScanPro-v2.0-blue?style=for-the-badge&logo=shield&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Nmap](https://img.shields.io/badge/Requires-Nmap-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A professional, GUI-based network scanner built on top of Nmap — designed for security professionals and ethical hackers.**

</div>

---

## 📸 Screenshot

> Dark-themed, clean GUI with multi-target scanning, real-time logging, and JSON report export.
<img width="1366" height="706" alt="image" src="https://github.com/user-attachments/assets/0204fbb2-4ef0-43a0-96c6-3e1e66786d33" />

---
<img width="1366" height="724" alt="image" src="https://github.com/user-attachments/assets/a0772f32-6c36-4ea1-a6f6-51274517c8c8" />

<img width="1363" height="732" alt="image" src="https://github.com/user-attachments/assets/204163a0-dc2d-4cdf-add4-0452c876b04f" />

## ✨ Features

- 🎯 **Multi-target scanning** — scan comma-separated IPs, hostnames, or CIDR ranges simultaneously
- 🔄 **4 Scan Modes**:
  - `Quick Scan` — Top 100 ports with service detection
  - `Aggressive (-A)` — Full OS detection, version detection, scripts, traceroute
  - `Top 1000 Ports` — Broad coverage with service version detection
  - `UDP Scan (-sU)` — Top 100 UDP ports
- 📋 **Real-time log output** — timestamped live scan results in the GUI
- 💾 **JSON Report Export** — auto-named reports with full scan data
- ⏹️ **Stop mid-scan** — interrupt multi-target queue any time
- ⌨️ **Keyboard shortcuts** — `Esc` to stop, `Ctrl+S` to export
- 🌙 **Dark mode UI** — built with CustomTkinter

---

## 🛠️ Requirements

### System Requirements
- **Nmap** must be installed and available in your system PATH
  - Windows: [Download Nmap](https://nmap.org/download.html) (installer adds to PATH automatically)
  - Linux: `sudo apt install nmap` or `sudo yum install nmap`
  - macOS: `brew install nmap`

### Python Requirements
- Python **3.8 or higher**

Install Python dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Installation & Usage

### Option 1: Run from Source

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/SecureScanPro.git
cd SecureScanPro

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python secure_scan_pro.py
```

> ⚠️ On Linux/macOS, some scan types (UDP, OS detection) require root privileges:
> ```bash
> sudo python secure_scan_pro.py
> ```

### Option 2: Windows Executable (Build it yourself)

```bash
pip install pyinstaller
pyinstaller SecureScanPro.spec
```

The executable will be in the `dist/` folder.

> **Note:** The `.spec` file bundles `nmap.exe` from `C:\Program Files (x86)\Nmap\nmap.exe`.  
> Update the path in `SecureScanPro.spec` if your Nmap installation is in a different location.

---

## 📁 Project Structure

```
SecureScanPro/
├── secure_scan_pro.py          # Main application source
├── SecureScanPro.spec          # PyInstaller build spec
├── requirements.txt            # Python dependencies
├── assets/
│   └── icon.ico                # Application icon
├── reports_sample/
│   └── secure_scan_pro_report_*.json   # Example report output
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📄 Report Format

Reports are exported as JSON files named `secure_scan_pro_report_YYYYMMDD_HHMMSS.json`.

Each entry contains:
```json
{
  "target": "scanme.nmap.org",
  "mode": "Aggressive (-A)",
  "output": "...(full nmap output)...",
  "time": "2026-04-25 16:49:32.718513"
}
```

---

## ⚙️ Building from Source (Windows)

1. Make sure Nmap is installed at `C:\Program Files (x86)\Nmap\`  
   (or update the path in `SecureScanPro.spec`)
2. Install PyInstaller: `pip install pyinstaller`
3. Build:
   ```bash
   pyinstaller SecureScanPro.spec
   ```
4. Find your executable at `dist/SecureScanPro.exe`

---

## ⚠️ Legal Disclaimer

> **This tool is intended for authorized security testing and educational purposes only.**
>
> - Only scan systems and networks you own or have explicit written permission to test.
> - Unauthorized port scanning may be illegal in your jurisdiction.
> - The author is not responsible for any misuse of this tool.
>
> **Always obtain proper authorization before scanning any network or system.**

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

See `.github/ISSUE_TEMPLATE/` for bug reports and feature requests.

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Nmap](https://nmap.org/) — The world's #1 network scanner
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — Modern dark-mode GUI framework for Python
