# Changelog

All notable changes to SecureScanPro are documented here.

---

## [2.0.0] - 2026-04-25

### Added
- Multi-target scanning via comma-separated input
- 4 scan modes: Quick, Aggressive, Top 1000 Ports, UDP
- Real-time timestamped log output in GUI
- JSON report export with auto-generated filenames
- Stop button to interrupt active scan queue
- Keyboard shortcuts: `Esc` (stop), `Ctrl+S` (export)
- `-Pn` flag applied across all modes for better reliability on filtered hosts
- Dark mode UI via CustomTkinter
- PyInstaller `.spec` for Windows standalone executable

### Changed
- Replaced `-n` (no DNS) with `-Pn` (skip host discovery) for improved scan success rate on remote targets

---

## [1.0.0] - Initial Release

- Basic single-target Nmap GUI wrapper
- CustomTkinter dark UI
- Simple log output display
