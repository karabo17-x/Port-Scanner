# Port-Scanner
TCP port scanner written in Python.  It checks a target IP address or hostname  Scans ports 1–1024  Identifies which ports are open  Attempts to map open ports to common services (like HTTP, FTP, SSH)  Displays the scan start time and results in the terminal
# 🔐 Python Port Scanner


This tool scans a target IP address or hostname to identify **open ports** and their associated services.

---

## 📌 Features

- Scans ports **1–1024**
- Resolves **hostnames to IP addresses**
- Identifies **open TCP ports**
- Attempts to detect **common services**
- Displays scan **start time**
- Handles common network errors gracefully

---

## 🧠 Purpose

Port scanning is a fundamental technique in **cybersecurity reconnaissance**.  
This script helps identify exposed services that could potentially be exploited if not properly secured.

It is intended for:
- Learning how port scanners work
- Understanding network services
- Practicing ethical hacking fundamentals


---

## 🚀 How It Works

1. Accepts an **IP address or hostname** as a command-line argument  
2. Resolves the hostname to an IP address  
3. Iterates through ports **1–1024**
4. Attempts a TCP connection to each port
5. Reports open ports and associated services

---

## 🛠️ Requirements

- Python **3.x**
- No external libraries required (uses Python standard library)

---

## ▶️ Usage

```bash
python3 scanner.py <IP_or_Hostname>
