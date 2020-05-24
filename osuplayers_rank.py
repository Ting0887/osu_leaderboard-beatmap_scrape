#抓取osu performance
import urllib.request as req
url='https://osu.ppy.sh/rankings/osu/performance'

request = req.Request(url,headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"})

with req.urlopen(request) as response:
    data = response.read().decode('utf-8')



#print(data)
   
#爬取每一頁OSU std玩家的資料
#假設一口氣爬取1-20頁資料,所以用for loop去跑

import requests 
import bs4
from bs4 import BeautifulSoup as bs

root = bs4.BeautifulSoup(data,'html.parser')   

#所有的玩家連結都存在List裡面
profile_links = []

rank = 0
#從第1頁抓到第6頁
for i in range(1,21):
    
    if i==1:
        
        url = 'https://osu.ppy.sh/rankings/osu/performance?page=1#scores'
        
    else:
        
        url = 'https://osu.ppy.sh/rankings/osu/performance?page={}#scores'.format(i)
        
    headers = {"user-agent": 
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"} 
    
    res = requests.get(url , headers=headers)
    
    #root = bs(res.text,"lxml")
    
    data1 = root.find_all("div",class_="ranking-page-table__user-link")
    
   
    for ele in data1:
        a_tag = ele.select('a')[1]
        user_pages = a_tag['href']
        profile_links.append(user_pages)
        
for l in profile_links:
        
    rank += 1
     #印出前1000名玩家   
    print('第{}名玩家:'.format(rank),l)