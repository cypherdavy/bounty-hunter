import requests

def exploit_rce(target_url, payload):
    """Attempt Remote Code Execution (RCE) exploitation."""
    try:
        response = requests.get(target_url + payload)
        if "root" in response.text:  # Check if the payload worked
            print(f"RCE attack successful with payload: {payload}")
            return True
        else:
            print("RCE attack failed.")
            return False
    except Exception as e:
        print(f"Error during RCE exploit: {e}")
        return False
