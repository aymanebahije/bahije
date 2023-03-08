
import numpy
import requests
from bs4 import BeautifulSoup
import csv
from itertools  import zip_longest

name=[]
adress=[]
distance=[]
links=[]

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

target_url = "https://www.booking.com/searchresults.fr.html?ss=Marrakech%2C+Marrakech-Tensift-Haouz%2C+Maroc&ssne=Londres&ssne_untouched=Londres&label=fr-85Sbyi2evytni3mHZEi6UgS267492169156%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1009985%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Ye7BFAsTyVd6vvamF_no64o&sid=b85d5f37ea7a23a27f0ec5f4f0df18df&aid=376366&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-38833&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=1df83e1c1631004e&ac_meta=GhAxZGY4M2UxYzE"

resp = requests.get(target_url, headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')

name=soup.find_all("div",{"fcab3ed991 a23c043802"})
adress=soup.find_all("span",{"f4bd0794db b4273d69aa"})
distance=soup.find_all("span",{"cb5ebe3ffb"})

for i in range(len(name)):
   name.append(name[i].text)  
   adress.append(adress[i].text) 
   distance.append(distance[i].text) 
print(name,adress,distance)



file_list = [name,adress,distance]
exported =zip_longest(*file_list)

with open(r"C:\Users\HP\Documents\file csv\names.csv","w") as myfile:
        wr = csv.writer(myfile)
        wr.writerow(["name","distance","adress"])
        wr.writerows(exported)



