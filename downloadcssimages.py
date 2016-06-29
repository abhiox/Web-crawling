import os
import re
import sys
import requests
from bs4 import BeautifulSoup

def download_img_css(url):
    site = url.split('//')[-1].split('/')[0]
    os.makedirs(site)
    response = requests.get(url)
    if response.status_code != 200:
        return
    soup = BeautifulSoup(response.text)
    links = soup.find_all(rel = "stylesheet")
    hrefs = []
    for i in links:
        src = i.get('href')
        hrefs.append(src)

    imagesrc = set()
    for src in hrefs:
        cssrequest = requests.get(src)
        urls = re.findall('url\(([^)]+)\)',cssrequest.text)
        for i in urls:
            if i[:7] == 'http://' or i[:8] == 'https://':
                imagesrc.add(i)
            else:
                imagesrc.add(src.split('/')[0]+'//'+src.split('/')[2]+i)
    
    i=0
    for img in imagesrc:
        try:
            r = requests.get(img)
        except:
            continue
        i = i+1
        file = str(i)+"."+img.split('.')[-1]
        f = open(site+'/'+file,'wb')
        f.write(r.content)
        f.close()
    
if __name__=='__main__':
    if len(sys.argv) < 2:
        print("Enter the website to fetch css file images")
    else:
        download_img_css(sys.argv[1])
