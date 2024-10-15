import subprocess

def whatweb_scan(target_url):
    """
    Function to perform website fingerprinting using WhatWeb.
    :param target_url: URL of the target website
    :return: Parsed output of WhatWeb scan
    """
    print(f"Starting WhatWeb scan on: {target_url}")
    
    try:
        # Running the WhatWeb command and capturing output
        result = subprocess.run(['whatweb', target_url, '--log-json=-'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Checking for any errors
        if result.returncode != 0:
            print(f"Error running WhatWeb: {result.stderr}")
            return None

        # Return WhatWeb JSON output for further analysis
        return result.stdout

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    target_url = input("Enter the target URL for WhatWeb scanning: ")

    # Perform the scan
    scan_result = whatweb_scan(target_url)

    if scan_result:
        print("\n[+] WhatWeb Scan Results:\n")
        print(scan_result)
    else:
        print("\n[-] No results returned from WhatWeb scan.")

if __name__ == "__main__":
    main()
