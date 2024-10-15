import sys

def print_help():
    """
    This function displays help instructions for using the Bug Hunter tool.
    """
    help_message = """
    ===========================
    Bounty Hunter - Help Menu
    ===========================

    A powerful bug bounty automation tool for vulnerability scanning, exploitation, and reporting.

    Usage:
      python main.py -u <URL> -t <target_type> [options]
      python main.py -h

    Options:
    -h, --help               Show this help message and exit.
    -u, --url <url>          Target URL for scanning (e.g., http://example.com).
    -t, --target <type>      Specify the target type (e.g., 'web', 'network').
    -p, --port <port>        Target port (default: 80).
    -o, --output <file>      Save the results to the specified output file.

    Example:
    python main.py -u https://example.com -t web -o result.txt

    Available Modules:
    - Recon: Perform reconnaissance (subdomain enumeration, tech stack detection, etc.)
    - Scan: Vulnerability scanning (using tools like OWASP ZAP, Nikto, etc.)
    - Exploit: Exploitation tools for XSS, SQLi, RCE, etc.
    - Report: Generate vulnerability reports in PDF or HTML format.

    For more detailed information, visit the GitHub repository or check the documentation.
    """
    print(help_message)

if __name__ == "__main__":
    if len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv:
        print_help()
    else:
        print("Invalid command. Use '-h' or '--help' for usage instructions.")
