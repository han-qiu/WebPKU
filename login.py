#!/usr/bin/env python3
import requests
import sys
import getpass
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
username = "Your PKU ID"
password = getpass.getpass()
payload = {'username':username,'password':password,"iprange":iprange,'lang':'en'}
url = 'https://its.pku.edu.cn/cas/webLogin'
session = requests.session()
r = session.post(url, data = payload,allow_redirects=True)
r = session.get('https://its.pku.edu.cn/netportal/ipgwResult.jsp')
page = html.fromstring(r.content)
result = page.xpath('//tr/td//text()')
for i in result:
    if not '\r' in i:
        print(i)
