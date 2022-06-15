import urllib.request
import re
from bs4 import BeautifulSoup


html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_228869.html').read()
soup = BeautifulSoup(html, "html.parser")

sum=0
tags = soup('span')
for tag in tags:
   
    y=str(tag)
    x= re.findall("[0-9]+",y)
    for i in x:
        i=int(i)
        sum=sum+i
print(sum)
