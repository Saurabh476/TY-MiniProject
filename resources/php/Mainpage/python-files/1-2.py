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
import matplotlib.pyplot as plt

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

with open("python-files/area_name.txt",'r') as read_stream:
    read_str = read_stream.readline().strip(' ')


if read_str in area_dict.keys():
    average_price = 0
    data_dictionary = area_dict[read_str]
    for item in data_dictionary:
        average_price += int(item["PRICE in Lacs"])
    average_price /= len(data_dictionary)

    with open("1-2.html", 'w') as write_stream:
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
            '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>',
            file=write_stream)
        print('<a class="navbar-brand page-scroll" href="#page-top">WEBSCRAPPER</a>', file=write_stream)
        print('<div class="phone"></div></div></div></nav>', file=write_stream)
        print('', file=write_stream)

        print('<section class="graph">',file=write_stream)
        print('<h1 class="sect-head-1-2">' + read_str + '</h1>', file=write_stream)
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
        print("<h3 >COSTLIEST PROPERTY PRICE : "+str(highest['PRICE in Lacs'])+"Lacs</h3>", file=write_stream)
        print("<a class='btn btn-full btn-content' href=\"costly.html\">VIEW PROPERTY INFO</a>",file=write_stream)
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
        print("<h3 >CHEAPEST PROPERTY PRICE : "+str(lowest['PRICE in Lacs'])+"Lacs</h3>", file=write_stream)
        print("<a class='btn btn-full btn-content' href=\"affordable.html\">VIEW PROPERTY INFO</a>",file=write_stream)
        print('</div>', file=write_stream)
        print('</section>',file=write_stream)

    # TO CREATE A GRAPH AND CREATE ITS IMAGE
    axix_price = []
    axix_rate = []
    axix_area = []
    i = 0
    for i in range(len(data_dictionary)):
        key = data_dictionary[i]
        j = i - 1
        while j >= 0 and data_dictionary[j]["PRICE in Lacs"] > key["PRICE in Lacs"]:
            data_dictionary[j + 1] = data_dictionary[j]
            j -= 1
        data_dictionary[j + 1] = key

    for item in data_dictionary:
        axix_rate.append(int(item["RATE{Rs/Sqft}"]))
        axix_area.append(int(item["AREA in Sqft"]))
        axix_price.append(int(item['PRICE in Lacs']))

    fig, ax = plt.subplots()
    plt.xlabel('AREA IN SQ FEET')
    plt.ylabel('PRICE IN LACKS')
    plt.plot(axix_area, axix_price, 'ro')
    fig.savefig('img/dot-graph.png')
    fig, ax = plt.subplots()
    plt.xlabel('AREA IN SQ FEET')
    plt.ylabel('RATE{Rs/Sqft}')
    plt.plot(axix_area, axix_rate)
    fig.savefig('img/line-graph.png')
    fig, ax = plt.subplots()
    plt.bar(1, len(data_dictionary))
    fig.savefig('bar2.png')

    # TO PASTE GRAPH IN WEBPAGE
    with open("1-2.html", 'a') as write_stream:
        print('<section class="graph">',file=write_stream)
        print('<div class="image">',file=write_stream)
        print("<img src=\"img/line-graph.png\">", file=write_stream)
        print('<h3 class="graph-name"> LINE GRAPH </h3>', file=write_stream)
        print('</div>', file=write_stream)
        print('</section>',file=write_stream)

        print('<section class="graph">', file=write_stream)
        print('<div class="image">', file=write_stream)
        print("<img src=\"img/dot-graph.png\">", file=write_stream)
        print('<h3 class="graph-name"> DOT GRAPH </h3>', file=write_stream)
        print('</div>', file=write_stream)
        print('</section>', file=write_stream)


    with open("1-2.html",'a') as write_stream:
        print("</body>",file=write_stream)
        print("</html>",file=write_stream)

    filename = 'http://localhost/WPL/resources/php/Mainpage/python-files/1-2.html'
    webbrowser.open(filename)
    prop = {}
    prop = highest
    with open("costly.html", 'w') as write_stream:
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
            '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>',
            file=write_stream)
        print('<a class="navbar-brand page-scroll" href="#page-top">WEBSCRAPPER</a>', file=write_stream)
        print('<div class="phone"></div></div></div></nav>', file=write_stream)

        print('<section class="graph">', file=write_stream)
        print('<h1 class="sect-head">COSTLY PROPERTY</h1>',file=write_stream)
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

    prop = lowest
    with open("affordable.html", 'w') as write_stream:
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
            '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>',
            file=write_stream)
        print('<a class="navbar-brand page-scroll" href="#page-top">WEBSCRAPPER</a>', file=write_stream)
        print('<div class="phone"></div></div></div></nav>', file=write_stream)

        print('<section class="graph">', file=write_stream)
        print('<h1 class="sect-head">AFFORDABLE PROPERTY</h1>', file=write_stream)
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
            "<a class='btn btn-full btn-content1' href=\"" + highest[
                'LINK'] + "\">CLICK HERE TO GO TO PROPERTY</a>",
            file=write_stream)
        print('</section>', file=write_stream)

        print("</body>", file=write_stream)
        print("</html>", file=write_stream)