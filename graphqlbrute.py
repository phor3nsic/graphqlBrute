
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import urllib3
import urllib.parse
import json
import argparse
import sys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

"""
Graphql Brutforce Scheme
"""
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-x", "--method", help="Method of request", default="POST")
parser.add_argument("-u", "--url", help="Url of Graphql", required=True)
parser.add_argument("-w", "--wordlist", help="Wordlist for brutforcing", default="wordlist.txt")
parser.add_argument("-p", "--proxy", help="Proxy for requests", default=None)
args = parser.parse_args()

METHOD = args.method
URL = args.url
WLIST = open(args.wordlist, "r")
PROXY = args.proxy

if args.proxy != None:
	PROXY = {
	"http": args.proxy,
	"https": args.proxy
	}

def verifyResponse(obj,status,text):
	if status == 200:
		print(f"[!] Object Found: {obj}")
	if "is required but not provided" in text:
		print(f"[!] Possible Object Found: {obj}")

def checkGET(obj):
	obj = obj.replace("\n","")
	payload = "query{%s{__typename}}"%(obj)
	req = requests.get(f"{URL}?query={urllib.parse.quote(payload)}", proxies=PROXY, verify=False)
	verifyResponse(obj,req.status_code,req.text)

def checkPOST(obj):
	obj = obj.replace("\n","")
	print(URL)
	payload = """query{
					%s{
						__typename
						}
				}"""%(obj)
	req = requests.post(URL, json={'query':payload}, proxies=PROXY, verify=False)
	verifyResponse(obj,req.status_code,req.text)

def construct(obj, nvl):
	scheme = obj + scheme
	print(scheme)

if __name__ == '__main__':
	if METHOD == "POST":
		try:
			with ThreadPoolExecutor() as t:
				t.map(checkPOST, WLIST, timeout=3)
		except KeyboardInterrupt:
			sys.exit()

	if METHOD == "GET":
		try:
			with ThreadPoolExecutor() as t:
				t.map(checkGET, WLIST, timeout=3)
		except KeyboardInterrupt:
			sys.exit()
	else:
		print("[?] Method not found\n- Methods accepted: GET or POST")
