import requests
from bs4 import BeautifulSoup
import csv 
import time 

headers={'User-agent':'Mozilla/5.0'} #establish agent to access pages
url = 'https://www.pharmalive.com/page/{page}/' #allows us to sort through mulitple pages

outfile = open("scrub_{}.csv".format(time.strftime("%Y%m%d-%H.%M.%S")),'w',newline='')
writer = csv.writer(outfile)
writer.writerow(["Link","Title","Description"])

for page in range(1,2):
    req = requests.get(url.format(page=page),headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    
    for link in soup.select('.av-heading-wrapper h2 a'):
        link = link.get('href')
        
        req2=requests.get(link, headers=headers)
        soup2=BeautifulSoup(req2.text, 'lxml')
        title = soup2.find(attrs={"itemprop":"headline"}).text
        desc = soup2.find(attrs={"itemprop":"text"}).text
        writer.writerow([link,desc])
        
outfile.close()
        
