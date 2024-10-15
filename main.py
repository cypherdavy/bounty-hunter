import argparse
from reconnaissance.recon import subdomain_enumeration, port_scan, tech_stack_detection
from scanners.scanner import zap_scan
from exploitation.exploit import exploit_xss
from pocs.poc_generator import generate_poc
from reporting.report_generator import generate_report

def main(target):
    # Reconnaissance
    print(f"Starting reconnaissance for {target}")
    subdomains = subdomain_enumeration(target)
    port_scan(target)
    tech_stack_detection(target)

    # Scanning
    print(f"Starting vulnerability scanning for {target}")
    scan_results = zap_scan(target)

    # Exploitation (example for XSS)
    print(f"Attempting exploitation for {
