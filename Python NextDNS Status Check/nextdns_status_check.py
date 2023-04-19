import os;import re;import requests as r
try:c=r.get(re.search(r"\'(h.*io\/)\'",r.get("https://test.nextdns.io").text)[1]).json()
except:c={"status":"unavailable"}
print(f"NextDNS status: {c['status']}");os.system("pause")