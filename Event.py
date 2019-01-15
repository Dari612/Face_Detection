from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import urllib.request
import csv









url = "http://lib.ru/"
request = urllib.request.Request(url)

request.add_header('User-Agent',"cheese")


data = urllib.request.urlopen(request).read()
bsObj = BeautifulSoup(data, "html.parser")

Event = bsObj.findAll("dir")
 
for name in Event:
  print (name.get_text())
  
 

  

  
 