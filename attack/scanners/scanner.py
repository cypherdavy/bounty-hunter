import time
from zapv2 import ZAPv2

target = "http://example.com"
zap = ZAPv2(apikey='your-zap-api-key')

def zap_scan(target):
    print(f"Starting scan for {target}")
    zap.urlopen(target)
    time.sleep(2)

    scan_id = zap.spider.scan(target)
    while (int(zap.spider.status(scan_id)) < 100):
        print(f"Spider progress: {zap.spider.status(scan_id)}%")
        time.sleep(5)

    print("Spider complete. Starting active scan.")
    active_scan_id = zap.ascan.scan(target)
    while (int(zap.ascan.status(active_scan_id)) < 100):
        print(f"Active scan progress: {zap.ascan.status(active_scan_id)}%")
        time.sleep(5)

    print("Active scan complete.")
    return zap.core.alerts()

if __name__ == "__main__":
    results = zap_scan(target)
    print(f"Scan results: {results}")
