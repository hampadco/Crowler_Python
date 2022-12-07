# urlopen
import urllib.request
#beautifulsoup4
from bs4 import BeautifulSoup

url = 'http://irsc.ut.ac.ir/index.php?lang=ea'
url2 = 'http://irsc.ut.ac.ir/index.php?page=2'
url3 = 'http://irsc.ut.ac.ir/index.php?page=3'
# connect to url
response1 = urllib.request.urlopen(url)
response2 = urllib.request.urlopen(url2)
response3 = urllib.request.urlopen(url3)
# concat response
response = response1.read() + response2.read() + response3.read()

# parse by beautifulsoup
soup = BeautifulSoup(response, 'html.parser')

# save to list all tag tr by class name 'DataRow1'  
tr = soup.find_all('tr', class_='DataRow1') 
# save to list all tag tr by class name 'DataRow2'
tr2 = soup.find_all('tr', class_='DataRow2')
# save to list all tag tr by class name 'DataRow1' and 'DataRow2'
tr.extend(tr2)
# find \n and replace with space -



#  save all tr text into file 

with open('files/test.txt', 'w',encoding="utf-8") as f:
    for i in tr:
        f.write('-----------------------------')
        f.write(i.text)
        
       




    




