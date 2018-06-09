#!/usr/bin/env python3

import requests
import time
import progressbar

def get_status_code(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}        
        u=requests.head(url,headers=headers) #Get request with head
        return u.status_code
    except StandardError:
        return None

def start_scan(url,f='./php.txt'):
    try:
        print(url)
        files=open(f)
        #############################ProgressBar mode
        #lens=len(files.readlines())
        #progbar=progressbar.ProgressBar()
        #progbar.start(lens)
        #############################ProgressBar mode
        for line in files:
            url_changed=url+line
            status_code=get_status_code(url_changed)
            if status_code=="200" or status_code=="403":
                print(url_changed+"  "+str(status_code))
            #progbar.update(line+1)
        #progbar.finish()
    except StandardError:
        return None

web=input("Input the WebPath:")
web=web.split()
if len(web)==2:
    start_scan(web[0],web[1])
elif len(web)==1:
    start_scan(web[0])
else:
    print("You have some error about your input")
