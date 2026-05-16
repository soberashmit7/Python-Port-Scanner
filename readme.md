# Python Port Scanner

A GUI-based multithreaded TCP port scanner built using Python and Tkinter.

This project scans open ports on a target IP address or website, displays live scan progress, and exports scan results to a text file.

---

## Features

- GUI-based interface using Tkinter
- Multithreaded port scanning
- Custom start and end port selection
- Live scanning updates
- Stop Scan functionality
- Service detection
- DNS resolution
- Scrollable output window
- Dark theme cybersecurity-style UI
- Export scan results to text file
- Error handling for invalid targets and ports

---

## Technologies Used

- Python
- Tkinter
- Socket Programming
- Threading

---

## How It Works

1. User enters:
   - Target IP or Website
   - Start Port
   - End Port

2. The scanner:
   - Resolves domain to IP
   - Scans ports using TCP sockets
   - Detects open ports and services
   - Displays live scan progress

3. Results are:
   - Displayed in GUI
   - Saved to `scan_results.txt`

---

## Screenshots

Add screenshots here after uploading images.

Example:

```markdown
![Scanner Screenshot](screenshot.png)
```

---

## How To Run

### Install Python

Download Python from:
https://www.python.org/downloads/

---

### Run the Program

```bash
python scanner.py
```

---

## Example

Target:
```text
scanme.nmap.org
```

Port Range:
```text
1 - 100
```

---

## Educational Purpose

This project was created for educational and cybersecurity learning purposes only.

Please scan only systems you own or have permission to test.

---

## Author

Ashmit Chaudhary
