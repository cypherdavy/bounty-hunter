import requests

def subdomain_enumeration(domain):
    subdomains = []
    try:
        url = f"https://sonar.omnisint.io/subdomains/{domain}"
        response = requests.get(url)
        if response.status_code == 200:
            subdomains = response.json()
            print(f"Found subdomains: {subdomains}")
        else:
            print("Error retrieving subdomains.")
    except Exception as e:
        print(f"Error occurred: {e}")
    return subdomains

def port_scan(domain):
    # Placeholder for port scanning logic
    print(f"Port scanning for {domain}")
    # Use tools like Nmap or integrate with python-nmap for actual scanning.

def tech_stack_detection(domain):
    print(f"Detecting technology stack for {domain}")
    # Example: Integrate with WhatWeb or Wappalyzer API for tech stack detection.

if __name__ == "__main__":
    domain = input("Enter the target domain: ")
    subdomains = subdomain_enumeration(domain)
    port_scan(domain)
    tech_stack_detection(domain)
