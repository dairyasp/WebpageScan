#!/usr/bin/env python3

import sys
import requests
import argparse
import threading
import queue
from termcolor import *

flag = 1

class Scan(threading.Thread):
	def __init__(self,website):
		threading.Thread.__init__(self)
		self.website = website
		self.headers = {
			'Accept': '*/*',
    		'Referer': website,
    		'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
    		'Connection': 'Keep-Alive',
    		'Cache-Control': 'no-cache',
		}
	def _scan(self):
		while flag:
			lock.acquire()
			try:
				if not workQueue.empty():
					dic = workQueue.get()
					url = self.website + dic
					lock.release()
					respon = requests.get(url,headers=self.headers,allow_redirects=False)
					if(respon.status_code != 404 and respon.text != self.page_404.text):
						if(respon.status_code == 200):
							print(colored('['+str(respon.status_code)+']','green')+" - "+ str(len(respon.text)) + "B - " +dic)
						elif(respon.status_code == 301 or respon.status_code == 302):
							print(colored('['+str(respon.status_code)+']','yellow')+" - "+ str(len(respon.text)) + "B - " + dic + " --> " + str(respon.headers['location']))
						else:
							print(colored('['+str(respon.status_code)+']','magenta')+" - "+ str(len(respon.text)) + "B - " + dic)
				else:
					lock.release()
			except Exception as e:
				print(e)
				lock.release
	def _404(self):
		self.page_404 = requests.get(self.website+"/nopagehere/nopage.php",headers=self.headers,allow_redirects=False)
		return
	def run(self):
		self._404()
		self._scan()

if __name__ == '__main__':
	#获取输入
	parser = argparse.ArgumentParser()
	parser.add_argument('-u','--website',help="Website for scan,eg:http://www.baidu.com",type=str)
	parser.add_argument('-t','--threads',nargs='?',default='10',help="Number of threads,default is 10",type=int)
	args = parser.parse_args()

	#一些东西的创建
	lock = threading.Lock()
	workQueue = queue.Queue(0) #创建一个先进先出队列
	threadList = range(args.threads) #进程数
	threads = [] #用来判断线程是否全部结束
	web_dict = []
	with open("dict/dict.txt") as infile:
		while True:
			dic = infile.readline().strip()
			if(len(dic)==0):break
			web_dict.append(dic)

	#队列填充(公共字典区)
	lock.acquire()
	for word in web_dict:
		workQueue.put(word)
	lock.release()

	for tList in threadList:
		thread = Scan(args.website)
		thread.start()
		threads.append(thread)

	while not workQueue.empty():
		sys.stdout.write('{0}/{1}\r'.format(len(web_dict) - workQueue.qsize(),len(web_dict)))
		sys.stdout.flush()
		pass

	flag = 0

	for t in threads:
		t.join()
	print("Fin")
