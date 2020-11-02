#!C:/Users/SAURABH/AppData/Local/Programs/Python/Python36-32/python.exe
# -*- coding: UTF-8 -*-

# enable debugging
print("Content-Type: text/html")
print()

import cgi, cgitb
import requests
import bs4
import pandas

form = cgi.FieldStorage()
comp_url = form.getvalue('base_url')
url = comp_url.split('/')
base_url = '/'+url[3]
print('https://www.magicbricks.com'+base_url)
try:
    res = requests.get('https://www.magicbricks.com'+base_url)
except requests.ConnectionError as r:
    r.status_code = "Connection Refused"
soup = bs4.BeautifulSoup(res.text, 'html.parser')
all_items = soup.find_all(attrs={"class": "act"})
count = 0
next_list = []
final_list = []
num = 0
for item in all_items:
    if count < 3:
        next_list.append(item.get('href'))
        count += 1
next_list.append('NULL')
while num <= count:
    if base_url == 'NULL':
        break
    else:
        res = requests.get('https://www.magicbricks.com'+base_url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        all_items = soup.find_all('div', {"class": "m-srp-card__container"})

        for new_item in all_items:
            items_price = new_item.find_all('div', {'class': 'm-srp-card__info'})
            items_other = new_item.find_all('div', {'class': 'm-srp-card__desc'})
            items = {}
            flag = 0
            for item in items_price:
                price = item.find('span').text
                if 'Cr' in price:
                    price = price.strip('Cr')
                    price = float(price)*100
                elif 'Call for Price' in price:
                    flag = 1
                else:
                    price = float(price.strip('Lac'))
                items["PRICE in Lacs"] = price

            area = ''
            for item in items_other:
                if flag == 0:
                    info = item.find('a').text.strip('\n').split('\n')
                    items["PLOT/FLAT"] = info[0]
                    print(items["PLOT/FLAT"])
                    items["LOCALITY"] = info[3].upper()
                    print(items["LOCALITY"])
                    area = item.find('div', {'class': 'm-srp-card__summary__info'}).text.replace(u'\xa0', ' ')
                    if 'sqm' in area:
                        area = area.strip('sqm')
                        area = float(area) * 3.2
                    elif 'guntha' in area:
                        area = area.strip('guntha')
                        area = float(area) * 1089
                    elif 'sqyrd' in area:
                        area = area.strip('sqyrd')
                        area = float(area) * 9
                    else:
                        area = area.strip('sqft')
                        area = float(area)
                    items["AREA in Sqft"] = area
                    items["OWNER"] = item.find('div', {'class': 'm-srp-card__advertiser__name'}).text.upper()
                    links = item.find(attrs={"class": "m-srp-card__title"})
                    items["LINK"] = links.get('href')
                    price *= 100000
                    items["RATE{Rs/Sqft}"] = price / area

            if flag == 0:
                final_list.append(items)
        num += 1
        base_url = next_list[num]


data_frame = pandas.DataFrame(final_list)
data_frame.to_csv("OutPut.csv")
print(data_frame)