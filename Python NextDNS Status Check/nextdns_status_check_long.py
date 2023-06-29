import logging
import os
import re
from typing import Dict

import requests

logging.basicConfig(
    level=logging.INFO, 
    format="[%(asctime)s] [%(module)s] [%(levelname)-s] %(message)s", 
    datefmt='%Y-%m-%d %H:%M:%S'
)

try:
    req = requests.get("https://test.nextdns.io")
    pattern = r"\'(https.*\.test\.nextdns\.io\/)\'"
    res = re.search(pattern, req.text)
    req1 = requests.get(res[1])
    c: Dict[str, str] = req1.json()
    if not c["status"].startswith("ok"):
        logging.warning(f"NextDNS is {c['status']}")
except:
    logging.error("Service unvailable")
    c = {"status": "unavailable"}

logging.info(f"NextDNS status: {c['status']}")
os.system("pause")