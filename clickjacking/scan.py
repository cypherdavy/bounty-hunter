import vulheader

def print_vulnerability(header, status):
    details = {
        "Strict-Transport-Security": "Missing Strict-Transport-Security header can leave the site vulnerable to man-in-the-middle (MITM) attacks, allowing attackers to downgrade HTTPS connections.",
        "Content-Security-Policy": "Missing Content-Security-Policy header can lead to cross-site scripting (XSS) vulnerabilities, allowing malicious scripts to run on the site.",
        "X-Frame-Options": "Missing X-Frame-Options header can expose the site to clickjacking attacks, where an attacker can trick a user into interacting with a hidden frame.",
        "X-Content-Type-Options": "Missing X-Content-Type-Options header can cause browsers to incorrectly interpret file types, potentially leading to security risks like executing malicious scripts.",
        "Referrer-Policy": "Missing Referrer-Policy header can expose sensitive information in the referrer header, such as session IDs or user information, to external sites.",
        "Permissions-Policy": "Missing Permissions-Policy header can expose the site to attacks that exploit web platform features, such as geolocation or camera access."
    }

    print(f"{header}: {'Missing' if status == 'missing' else 'Present'}")
    if status == "missing" and header in details:
        print(f"Details: {details[header]}")

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
