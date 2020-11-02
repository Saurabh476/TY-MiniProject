#!C:/Users/SAURABH/AppData/Local/Programs/Python/Python36-32/python.exe
# -*- coding: UTF-8 -*-

# enable debugging
print("Content-Type: text/html")
print()

import cgi, cgitb
import requests
import bs4
import pandas as pd
import webbrowser
from matplotlib import pyplot as plt

# form = cgi.FieldStorage()
# comp_url = form.getvalue('base_url')
# url = comp_url.split('/')
# base_url = '/'+url[3]
# print('https://www.magicbricks.com'+base_url)
# try:
#     res = requests.get('https://www.magicbricks.com'+base_url)
# except requests.ConnectionError as r:
#     r.status_code = "Connection Refused"
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# all_items = soup.find_all(attrs={"class": "act"})
# count = 0
# next_list = []
# final_list = []
# num = 0
# for item in all_items:
#     if count < 3:
#         next_list.append(item.get('href'))
#         count += 1
# next_list.append('NULL')
# while num <= count:
#     if base_url == 'NULL':
#         break
#     else:
#         res = requests.get('https://www.magicbricks.com'+base_url)
#         soup = bs4.BeautifulSoup(res.text, 'html.parser')
#         all_items = soup.find_all('div', {"class": "m-srp-card__container"})
#
#         for new_item in all_items:
#             items_price = new_item.find_all('div', {'class': 'm-srp-card__info'})
#             items_other = new_item.find_all('div', {'class': 'm-srp-card__desc'})
#             items = {}
#             flag = 0
#             for item in items_price:
#                 price = item.find('span').text
#                 if 'Cr' in price:
#                     price = price.strip('Cr')
#                     price = float(price)*100
#                 elif 'Call for Price' in price:
#                     flag = 1
#                 else:
#                     price = float(price.strip('Lac'))
#                 items["PRICE in Lacs"] = price
#
#             area = ''
#             for item in items_other:
#                 if flag == 0:
#                     info = item.find('a').text.strip('\n').split('\n')
#                     items["PLOT/FLAT"] = info[0]
#                     print(items["PLOT/FLAT"])
#                     items["LOCALITY"] = info[3].upper()
#                     print(items["LOCALITY"])
#                     area = item.find('div', {'class': 'm-srp-card__summary__info'}).text.replace(u'\xa0', ' ')
#                     if 'sqm' in area:
#                         area = area.strip('sqm')
#                         area = float(area) * 3.2
#                     elif 'guntha' in area:
#                         area = area.strip('guntha')
#                         area = float(area) * 1089
#                     elif 'sqyrd' in area:
#                         area = area.strip('sqyrd')
#                         area = float(area) * 9
#                     else:
#                         area = area.strip('sqft')
#                         area = float(area)
#                     items["AREA in Sqft"] = area
#                     items["OWNER"] = item.find('div', {'class': 'm-srp-card__advertiser__name'}).text.upper()
#                     links = item.find(attrs={"class": "m-srp-card__title"})
#                     items["LINK"] = links.get('href')
#                     price *= 100000
#                     items["RATE{Rs/Sqft}"] = price / area
#
#             if flag == 0:
#                 final_list.append(items)
#         num += 1
#         base_url = next_list[num]
#
#
# data_frame = pandas.DataFrame(final_list)
# data_frame.to_csv("OutPut.csv")

# CSV FILE CREATED AND FINAL_LIST ALSO CREATED
# SORTING THE LIST IN FLATS AND PLOTS
# STORING FLATS IN DATA_DICTIONARY VARIABLE
# TO SORT PLOTS AND FLATS
data_frame = pd.read_csv("OutPut.csv")
final_list = data_frame.to_dict(orient='records')
list_plot = []
data_dictionary = []
for item in final_list:
    if 'Plot' in item["PLOT/FLAT"]:
        list_plot.append(item)
    else:
        data_dictionary.append(item)



##################################################
# TO SORT DATA USNG AREA AND STORING AREA WISE FLATS
##################################################
# TO APPEND THE 1.html FILE


traversed_area_list = []
area_wise_list = []
area_dict = {}
x_axix=[]
y_axix=[]
area_name=[]
num=[]
num_list=[]
count_list=[]
for entry in data_dictionary:
    if entry["LOCALITY"] not in traversed_area_list:
        traversed_area_list.append(entry["LOCALITY"])
        area_dict[entry["LOCALITY"]] = [entry]
    else:
        area_dict[entry["LOCALITY"]].append(entry)
count = 0
count1=0
for item in area_dict:
    area_name.append(item)
    num.append(len(area_dict[item]))
    num_list.append(len(area_dict[item]))
    count += 1
    count1 += 1
    count_list.append(count1)
    if count == 3:
        x_axix.append(area_name)
        area_name=[]
        y_axix.append(num)
        num=[]
        count = 0
fig,ax=plt.subplots()
plt.bar(count_list,num_list)
fig.savefig('img/main-graph.png')
# 1  CREATING HTML PAGE FOR AREA WISE LIST
with open("graphs.html", 'w') as write_stream:
    print('<!DOCTYPE html><html lang="en"><head><title>WEBSCRAPPER</title>', file=write_stream)
    print('<link rel="stylesheet" type="text/css"  href="../css/bootstrap.css">', file=write_stream)
    print('<link rel="stylesheet" type="text/css" href="../css/style.css">', file=write_stream)
    print('<link rel="stylesheet" type="text/css" href="../css/style1.css">', file=write_stream)
    print('</head>', file=write_stream)
    print('<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">', file=write_stream)
    print('<nav id="menu" class="navbar navbar-default navbar-fixed-top">', file=write_stream)
    print('<div class="container"> ', file=write_stream)
    print('<div class="navbar-header">', file=write_stream)
    print(
        '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"><span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>',
        file=write_stream)
    print('<a class="navbar-brand page-scroll" href="#page-top">WEBSCRAPPER</a>', file=write_stream)
    print('<div class="phone"></div></div></div></nav>', file=write_stream)
    for i in range(len(x_axix)):
        fig, ax = plt.subplots()
        plt.ylabel('NUMBER OF ADS')
        plt.bar(x_axix[i], y_axix[i])
        save_name = 'img/img' + str(i) + '.png'
        fig.savefig(save_name)
        print('<section class="graph">', file=write_stream)
        print('<div class="image">', file=write_stream)
        print('<img src="'+save_name+'">', file=write_stream)
        print('</div>', file=write_stream)
        print('</section>', file=write_stream)

    print("</body>", file=write_stream)
    print("</html>", file=write_stream)


############################################################
"""
    GRAPH WEB PAGE IS CREATED TILL HERE AFTER THAT THE MAIN PAGE WORK IS IN PROGRESS
"""
############################################################
with open("1-1.html", 'w') as write_stream:
    print('<!DOCTYPE html><html lang="en"><head><title>WEBSCRAPPER</title>', file=write_stream)
    print('<link rel="stylesheet" type="text/css"  href="../css/bootstrap.css">', file=write_stream)
    print('<link rel="stylesheet" type="text/css" href="../css/style.css">', file=write_stream)
    print('<link rel="stylesheet" type="text/css" href="../css/style1.css">', file=write_stream)
    print('</head>', file=write_stream)
    print('<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">', file=write_stream)
    print('<nav id="menu" class="navbar navbar-default navbar-fixed-top">', file=write_stream)
    print('<div class="container"> ', file=write_stream)
    print('<div class="navbar-header">', file=write_stream)
    print(
        '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"><span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>',
        file=write_stream)
    print('<a class="navbar-brand page-scroll" href="#page-top">WEBSCRAPPER</a>', file=write_stream)
    print('<div class="phone"></div></div></div></nav>', file=write_stream)
    print('<section class="graph">', file=write_stream)
    print('', file=write_stream)

    for item in area_dict:
        print('<div>',file=write_stream)
        area_item = item.strip(',')
        print("<a  class='btn btn-full btn-login' href=\"python-files/area_name.php?id="+item+"\">"+item+"</a>", file=write_stream)
        print('</div>', file=write_stream)

    print('<div>', file=write_stream)
    print("<a  class='btn btn-full btn-login' href=\"2-1.py\">SHOW MORE</a>", file=write_stream)
    print('</div>', file=write_stream)
    print("</section>",file=write_stream)
    print('<section class="graph">', file=write_stream)
    print('<div class="image">', file=write_stream)
    print('<img src="img/main-graph.png">', file=write_stream)
    print('<h3 class="graph-name"> LOCALITY GRAPH </h3>', file=write_stream)
    print('</div>', file=write_stream)
    print('<div>', file=write_stream)
    print("<a  class='btn btn-full btn-login show-more' href=\"graphs.html\">SHOW GRAPHS</a>", file=write_stream)
    print('</div>', file=write_stream)
    print('</section>', file=write_stream)
    print("</body>",file=write_stream)
    print("</html>",file=write_stream)

filename = 'http://localhost/WPL/resources/php/Mainpage/python-files/1-1.html'
webbrowser.open(filename)
