import vulheader

def print_vulnerability(header, status):
    print(f"{header}: {'Missing' if status == 'missing' else 'Present'}")

def scan_inclusion(target_url):
    headers_to_check = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy"
    ]
    for header in headers_to_check:
        result = vulheader.check(target_url, header)
        print_vulnerability(header, result)
