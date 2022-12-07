# urlopen
import urllib.request
#beautifulsoup4
from bs4 import BeautifulSoup

url = 'https://tfp.put.ac.ir/fa-IR/tfp.put.ac/5171/page/%D8%A7%D8%B9%D8%B6%D8%A7%DB%8C-%D9%87%DB%8C%D8%A7%D8%AA-%D8%B9%D9%84%D9%85%DB%8C'

# connect to url
response = urllib.request.urlopen(url)



# parse by beautifulsoup
soup = BeautifulSoup(response, 'html.parser')

# save to list all tag tr by class name 'DataRow1'  
tr = soup.find_all('tr', class_='GridRow_Business') 

# find \n and replace with space -



#  save all tr text into file 

with open('files/asatid.txt', 'w',encoding="utf-8") as f:
    for i in tr:
        f.write('-----------------------------')
        f.write(i.text)
        
       




    




