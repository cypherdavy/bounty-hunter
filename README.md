# Bounty Hunter - The Ultimate Bug Hunting Tool


### Introduction

Bounty Hunter is an advanced, automated tool designed for bug hunters and penetration testers. It integrates a variety of attacks, reconnaissance, and vulnerability testing functions that can be executed with just one click. By simply providing a target URL or domain, this tool performs various security tests like SQL Injection, Cross-Site Scripting (XSS), Remote Code Execution (RCE), Subdomain Discovery, and many more.

### Features

- **Reconnaissance:** Automatically gathers information about the target.
- **Vulnerability Scanning:** Tests for common web vulnerabilities like RCE, LFI/RFI, CSRF, XSS, and SQL Injection.
- **Exploitation:** Attempts to exploit identified vulnerabilities (use responsibly!).
- **Reporting:** Automatically generates reports summarizing the findings and proof of concept (PoC).
- **Subdomain Enumeration** and **Brute Force Attacks**.

### Requirements

To run the tool, ensure you have the following installed:

- **Python 3.8+**
- **Required Python Libraries** (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bounty-hunter.git
    cd bounty-hunter
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the tool with the target URL:
    ```bash
    python main.py
    ```

2. You will be prompted to enter a target URL:
    ```bash
    Enter the target URL: http://example.com
    ```

3. The tool will run through all tests and generate a report.

#### Command Line Options:

- **-h, --help**: Displays the help message.
- **-u, --url**: Specify the target URL to run the tests.
  
Example:
```bash
python main.py -u http://example.com
