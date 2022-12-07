# urlopen
import urllib.request
#beautifulsoup4
from bs4 import BeautifulSoup

url = 'https://www.varzesh3.com/'

# connect to url
response = urllib.request.urlopen(url)



# parse by beautifulsoup
soup = BeautifulSoup(response, 'html.parser')

# save to list all tag tr by class name 'DataRow1'  
tr = soup.find_all('li', class_='video-type') 

# find \n and replace with space -



#  save all tr text into file 

with open('files/newssport.txt', 'w',encoding="utf-8") as f:
    for i in tr:
        f.write('-----------------------------')
        f.write(i.text)
        
       




    




