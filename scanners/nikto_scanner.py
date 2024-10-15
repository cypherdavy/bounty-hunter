import requests
import argparse
import re
import socket
import ssl
import os
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

# Common directories to brute-force
COMMON_DIRECTORIES = [
    'admin', 'login', 'dashboard', 'config', 'test', 'backup', 'db', 'secret', 
    'uploads', 'images', 'scripts', 'private'
]

# User-Agent to simulate a browser request
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Common HTTP methods to test
HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH']

def check_http_methods(url):
    print(f"\n[INFO] Checking allowed HTTP methods for {url}")
    for method in HTTP_METHODS:
        try:
            response = requests.request(method, url, headers=HEADERS)
            print(f"{method}: {response.status_code}")
        except Exception as e:
            print(f"[ERROR] {method} request failed: {e}")

def directory_bruteforce(base_url):
    print(f"\n[INFO] Bruteforcing common directories on {base_url}")
    with ThreadPoolExecutor(max_workers=10) as executor:
        for directory in COMMON_DIRECTORIES:
            full_url = urljoin(base_url, directory)
            executor.submit(scan_directory, full_url)

def scan_directory(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            print(f"[FOUND] Directory found: {url}")
    except Exception as e:
        print(f"[ERROR] Error scanning {url}: {e}")

def ssl_scan(hostname):
    print(f"\n[INFO] Performing SSL scan for {hostname}")
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                print(f"[SSL INFO] Certificate Subject: {cert['subject']}")
                print(f"[SSL INFO] Valid from: {cert['notBefore']} to {cert['notAfter']}")
    except Exception as e:
        print(f"[ERROR] SSL scan failed: {e}")

def detect_software(url):
    print(f"\n[INFO] Detecting server software for {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        server_header = response.headers.get('Server', 'Unknown')
        powered_by = response.headers.get('X-Powered-By', 'Unknown')
        print(f"[INFO] Server: {server_header}")
        print(f"[INFO] Powered By: {powered_by}")

        # Basic detection of outdated or vulnerable servers
        if 'Apache' in server_header and '2.2' in server_header:
            print("[VULNERABILITY] Apache 2.2 is outdated and vulnerable!")
        if 'nginx' in server_header and '1.10' in server_header:
            print("[VULNERABILITY] Nginx 1.10 is outdated and vulnerable!")

    except Exception as e:
        print(f"[ERROR] Failed to detect software: {e}")

def find_emails_on_page(url):
    """ Extract emails from the given URL """
    print(f"\n[INFO] Extracting emails from {url}")
    try:
        response = requests.get(url, headers=HEADERS)
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
        if emails:
            print(f"[INFO] Emails found: {emails}")
        else:
            print(f"[INFO] No emails found on {url}")
    except Exception as e:
        
