# Bounty Hunter Tool

**Bounty Hunter** is an advanced bug-hunting tool designed to automate the entire bug bounty process, including reconnaissance, scanning, exploitation, PoC generation, and reporting. It integrates various scanning tools and exploits common vulnerabilities like XSS, SQL Injection, RCE, and more.

## Features
- **Reconnaissance**: Subdomain enumeration, port scanning, tech stack detection.
- **Vulnerability Scanning**: Automatic scan for common vulnerabilities like XSS, SQL Injection, etc.
- **Exploitation**: Automated exploitation of discovered vulnerabilities (e.g., XSS, SQLi, RCE).
- **PoC Generation**: Automatically generate Proof of Concepts for vulnerabilities.
- **Reporting**: Create detailed PDF or HTML reports with findings and exploitation steps.

## Requirements
- Python 3.6+
- Install dependencies via `pip install -r requirements.txt`.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/cypherdavy/bounty-hunter
   cd bounty-hunter
