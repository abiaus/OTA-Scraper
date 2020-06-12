
#Importo librerias
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import urllib


#------------------DICT--------------------------
dict = {'key':'value'}


#--------------------------------------------------------------
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
site = 'despegar.com.ar'

#query_ht = input("Agrega un hotel: ")
query_ht = 'panamericano buenos aires'
query_ht_plus = query_ht.replace(' ','+')
google_url ='https://www.google.com/search?q=site:'+site+'+'+query_ht_plus
print("-------BUSCANDO------")
#--------------------------------------------------------------

google_response = requests.get(google_url,headers=headers)
google_content = google_response.content
soup2 = BeautifulSoup(google_content, "html.parser")
page_url = soup2.find('a', attrs={'href': re.compile("^https://www.despegar")})

url = page_url['href']
webpage_response = requests.get(url,headers=headers)
#Guardo su contenido como html
webpage = webpage_response.content

#------------------SOPA--------------------------

soup = BeautifulSoup(webpage, "html.parser")

dict['page_url'] = page_url['href']
dict['name_ht'] = soup.find(attrs={'class':'hf-hotel-name -eva-3-bold'}).get_text()
dict['id_ht'] = page_url['href'][38:44]
dict['description_ht'] = soup.find(attrs={'class':'eva-3-p hf-description-text'}).get_text()
dict['address_ht'] = soup.find(attrs={'class':'hf-map-adress'}).get_text()
dict['rating_ht'] = soup.find(attrs={'class':'-eva-3-tc-white -eva-3-bold rating-text'}).get_text()
dict['main_img'] = soup.select_one('img')['src']
dict['amenities'] = soup.find(attrs={'class':'-eva-3-hide-small amenity-text'})
dict['destination'] = soup.find(attrs={'class':'hf-location-place'}).get_text()


'''print(name_ht)
print(id_ht)
#print(description_ht)
print(address_ht)
print(rating_ht)
print(main_img)
print(amenities)
print(destination)'''

print(dict)