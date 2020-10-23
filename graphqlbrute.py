
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import urllib3
import json
import sys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
"""
Graphql Brutforce Scheme
"""
if len(sys.argv) < 3:
	print(f"Ex: python3 {sys.argv[0]} http://example/graphql wordlist.txt")
	sys.exit()

url = sys.argv[1]
wlist = open(sys.argv[2], "r")

def check(obj):
	obj = obj.replace("\n","")
	payload = """query{
					%s{
						__typename
						}
				}"""%(obj)
	req = requests.post(url, json={'query':payload})
	if req.status_code == 200:
		print(f"[!] Object Found: {obj}")
	if "is required but not provided" in req.text:
		print(f"[!] Possible Object Found: {obj}")

def construct(obj, nvl):
	scheme = obj + scheme
	print(scheme)

if __name__ == '__main__':

	try:
		with ThreadPoolExecutor() as t:
			t.map(check, wlist, timeout=3)

	except KeyboardInterrupt:
		sys.exit()
