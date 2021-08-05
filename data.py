from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

headers = ["name","distance" , "mass" , "radius"]
bright_stars_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(bright_stars_url)
print(page)

soup = bs(page.text,'html.parser')
star_table = soup.find('table')
temp_list = []
table_rows = star_table.find_all('tr')
for tr in table_rows:
  td = tr.find_all('td')
  row = [i.text.rstrip()for i in td]
  temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []
lum = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][3])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][6])
    star_names.append(temp_list[i][7])
    lum.append(temp_list[i][7]) 


df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),coloumns = ['star_names','distance','mass','radius','luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')
