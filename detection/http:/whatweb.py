import requests
import json
import time

class WhatWebScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.api_url = "https://api.whatweb.net"  # Replace with Wappalyzer or WhatWeb API URL
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }

    def fetch_website_data(self):
        """
        Fetch the web page content to perform technology stack detection.
        """
        try:
            print(f"Sending request to {self.target_url}...")
            response = requests.get(self.target_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error fetching website data: {e}")
            return None

    def analyze_stack(self, response):
        """
        Analyze the HTTP response and extract technology stack information.
        This will send the response to WhatWeb or Wappalyzer API for stack detection.
        """
        if response:
            print("Analyzing the website's technology stack...")
            try:
                # Send the response to WhatWeb/Wappalyzer API for analysis
                data = {
                    "url": self.target_url,
                    "headers": response.headers,
                    "html": response.text
                }

                # For Wappalyzer API, replace the API endpoint and authorization token
                # Wappalyzer API integration example:
                # api_response = requests.post(self.api_url, json=data, headers={'Authorization': 'Bearer <API_KEY>'})
                
                # Using WhatWeb's output locally (use an API if available)
                api_response = requests.post(self.api_url, json=data, headers=self.headers)
                api_response.raise_for_status()

                tech_stack = api_response.json()
                return tech_stack

            except Exception as e:
                print(f"Error during stack analysis: {e}")
                return None
        return None

    def format_results(self, tech_stack):
        """
        Format the technology stack results into a readable format.
        """
        if tech_stack:
            print("\nTechnology Stack Detected:\n")
            print(f"Target URL: {self.target_url}\n")
            print("Detected Technologies:")
            for tech in tech_stack.get('technologies', []):
                print(f" - {tech['name']} ({tech['category']})")

        else:
            print("No technologies detected or error in analysis.")

    def scan(self):
        """
        The main function to scan and detect the technology stack of a website.
        """
        response = self.fetch_website_data()
        if response:
            tech_stack = self.analyze_stack(response)
            self.format_results(tech_stack)

if __name__ == "__main__":
    # Example usage
    target_url = input("Enter target URL (e.g., https://example.com): ")
    scanner = WhatWebScanner(target_url)
    scanner.scan()
