#!/usr/bin/env python3

import requests
import argparse

class scan:
	def __init__(self,website,headers):
		self.website = website
		self.headers = headers
	def _webScan(self):
		try:
			respon = requests.get(self.website,headers=self.headers)
		except Exception as e:
			print(e)
		return respon

class parameter:
	def _parameter(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('website',help="website for scan,eg:https://www.baidu.com",type=str)
		args = parser.parse_args()
		return args

class functionHandle:
	__dict = 'dict/dict.txt'
	def __init__(self,dir):
		self.dir = dir
	def _headers(self):
		headers={
		    'Accept': '*/*',
    		'Referer': self.dir,
    		'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
    		'Connection': 'Keep-Alive',
    		'Cache-Control': 'no-cache',
		}
		return headers
	def _dirToWebsite(self):
		website=[]
		with open(dict) as infile:
			while True:
				exdict = infile.readline().strip()
				if(len(exdict) == 0):break
				website.append(self.dir + exdict)
		return website

class judgement:
	notFoundPage = 'The beautiful girl,all over the world~'
	def __init__(self,website):
		self.website = website
	def _notFoundPage(self,responA,responB):
		if(responA.text == responB.text and responA.status_code != 404):
			notFoundPage = responA
	def scanPage(self,respon):
		if(respon.status_code != 404 and respon.text != notFoundPage.text):
			print('['+str(respon.status_code)+']'+ self.website)
