
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning

import requests
import urllib3
import urllib.parse
import json
import argparse
import sys
import re

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-x", "--method", help="Method of request", default="POST")
parser.add_argument("-u", "--url", help="Url of Graphql", required=True)
parser.add_argument("-w", "--wordlist", help="Wordlist for brutforcing", default="wordlist.txt")
parser.add_argument("-p", "--proxy", help="Proxy for requests", default=None)
args = parser.parse_args()

METHOD = args.method
URL = args.url
WLIST = open(args.wordlist, "r").readlines()
PROXY = args.proxy
USERA = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0"}
objects_f = []

banner=f"""
\u001b[36m██████╗ ██████╗ ██╗   ██╗████████╗\u001b[31m ██████╗ \u001b[36m██╗     
\u001b[36m██╔══██╗██╔══██╗██║   ██║╚══██╔══╝\u001b[31m██╔═══██╗\u001b[36m██║     
\u001b[36m██████╔╝██████╔╝██║   ██║   ██║   \u001b[31m██║   ██║\u001b[36m██║     
\u001b[36m██╔══██╗██╔══██╗██║   ██║   ██║   \u001b[31m██║▄▄ ██║\u001b[36m██║     
\u001b[36m██████╔╝██║  ██║╚██████╔╝   ██║   \u001b[31m╚██████╔╝\u001b[36m███████╗
\u001b[36m╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   \u001b[31m ╚══▀▀═╝ \u001b[36m╚══════╝
                                                   
\u001b[36;1mWordlist size:\u001b[0m {len(WLIST)}\u001b[36;1m | Method: \u001b[0m {METHOD} \u001b[36;1m | Target: \u001b[0m {URL}
"""

if args.proxy != None:
	PROXY = {
	"http": args.proxy,
	"https": args.proxy
	}

def dym(text):
	r = '\\"(.*?)\\"'
	resp = json.loads(text)
	message = resp["errors"][0]["message"]
	x = re.findall(r, message)
	obj = x[2]
	verifyObjs(obj)

def verifyObjs(obj):
	if obj not in objects_f:
		objects_f.append(obj) 
		print(f"\u001b[32;1m[!] Object Found:\u001b[0m {obj}")

def verifyResponse(obj,status,text):
	if status == 200:
		verifyObjs(obj)
	if "is required but not provided" in text:
		verifyObjs(obj)
	if "Did you mean" in text:
		dym(text)

def checkGET(obj):
	obj = obj.replace("\n","")
	payload = "query{%s{__typename}}"%(obj)
	req = requests.get(f"{URL}?query={urllib.parse.quote(payload)}", proxies=PROXY, headers=USERA, verify=False)
	verifyResponse(obj,req.status_code,req.text)

def checkPOST(obj):
	obj = obj.replace("\n","")
	payload = """query{
					%s{
						__typename
						}
				}"""%(obj)
	req = requests.post(URL, json={'query':payload}, proxies=PROXY, headers=USERA, verify=False)
	verifyResponse(obj,req.status_code,req.text)

def construct(obj, nvl):
	scheme = obj + scheme
	print(scheme)

if __name__ == '__main__':

	print(banner)

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
