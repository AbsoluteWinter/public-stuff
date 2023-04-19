import logging as l;import os;import re;import requests as r
l.basicConfig(level=l.INFO,format="[%(asctime)s] [%(module)s] [%(levelname)-s] %(message)s",datefmt='%Y-%m-%d %H:%M:%S')
try:
    req=r.get("https://test.nextdns.io");pattern=r"\'(https.*\.test\.nextdns\.io\/)\'";res=re.search(pattern, req.text);req1=r.get(res[1]);c=req1.json()
    if not c["status"].startswith("ok"):l.warning(f"NextDNS is {c['status']}")
except:
    l.error("Service unvailable");c={"status":"unavailable"}
l.info(f"NextDNS status: {c['status']}");os.system("pause")