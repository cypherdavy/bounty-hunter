import requests

def brute_force_directories(target_url, wordlist):
    """Brute force directories and files on the target URL."""
    found_directories = []
    for word in wordlist:
        url = f"{target_url}/{word}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                found_directories.append(url)
                print(f"Found directory: {url}")
        except Exception as e:
            print(f"Error during directory brute force: {e}")
    return found_directories
