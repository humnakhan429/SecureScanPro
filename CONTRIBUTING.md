# Contributing to SecureScanPro

Thank you for your interest in contributing! Here's how to get started.

---

## 🐛 Reporting Bugs

Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template when opening an issue.  
Please include your OS, Python version, Nmap version, and any error output.

## 💡 Suggesting Features

Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template.

---

## 🔧 Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/SecureScanPro.git
cd SecureScanPro
pip install -r requirements.txt
python secure_scan_pro.py
```

---

## 📋 Pull Request Guidelines

1. Fork the repo and create a branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Keep changes focused — one feature or fix per PR.
3. Test on at least one platform before submitting.
4. Update `CHANGELOG.md` under an `[Unreleased]` section.
5. Describe what your PR does and why in the PR description.

---

## ✅ Code Style

- Follow PEP 8
- Use descriptive variable/function names
- Add comments for non-obvious logic
- Keep GUI and scan logic in separate methods where possible

---

## ⚠️ Important

All contributions must be for **ethical, authorized security testing** use cases only.  
PRs that add features designed to facilitate unauthorized access will not be accepted.
