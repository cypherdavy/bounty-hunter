from zapv2 import ZAPv2
import time

def zap_scan(target, api_key="your_api_key"):
    zap = ZAPv2(apikey=api_key)
    zap.urlopen(target)
    time.sleep(2)

    scan_id = zap.spider.scan(target)
    while int(zap.spider.status(scan_id)) < 100:
        print(f"Spider progress: {zap.spider.status(scan_id)}%")
        time.sleep(5)

    active_scan_id = zap.ascan.scan(target)
    while int(zap.ascan.status(active_scan_id)) < 100:
        print(f"Active scan progress: {zap.ascan.status(active_scan_id)}%")
        time.sleep(5)

    return zap.core.alerts()
