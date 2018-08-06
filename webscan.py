#!/usr/bin/env python3
import requests
import argparse
from termcolor import *

class Scan:
	def __init__(self,website):
		self.website = website
		self.dict = 'dict/dict.txt'
		self.headers = {
			'Accept': '*/*',
    		'Referer': website,
    		'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
    		'Connection': 'Keep-Alive',
    		'Cache-Control': 'no-cache',
		}
	def _scan(self,url):
		try:
			respon = requests.get(url,headers=self.headers)
			if(respon.status_code != 404 and respon.text != self.page_404.text):
				if(respon.status_code == 200):
					print(colored('['+str(respon.status_code)+']','green')+" "+url)
				else:
					print(colored('['+str(respon.status_code)+']','yellow')+" "+url)
		except Exception as e:
			print(e)

	def _combineAddr(self):
		web = []
		with open(self.dict) as infile:
			while True:
				dic = infile.readline().strip()
				if(len(dic)==0):break
				web.append(self.website + dic)
		return web
	def _404(self):
		self.page_404 = requests.get(self.website+"/nopagehere/nopage.php",headers=self.headers,allow_redirects=False)
		return

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('website',help="Website for scan,eg:http://www.baidu.com",type=str)
	args = parser.parse_args()
	s = Scan(args.website)
	s._404()
	web_dict = s._combineAddr()
	#print(web_dict)
	for url in web_dict:
		s._scan(url)