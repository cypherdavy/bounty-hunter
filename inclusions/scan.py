from inclusion import scan

def print_vulnerability(test_url):
    print(f"Inclusion vulnerability found : {test_url}")

def scan_inclusion(target_url):
    vulnerabilities = scan(target_url, callback=print_vulnerability)

    with open("inclusion_results.txt", "w") as f:
        if vulnerabilities:
            for vulnerability in vulnerabilities:
                f.write(f"Inclusion vulnerability found : {vulnerability}\n")
        else:
            f.write("No vulnerabilities found.\n")
            print("No vulnerabilities found.")
