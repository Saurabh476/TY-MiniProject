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

#######################################################
# BY CLICKING THE BUTTONS WE GO TO THE WEBPAGE
# WHERE ONLY WE SHOW THE INFORMATION AND JUST
# A LINK TO THE PROPERTY OF THE MAGIC BRICKS
#######################################################
prop = {}
with open("2-2.html", 'w') as write_stream:
    print('<!DOCTYPE html><html lang="en"><head><title>WEBSCRAPPER</title>', file=write_stream)
    print('<link rel="stylesheet" type="text/css"  href="../css/bootstrap.css">', file=write_stream)
    print('<link rel="stylesheet" type="text/css" href="../css/style.css">', file=write_stream)
    print('<link rel="stylesheet" type="text/css" href="../css/style1.css">', file=write_stream)
    print('</head>', file=write_stream)
    print('<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">', file=write_stream)
    print('<nav id="menu" class="navbar navbar-default navbar-fixed-top">', file=write_stream)
    print('<div class="container"> ', file=write_stream)
    print('<div class="navbar-header">', file=write_stream)
    print('<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>',file=write_stream)
    print('<a class="navbar-brand page-scroll" href="#page-top">WEBSCRAPPER</a>', file=write_stream)
    print('<div class="phone"></div></div></div></nav>', file=write_stream)

with open("python-files/costly-afford.txt",'r') as read_stream:
    read_line = read_stream.readline()

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

with open("python-files/costly-afford.txt",'w') as write_stream:
    print("20",file=write_stream)
