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


with open('python-files/urls.txt','r') as read_stream:
    read_line = read_stream.readline().strip(' ')
    read_line = int(read_line)
if read_line == 0:
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
    # data_frame = pd.read_csv("OutPut.csv")
    # final_list = data_frame.to_dict(orient='records')
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
    for entry in data_dictionary:
        if entry["LOCALITY"] not in traversed_area_list:
            traversed_area_list.append(entry["LOCALITY"])
            area_dict[entry["LOCALITY"]] = [entry]
        else:
            area_dict[entry["LOCALITY"]].append(entry)


    # 1  CREATING HTML PAGE FOR AREA WISE LIST

    with open("1-1.html", 'w') as write_stream:
        print('<!DOCTYPE html><html lang="en"><head><title>MAGICSCRAPPER</title>', file=write_stream)
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
        print('<a class="navbar-brand page-scroll" href="#page-top">MAGIC SCRAPPER</a>', file=write_stream)
        print('<div class="phone"></div></div></div></nav>', file=write_stream)
        print('<section class="graph">', file=write_stream)
        print('', file=write_stream)
        print('', file=write_stream)
        for item in area_dict:
            print('<div>',file=write_stream)
            area_item = item.strip(',')
            print("<a  class='btn btn-full btn-login' href=\"python-files/1.php?id="+item+"\">"+item+"</a>", file=write_stream)
            print('</div>', file=write_stream)

        print('<div>', file=write_stream)
        print("<a  class='btn btn-full btn-login' href=\"python-files/3.php?id=2\">SHOW MORE</a>", file=write_stream)
        print('</div>', file=write_stream)
        print("</section>",file=write_stream)
        print("</body>",file=write_stream)
        print("</html>",file=write_stream)

    with open('python-files/urls.txt', 'w') as write_stream:
        print('1',file=write_stream)

    filename = 'http://localhost/WPL/resources/php/Mainpage/python-files/1-1.html'
    webbrowser.open(filename)
###############################################################
# FROM HERE ALL THE STUFF DISPLAYED IS OF A SPECIAL AREA ONLY #
###############################################################

################## AFTER CLICKING THE BUTTON #########################
# TO FIND AVERAGE HIGHEST LOWEST AND GRAPH IE 1.1HTML #
####################### AVERAGE PRICE IN LACS ########################


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
for entry in data_dictionary:
    if entry["LOCALITY"] not in traversed_area_list:
        traversed_area_list.append(entry["LOCALITY"])
        area_dict[entry["LOCALITY"]] = [entry]
    else:
        area_dict[entry["LOCALITY"]].append(entry)

with open("python-files/urls1.txt",'r') as read_stream:
    read_str = read_stream.readline().strip(' ')


if read_str in area_dict.keys():
    average_price = 0
    data_dictionary = area_dict[read_str]
    for item in data_dictionary:
        average_price += int(item["PRICE in Lacs"])
    average_price /= len(data_dictionary)

    with open("1-2.html", 'w') as write_stream:
        print('<!DOCTYPE html><html lang="en"><head><title>MAGICSCRAPPER</title>', file=write_stream)
        print('<link rel="stylesheet" type="text/css"  href="../css/bootstrap.css">', file=write_stream)
        print('<link rel="stylesheet" type="text/css" href="../css/style.css">', file=write_stream)
        print('<link rel="stylesheet" type="text/css" href="../css/style1.css">', file=write_stream)
        print('</head>', file=write_stream)
        print('<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">', file=write_stream)
        print('<nav id="menu" class="navbar navbar-default navbar-fixed-top">', file=write_stream)
        print('<div class="container"> ', file=write_stream)
        print('<div class="navbar-header">', file=write_stream)
        print(
            '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>',
            file=write_stream)
        print('<a class="navbar-brand page-scroll" href="#page-top">MAGIC SCRAPPER</a>', file=write_stream)
        print('<div class="phone"></div></div></div></nav>', file=write_stream)
        print('', file=write_stream)
        print('', file=write_stream)

        print('<section class="graph">',file=write_stream)
        print('<div>',file=write_stream)
        print("<h3 >AVERAGE PRICE : "+str(average_price)+"</h3>", file=write_stream)
        print('</div>', file=write_stream)
        print('</section>',file=write_stream)


    # TO FIND THE COSTLIEST PROPERTY AND COSTLY AREA
    highest = data_dictionary[0]
    for item in data_dictionary:
        if item["PRICE in Lacs"] > highest["PRICE in Lacs"]:
            highest = item
    with open("1-2.html", 'a') as write_stream:
        print('<section class="graph">',file=write_stream)
        print('<div>',file=write_stream)
        print("<h3 >HIGHEST PRICE : "+str(highest['PRICE in Lacs'])+"Lacs</h3>", file=write_stream)
        print("<a class='btn btn-full btn-content' href=\""+highest['LINK']+"\">CLICK HERE TO GO TO PROPERTY</a>",file=write_stream)
        print('</div>', file=write_stream)
        print('</section>',file=write_stream)



    # TO FIND THE LOWEST
    lowest = data_dictionary[0]
    for item in data_dictionary:
        if item["PRICE in Lacs"] < lowest["PRICE in Lacs"]:
            lowest = item

    with open("1-2.html", 'a') as write_stream:
        print('<section class="graph">',file=write_stream)
        print('<div>',file=write_stream)
        print("<h3 >LOWEST PRICE : "+str(lowest['PRICE in Lacs'])+"Lacs</h3>", file=write_stream)
        print("<a class='btn btn-full btn-content' href=\""+lowest['LINK']+"\">CLICK HERE TO GO TO PROPERTY</a>",file=write_stream)
        print('</div>', file=write_stream)
        print('</section>',file=write_stream)

    # TO CREATE A GRAPH AND CREATE ITS IMAGE
    # axix1 = []
    # i = 0
    # for i in range(len(data_dictionary)):
    #     key = data_dictionary[i]
    #     j = i - 1
    #     while j >= 0 and data_dictionary[j]["PRICE in Lacs"] > key["PRICE in Lacs"]:
    #         data_dictionary[j + 1] = data_dictionary[j]
    #         j -= 1
    #     data_dictionary[j + 1] = key
    # for item in data_dictionary:
    #     axix1.append(int(item["RATE{Rs/Sqft}"]))
    # fig, ax = plt.subplots()
    # plt.plot(axix1)
    # fig.savefig('img/graph2.png')
    # TO PASTE GRAPH IN WEBPAGE
    with open("1-2.html", 'a') as write_stream:
        print('<section class="graph">',file=write_stream)
        print('<div class="image">',file=write_stream)
        print("<img src=\"img/graph2.png\">", file=write_stream)
        print('<h3> DOT GRAPH </h3>', file=write_stream)
        print('</div>', file=write_stream)
        print('</section>',file=write_stream)


    with open("1-2.html",'a') as write_stream:
        print("</body>",file=write_stream)
        print("</html>",file=write_stream)

    with open("python-files/urls1.txt",'w') as write_stream:
        print("NOTHING",file=write_stream)

    filename = 'http://localhost/WPL/resources/php/Mainpage/python-files/1-2.html'
    webbrowser.open(filename)

#######################################################
# AFTER CLICKING SHOW MORE BUTTON IN 1 IE 2-1-SHOW MORE
# PHP FILE IS USED TO WRITE THE ID IN THE TXT FILE
# SO THAT WE CAN DECIDE WHICH MODULE TO RUN
# IE COSTLY OR THE AFFORDABLE
#######################################################
with open("python-files/urls3.txt",'r') as read_stream:
    read_line = read_stream.readline().strip(' ')

if read_line == '2':
    with open("2-1.html", 'w') as write_stream:
        print('<!DOCTYPE html><html lang="en"><head><title>MAGICSCRAPPER</title>', file=write_stream)
        print('<link rel="stylesheet" type="text/css"  href="../css/bootstrap.css">', file=write_stream)
        print('<link rel="stylesheet" type="text/css" href="../css/style.css">', file=write_stream)
        print('<link rel="stylesheet" type="text/css" href="../css/style1.css">', file=write_stream)
        print('</head>', file=write_stream)
        print('<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">', file=write_stream)
        print('<nav id="menu" class="navbar navbar-default navbar-fixed-top">', file=write_stream)
        print('<div class="container"> ', file=write_stream)
        print('<div class="navbar-header">', file=write_stream)
        print(
            '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>',
            file=write_stream)
        print('<a class="navbar-brand page-scroll" href="#page-top">MAGIC SCRAPPER</a>', file=write_stream)
        print('<div class="phone"></div></div></div></nav>', file=write_stream)
        print('<section class="graph">', file=write_stream)
        print('', file=write_stream)
        print('', file=write_stream)

        print('<div>', file=write_stream)
        print("<a class='btn btn-full btn-login' href=\"python-files/2.php?id=11\">COSTLIEST PROPERTY</a>", file=write_stream)
        print('</div>', file=write_stream)

        print('<div>', file=write_stream)
        print("<a class='btn btn-full btn-login' href=\"python-files/2.php?id=22\">AFFORDABLE PROPERTY</a>", file=write_stream)
        print('</div>', file=write_stream)


    # TO FIND THE COSTLIEST PROPERTY AND COSTLY AREA
    highest = data_dictionary[0]
    for item in data_dictionary:
        if item["PRICE in Lacs"] > highest["PRICE in Lacs"]:
            highest = item

    with open("2-1.html", 'a') as write_stream:
        print('<div class="info">', file=write_stream)
        print("<h3 >COSTLY AREA : " + str(highest['LOCALITY']) + "</h3>", file=write_stream)
        print('</div>', file=write_stream)

    # TO FIND THE LOWEST
    lowest = data_dictionary[0]
    for item in data_dictionary:
        if item["PRICE in Lacs"] < lowest["PRICE in Lacs"]:
            lowest = item

    with open("2-1.html", 'a') as write_stream:
        print('<div class="info">', file=write_stream)
        print("<h3 >AFFORDABLE AREA : " + str(lowest['LOCALITY']) + "</h3>", file=write_stream)
        print('</div>', file=write_stream)

    with open("2-1.html", 'a') as write_stream:
        print('</section>', file=write_stream)
        print("</body>", file=write_stream)
        print("</html>", file=write_stream)

    with open("python-files/urls3.txt",'w') as write_stream:
        print("",file=write_stream)

    filename = 'http://localhost/WPL/resources/php/Mainpage/python-files/2-1.html'
    webbrowser.open(filename)

#######################################################
# BY CLICKING THE BUTTONS WE GO TO THE WEBPAGE
# WHERE ONLY WE SHOW THE INFORMATION AND JUST
# A LINK TO THE PROPERTY OF THE MAGIC BRICKS
#######################################################
prop = {}
with open("2-2.html", 'w') as write_stream:
    print('<!DOCTYPE html><html lang="en"><head><title>MAGICSCRAPPER</title>',file=write_stream)
    print('<link rel="stylesheet" type="text/css"  href="../css/bootstrap.css">',file=write_stream)
    print('<link rel="stylesheet" type="text/css" href="../css/style.css">',file=write_stream)
    print('<link rel="stylesheet" type="text/css" href="../css/style1.css">',file=write_stream)
    print('</head>',file=write_stream)
    print('<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">',file=write_stream)
    print('<nav id="menu" class="navbar navbar-default navbar-fixed-top">',file=write_stream)
    print('<div class="container"> ',file=write_stream)
    print('<div class="navbar-header">',file=write_stream)
    print('<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>',file=write_stream)
    print('<a class="navbar-brand page-scroll" href="#page-top">MAGIC SCRAPPER</a>',file=write_stream)
    print('<div class="phone"></div></div></div></nav>',file=write_stream)
    print('',file=write_stream)
    print('',file=write_stream)
with open("python-files/urls2.txt",'r') as read_stream:
    read_line = read_stream.readline()
if read_line == '\n':
    print()
elif read_line == '':
    print()
else:
    read_line = int(read_line.strip('\n').strip(' '))
    if read_line == 11:
        highest = data_dictionary[0]
        for item in data_dictionary:
            if item["PRICE in Lacs"] > highest["PRICE in Lacs"]:
                highest = item
        prop = highest
        with open("2-2.html", 'a') as write_stream:
            print('<section class="graph">', file=write_stream)
            print('<h1 class="sect-head">COSTLIEST PROPERTY</h1>',file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >AREA IN SQ FEET : " + str(prop['AREA in Sqft']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print('</section>', file=write_stream)

            print('<section class="graph">', file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >PRICE PER SQ FEET IN RUPEES : " + str(prop['RATE{Rs/Sqft}']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print('</section>', file=write_stream)

            print('<section class="graph">', file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >TOTAL COST IN LACS : " + str(prop['PRICE in Lacs']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print('</section>', file=write_stream)

            print('<section class="graph">', file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >LOCALITY : " + str(prop['LOCALITY']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print('</section>', file=write_stream)

            print('<section class="graph">', file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >OWNER : " + str(prop['OWNER']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print(
                "<a class='btn btn-full btn-content1' href=\"" + highest['LINK'] + "\">CLICK HERE TO GO TO PROPERTY</a>",
                file=write_stream)
            print('</section>', file=write_stream)

            print("</body>", file=write_stream)
            print("</html>", file=write_stream)
            filename = 'http://localhost/WPL/resources/php/Mainpage/python-files/2-2.html'
            webbrowser.open(filename)
    elif read_line == 22:
        lowest = data_dictionary[0]
        for item in data_dictionary:
            if item["PRICE in Lacs"] < lowest["PRICE in Lacs"]:
                lowest = item

        prop = lowest
        with open("2-2.html", 'a') as write_stream:
            print('<section class="graph">', file=write_stream)
            print('<h1 class="sect-head">AFFORDABLE PROPERTY</h1>',file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >AREA IN SQ FEET : " + str(prop['AREA in Sqft']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print('</section>', file=write_stream)

            print('<section class="graph">', file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >PRICE PER SQ FEET IN RUPEES : " + str(prop['RATE{Rs/Sqft}']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print('</section>', file=write_stream)

            print('<section class="graph">', file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >TOTAL COST IN LACS : " + str(prop['PRICE in Lacs']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print('</section>', file=write_stream)

            print('<section class="graph">', file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >LOCALITY : " + str(prop['LOCALITY']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print('</section>', file=write_stream)

            print('<section class="graph">', file=write_stream)
            print('<div>', file=write_stream)
            print("<h3 >OWNER : " + str(prop['OWNER']) + "</h3>", file=write_stream)
            print('</div>', file=write_stream)
            print(
                "<a class='btn btn-full btn-content1' href=\"" + lowest['LINK'] + "\">CLICK HERE TO GO TO PROPERTY</a>",
                file=write_stream)
            print('</section>', file=write_stream)

            print("</body>", file=write_stream)
            print("</html>", file=write_stream)
            filename = 'http://localhost/WPL/resources/php/Mainpage/python-files/2-2.html'
            webbrowser.open(filename)

with open("python-files/urls2.txt",'w') as write_stream:
    print("20",file=write_stream)
