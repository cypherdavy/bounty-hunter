import shodan

def shodan_scan(api_key, target_ip):
    api = shodan.Shodan(api_key)
    try:
        results = api.host(target_ip)
        print(f"Results for {target_ip}:")
        print(f"IP: {results['ip_str']}")
        print(f"Organization: {results.get('org', 'n/a')}")
        print(f"Operating System: {results.get('os', 'n/a')}")
        for item in results['data']:
            print(f"Port: {item['port']}")
            print(f"Banner: {item['data']}")
    except shodan.APIError as e:
        print(f"Shodan API error: {e}")
