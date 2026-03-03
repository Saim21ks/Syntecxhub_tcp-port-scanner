# 🔍 Multithreaded TCP Port Scanner

A fast, concurrent TCP port scanner built in Python using socket programming and ThreadPoolExecutor.

## 🚀 Features

- TCP Connect Scan
- Custom Port Range
- Configurable Timeout
- Adjustable Thread Count
- Logging to file
- Exception Handling
- Modular Architecture
- Unit Tests

## 📦 Installation

```bash
git clone https://github.com/yourusername/tcp-port-scanner.git
cd tcp-port-scanner
```

## ▶ Usage

```bash
python3 main.py 192.168.1.1 -p 20-100
```

With custom timeout & threads:

```bash
python3 main.py scanme.nmap.org -p 1-1000 -t 0.5 -th 200
```

## 🛠 Example Output

```
[OPEN] 22
[CLOSED] 23
[TIMEOUT] 443
```

Logs saved in:

```
logs/scan.log
```

## 🧠 Technical Concepts Used

- TCP Three-Way Handshake
- Socket Programming
- Multithreading
- Exception Handling
- CLI Argument Parsing
- Logging Mechanisms

## ⚠ Legal Disclaimer

Only scan systems you own or have permission to test.
Unauthorized scanning is illegal.

---

## 👨‍💻 Author

Mohamed Saim
