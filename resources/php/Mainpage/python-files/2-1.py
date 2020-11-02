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



"""
# TO SORT DATA USNG AREA AND STORING AREA WISE FLATS
##################################################
# TO APPEND THE 1.html FILE
"""

traversed_area_list = []
area_wise_list = []
area_dict = {}
for entry in data_dictionary:
    if entry["LOCALITY"] not in traversed_area_list:
        traversed_area_list.append(entry["LOCALITY"])
        area_dict[entry["LOCALITY"]] = [entry]
    else:
        area_dict[entry["LOCALITY"]].append(entry)

"""
#######################################################
# AFTER CLICKING SHOW MORE BUTTON IN 1 IE 2-1-SHOW MORE
# PHP FILE IS USED TO WRITE THE ID IN THE TXT FILE
# SO THAT WE CAN DECIDE WHICH MODULE TO RUN
# IE COSTLY OR THE AFFORDABLE
#######################################################
"""
with open("2-1.html", 'w') as write_stream:
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
    print('', file=write_stream)
    print('', file=write_stream)

    print('<div>', file=write_stream)
    print("<a class='btn btn-full btn-login' href=\"python-files/show_more.php?id=11\">COSTLIEST PROPERTY</a>", file=write_stream)
    print('</div>', file=write_stream)

    print('<div>', file=write_stream)
    print("<a class='btn btn-full btn-login' href=\"python-files/show_more.php?id=22\">AFFORDABLE PROPERTY</a>", file=write_stream)
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

filename = 'http://localhost/WPL/resources/php/Mainpage/python-files/2-1.html'
webbrowser.open(filename)
