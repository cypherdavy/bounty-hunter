import requests
import re

def extract_emails_from_url(target_url):
    """Extract emails from the web page at the target URL."""
    try:
        response = requests.get(target_url)
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text)
        print(f"Emails found on {target_url}: {emails}")
        return emails
    except Exception as e:
        print(f"Error extracting emails: {e}")
        return []
