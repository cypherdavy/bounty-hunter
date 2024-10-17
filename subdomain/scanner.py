import os

def scan_subdomains(target_url):
    user_choice = input("Do you have a subdomain list to scan? (yes or no) : ").strip().lower()
    
    if user_choice in ['yes', 'y']:
        subdomain_list_name = input("Enter your subdomain list file name (with .txt extension) : ").strip()
        if os.path.isfile(subdomain_list_name):
            os.system(f"subspy --url {target_url} --sub-list {subdomain_list_name} --save output.txt")
        else:
            print("File not found. Please try again.")
    else:
        os.system(f"subspy --url {target_url} --save output.txt")

    print("Subdomain scanning completed.")
