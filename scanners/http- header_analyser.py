import requests

def analyze_headers(url):
    response = requests.get(url)
    print("HTTP Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

if __name__ == "__main__":
    target_url = input("Enter target URL: ")
    analyze_headers(target_url)
