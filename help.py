import argparse
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


parser = argparse.ArgumentParser(description='Bounty Hunter - Automated Bug Hunting Tool')


parser.add_argument('-u', '--url', type=str, help='Target URL for testing')
parser.add_argument('-r', '--recon', action='store_true', help='Run reconnaissance phase')
parser.add_argument('-b', '--brute-force', action='store_true', help='Run brute-force login attacks')
parser.add_argument('-s', '--sql-injection', action='store_true', help='Run SQL injection tests')
parser.add_argument('-x', '--xss', action='store_true', help='Run Cross-Site Scripting (XSS) tests')
parser.add_argument('-c', '--csrf', action='store_true', help='Run CSRF attack')
parser.add_argument('-rfi', '--lfi', action='store_true', help='Run RFI/LFI exploit attacks')
parser.add_argument('-e', '--rce-exploit', action='store_true', help='Run RCE exploit')
parser.add_argument('-m', '--mitm', action='store_true', help='Run MITM (Man-in-the-Middle) attack')
parser.add_argument('-g', '--generate-poc', action='store_true', help='Generate PoC for vulnerabilities')
parser.add_argument('-si', '--sqli-fuzzer', action='store_true', help='Run SQL injection fuzzer')
parser.add_argument('-ssl', '--ssl-test', action='store_true', help='Test SSL security')
parser.add_argument('-sub', '--subdomain', action='store_true', help='Run subdomain discovery')
parser.add_argument('-z', '--zap-scan', action='store_true', help='Run ZAP (OWASP) scan')
parser.add_argument('-h', '--help', action='help', help='Show this help message and exit')

args = parser.parse_args()


username_list = ["admin", "test", "root"]
password_list = ["admin123", "password123", "123456"]
payloads_sql_injection = ["' OR 1=1 --", "' OR 'a'='a", "'; DROP TABLE users; --"]
subdomain_wordlist = ["www", "dev", "staging", "api", "shop"]

def run_automated_tests(target_url):
    print(f"\nStarting automated tests on {target_url}...\n")
    

    if args.recon:
        print("\nStarting reconnaissance phase...\n")
        recon(target_url)
        subdomains = find_subdomains(target_url)
        
    if args.brute_force:
        print("\nRunning brute-force login...\n")
        brute_force_login(target_url, username_list, password_list)
    
    if args.sql_injection:
        print("\nRunning SQL injection tests...\n")
        fuzz_sql_injection(target_url, payloads_sql_injection)
    
    if args.xss:
        print("\nRunning XSS tests...\n")
        fuzz_http_headers(target_url)
    
    if args.csrf:
        print("\nRunning CSRF attack...\n")
        exploit_csrf(target_url)
    
    if args.lfi:
        print("\nRunning LFI/RFI exploit...\n")
        exploit_lfi_rfi(target_url)
    
    if args.rce_exploit:
        print("\nRunning RCE exploit...\n")
        exploit_rce(target_url)
    
    if args.mitm:
        print("\nRunning MITM attack...\n")
        mitm_attack(target_url)

    if args.generate_poc:
        print("\nGenerating PoC for vulnerabilities...\n")
        generate_poc(target_url)
    
    if args.sqli_fuzzer:
        print("\nRunning SQL injection fuzzer...\n")
        fuzz_sql_injection(target_url, payloads_sql_injection)
    
    if args.ssl_test:
        print("\nTesting SSL security...\n")
        test_ssl_security(target_url)
    
    if args.subdomain:
        print("\nRunning subdomain discovery...\n")
        find_subdomains(target_url)
    
    if args.zap_scan:
        print("\nRunning ZAP scan...\n")
        zap_scan(target_url)

    print("Generating Report...")
    generate_report(target_url)

    print("\nAutomation complete!")

if __name__ == "__main__":
    if args.url:
        target_url = args.url
        run_automated_tests(target_url)
    else:
        print("Please specify a target URL using -u or --url.")
