#search malshare.com and download by using hash code
#get into hashes link and get all hashes then all of them are used for searching and downloading malware
#if there exists or it is not suitable for our malware criteria then it is skipped
#there are some important data taking from the search page

#Author: Mert NAR

import requests
import mechanize
import cookielib
from requests.auth import HTTPBasicAuth
from BeautifulSoup import  BeautifulSoup
try:
	from fake_useragent import UserAgent
except:
	print ("Missing libary. Try below command installing library. \n pip install fake-useragent")
#1- login -  https://virusshare.com/login.4n6
def login(url,name,password):
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_robots(False) # ignore robots
    br.open(url)
    br.select_form(name="login")
    br["username"] = name
    br["password"] = password
    res = br.submit()
    content = res.read()
    return br

#2- get all hashes in the ind link and put them in a list
def basamak(sayi):
    sayac=0
    while sayi:      
        sayac+=1       
        sayi=sayi/10
    return sayac
def malwhashes(ind):
    url_ind = "0"*(4-basamak(ind)) +str(ind)
    url = "https://virusshare.com/hashes/VirusShare_"+url_ind+".md5"
    r = requests.get(url)
    hashes =  [h for h in r.content.split('\n') if '#' not in h]
    i=0;
    for h in hashes:
        i+=1
        if '#' not in h:
            print h;
        if i>25:
            break
    return hashes
    #print hashes[0], hashes[1]
    #return r.content
def virusshare_hashsearch_content(br,hashv):
    url = "https://virusshare.com/"
    br.set_handle_robots(False) # ignore robots
    resp = br.open(url)
    br.select_form(nr=0)
    br["search"] = hashv
    res = br.submit()
    content = res.read()
    return content
def getFileType(content):
    soup = BeautifulSoup(content)
    tables = soup.findChildren('table')
    table = tables[0]
    rows = table.findChildren(['th', 'tr'])
    isfinded = 0
    last_tr = rows[-1] # date in last row - dependency: virusshare UI site design
    #print last_tr.text
    m = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2}', last_tr.text)
    date = m.group(0)
    
    for row in rows:
        tds = row.findChildren('td')
        for td in tds:
            val = td.string
            if(val == 'File Type'):
                isfinded = 1
                continue
            if(isfinded):
                return [date,val]

#3-check it is available to download

#4- download malware

#5- save malware information

#6- search hashed malware

#7- main: get hash list and search all of them one as download if it is good and save its info

#hash search - the hash value is put in list before?
loginurl = "https://virusshare.com/login.4n6"
name='merlingo'
password='AnTrIs135AUgjj'
hashv = '3cc5871bf954c043acddda4b9ebcaf893519b191266df8f3deba5f2b6f0d0fc0'
zipv = 'VirusShare_d650552bc9e86d433978043088f24644.zip'
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br = login(br,name,password)
content = virusshare_hashsearch_content(br,hashv)
malwhashes(0)
