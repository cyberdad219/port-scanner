# Network Security Sandbox: Python TCP Port Scanner

A lightweight, multi-platform **TCP Port Scanner** built from scratch using Python's native `socket` library. This project serves as a security engineering sandbox designed to demonstrate network discovery mechanics, socket programming, and fundamental TCP/IP handshake sequences.

## Purpose & Security Mindset
This tool was engineered strictly for **educational purposes and authorized vulnerability assessment**. Understanding how network scanning works under the hood is critical for identifying unauthorized exposed services, auditing firewall configurations, and hardening infrastructure against external threats.

## Core Concepts Demonstrated
* **TCP Three-Way Handshake (`SYN` -> `SYN-ACK` -> `ACK`):** Implemented using Python's `socket.connect_ex()` layer to actively determine if remote doors are open, closed, or filtered.
* **Structured Exception Handling:** Wrapped execution flows inside robust `try/except` blocks to catch interruptions (like a user pressing `Ctrl+C`) or connection timeouts cleanly without crashing.
* **Low-Level Network I/O:** Configured timeout windows to prevent script hang, optimizing the performance of single-threaded port discovery.

## Requirements & Installation
No external third-party libraries (like `scapy` or `nmap-python`) are required. The script runs entirely on Python's built-in standard library.

1. Ensure you have **Python 3.x** installed.
2. Clone this repository to your local workspace.
3. Open a terminal in the project directory.

## How To Run
By default, the script is securely pre-configured to audit `localhost` (your own loopback IP) across common network ports (21, 22, 80, 443, etc).

Run the scanner using your system's terminal:

### On Windows:
```bash
python scanner.py
```

### On Mac / Linux:
```bash
python3 scanner.py
```

## Expected Output Examples

### Secure Host Configuration
If your target machine is securely hardened with no listening background processes exposed on those ports, the tool returns a clean status list:
```text
Port 21 is closed.
Port 22 is closed.
Port 80 is closed.
Port 443 is closed.
Port 8080 is closed.
```

### Clean Interruption Handling
Pressing `Ctrl+C` mid-scan cleanly interrupts the operational loop through custom exception mapping:
```text
Port 21 is closed.
[!] Exiting script gracefully...
```

---
*Disclaimer: This repository is intended to show foundational cybersecurity engineering logic. Unauthorized scanning of networks you do not own or have explicit written permission to test is strictly illegal.*
