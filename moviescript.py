import requests
from bs4 import BeautifulSoup
from pythonds.basic import Queue
import csv
import sys


with open('new.csv','w') as csvfile:						#name of the file is set as new.csv
    fieldnames = ['rating','movie','director']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()

def getsoup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    return soup

def getlinks(url):
    soup = getsoup(url)
    hrefs = soup.find_all("div",class_="rec_item")
    src = []
    for i in hrefs:
        urls = i.a['href']
        src.append('http://www.imdb.com' + urls.split('?')[0])
    print("returning links")
    print(src)
    return src

num = 0
def savemovie(url):
    global num
    soup = getsoup(url)
    ratwrap = soup.find(itemprop="ratingValue").string
    rating = float(ratwrap)
    
    if rating>=6.5 and rating<=8.5:										#movies of ratings between 6.5 and 8.5 are searched
        dirwrap = soup.find(itemprop="director")
        director = dirwrap.span.string
        namelist = soup.title.string.split('-')
        name = namelist[0]
        if(len(namelist)>2):
            name = namelist[0]+'-'+namelist[1]
        with open('new.csv','a') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writerow({'movie':name,'director':director,'rating':rating})
        num = num-1
        print("value of num=",num)
        print("done for "+name)

visitedset = set()
plength = 0
def checklength():
    global plength
    global visitedset
    if len(visitedset)>plength:
        plength +=1
        return 1
    elif len(visitedset)==plength:
        return 0

srcq = Queue()
def getnames(url,freq):
    global num
    global srcq
    global visitedset
    visitedset.add(url)
    srcq.enqueue(url)  
    
    num = freq
    num = int(num)
    while num != 0:
        currentsrc = srcq.dequeue()
        print("currentsrc="+currentsrc)
        for branch in getlinks(currentsrc):
            visitedset.add(branch)
            if checklength() ==0:
                continue  
            srcq.enqueue(branch)
        print(srcq)
        savemovie(currentsrc)

if __name__=='__main__':
    if len(sys.argv)<2:
        print("enter the url and the number of entries")
    else:
        print("filename: new.csv directory: pwd")
        getnames(sys.argv[1],sys.argv[2])

