# 🔍 NetScan — Python Network Port Scanning Tool

NetScan is an educational cybersecurity project written in Python that performs network port scanning to identify open services and potential security risks.

The tool helps students and security researchers understand how attackers discover network services and how defenders analyze exposed ports.

⚠ This tool is intended for authorized security testing and educational use only.

---

## 📁 Project Structure

```
NetScan/
│
├── scanner.py
├── requirements.txt
└── README.md
```

---

## 🚀 Core Features

### Port Scanning
- TCP port scanning
- Custom port range support
- Fast connection testing
- Open port detection

### Target Analysis
- IP address validation
- Host availability check
- Service reachability testing
- Connection timeout handling

### Scan Management
- Sequential scanning engine
- Real-time scan output
- Error handling
- Interrupt support

---

## 🧩 Technologies Used

- Python 3.x
- socket library
- threading (if enabled)
- sys
- OS networking stack

---


## ▶️ Usage

Basic usage:

```bash
python scanner.py
```

With arguments:

```bash
python scanner.py --target 192.168.1.10 --ports 1-1000
```

Example:

```bash
python scanner.py --target scanme.nmap.org --ports 20-443
```

---

## 🔄 Scanning Workflow

```
Scanner → Target → Port Check → Result
```

1. The scanner selects target host.
2. Attempts connection to each port.
3. Detects open or closed status.
4. Displays scan results.
5. Saves findings (optional).

---

## 📚 Security Concepts Covered

- Port scanning techniques
- Network reconnaissance
- Service enumeration
- Attack surface analysis
- Network exposure assessment
- Defensive security auditing

---

## ⚠️ Legal and Ethical Notice

This tool must only be used on systems and networks where explicit authorization has been granted.

Unauthorized scanning may violate laws and policies.

The author is not responsible for misuse.

---

## 🎓 Educational Purpose

This project helps learners:

- Understand network discovery methods
- Practice ethical hacking techniques
- Analyze exposed services
- Improve defensive awareness
- Develop penetration testing skills

---

## 📈 Future Enhancements

- Multithreaded scanning
- Service version detection
- Banner grabbing
- UDP scanning
- Output export (CSV/JSON)
- Scan history tracking
- GUI interface

---

## 👨‍💻 Author

Specialization: Cybersecurity Engineering  


---

## 📄 License

MIT License

For educational and research purposes only.
