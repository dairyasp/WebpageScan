#!/usr/bin/env python3

import requests
import argparse

#自定义参数
parser = argparse.ArgumentParser()
parser.add_argument('website',help="Website for scan",type=str)
args = parser.parse_args()

#字典
dict = 'dict/dict.txt'

#传入网址参数
website = args.website

#请求头设置
headers = {
    'Accept': '*/*',
    'Referer': website,
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
    'Connection': 'Keep-Alive',
    'Cache-Control': 'no-cache',
}

#字典与网址拼接后放入webdict
webdict=[]

#拼接网址与字典
with open(dict) as infile:
    while True:
        exdict = infile.readline().strip()
        if(len(exdict) == 0):break
        webdict.append(website+exdict)

for url in webdict:
    try:
        respon = requests.get(url,headers=headers)
    except Exception as e:
        print(url)
        print(e)
    if(respon.status_code==200):
        print('['+str(respon.status_code)+']'+ url)