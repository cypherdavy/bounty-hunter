import os
from validlink import check_url_validity

output_file = 'output.txt'

def scan_subdomains(target_url):
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url
    
    is_valid_target = check_url_validity(target_url)
    if not is_valid_target:
        print(f"The URL {target_url} is not valid. Please enter a valid URL.")
        return

    user_choice = input("Do you have a subdomain list to scan? (yes or no): ").strip().lower()
    
    if user_choice in ['yes', 'y']:
        subdomain_list_name = input("Enter your subdomain list file name (with .txt extension): ").strip()
        if os.path.isfile(subdomain_list_name):
            os.system(f"subspy --url {target_url} --sub-list {subdomain_list_name} --save {output_file}")
        else:
            print("File not found. Please try again.")
            return
    else:
        os.system(f"subspy --url {target_url} --save {output_file}")

    if os.path.isfile(output_file):
        with open(output_file, 'r') as file:
            lines = file.readlines()
        
        os.remove(output_file) 
        
        formatted_subdomains = []
        for line in lines:
            if line.startswith("Sub: "):
                formatted_subdomain = line.replace("Sub: ", "").strip()
                if not formatted_subdomain.startswith("http"):
                    formatted_subdomain = "https://" + formatted_subdomain
                formatted_subdomains.append(formatted_subdomain)

        with open('output.txt', 'w') as valid_file:
            for subdomain in formatted_subdomains:
                valid_file.write(f"{subdomain}\n")

        print("Subdomain scanning completed. Valid subdomains saved to 'output.txt'.")
    else:
        print("Output file not found. Please check the scanning process.")
