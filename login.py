#!/usr/bin/env python
import requests
import sys
import getpass
from termcolor import colored
from lxml import html
def usage():
	print("python fake.py 'yes'|'no'")
	print("yes for global ip, no for local ip")
if len(sys.argv)!=2:
	usage()
	sys.exit(1)
else:
	if sys.argv[1] == 'yes':
		iprange = 'yes'
	else:
		iprange = 'no'
username = 'your PKU ID'
password = getpass.getpass()
payload = {'username':username,'password':password,"iprange":iprange,'lang':'en'}
url = 'https://its.pku.edu.cn/cas/webLogin'
session = requests.session()
r = session.post(url, data = payload)
page = html.fromstring(r.content)
node = page.get_element_by_id('input_tip')
if node.text:
	print(node.text)
for i in node:
	if i.text == None:
		text = i[0].text
	else:
		text = i.text
	if "地址" in text:
		text = colored(text,'red')
	print(text)
