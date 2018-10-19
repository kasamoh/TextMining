



url="https://www.darty.com/nav/recherche?s=prix_desc&npk=1&text=dell&fa=756"


# domcomagent ; navuateur , ortable , 
#spoofer

#accesss token  --- digit cote --- Oauth  ( ermet de controler l'acces engroupet l'autorisationd'acce s , )
#json est le format le plus utilisé pour communiquer avec les api
### il vaut ieux avoir exploraeur json : installer jsonformatter 


#omdb api
# jiq
# iftt : annuairedes api pour counquer entre ux
# lire la doc sur pandas
# book : python for data analysis

res = requests.get(url)
html_doc = res.text



def getdiscountp(query):
    soup = _handle_request_result_and_build_soup(res)  
    change_class={'class':'darty_prix_barre_remise darty_small separator_top'}
    reduc =soup.findAll("p",change_class)
    listered=list(map(lambda x:x.text , reduc))
    return(list(map(lambda x:_convert_string_to_float(x),listered)))











import requests
import unittest
from bs4 import BeautifulSoup
import urllib
from lxml import etree
from lxml import html
import requests
import urllib
import re   # regex



base = "https://www.reuters.com/finance/stocks/financial-highlights/"




def _handle_request_result_and_build_soup(request_result):
  if request_result.status_code == 200:
    html_doc =  request_result.text
    soup = BeautifulSoup(html_doc,"html.parser")
    return soup


def _convert_string_to_float(string):
    regex = re.compile(r'[\n\r\t]')
    s = regex.sub(" ", str(string))
    s=s.replace("%","")
    s=s.replace("-","")
    return float(s.strip())


def get_price_change_query(query):
    
    url=base+query
    res = requests.get(url)
    soup = _handle_request_result_and_build_soup(res)
    stock_class = {'style':'font-size: 23px;'}
    stock_price =soup.find("span",stock_class).text
    
    change_class={'class':'neg'}
    stock_change =soup.findAll("span",change_class)[1].text

    return {'stock_price':_convert_string_to_float(stock_price),'stock_change':_convert_string_to_float(stock_change)/100}


def get_quartermean (query):
    
    url=base+query
    res = requests.get(url)
    soup = _handle_request_result_and_build_soup(res)
    
    listetables=soup.findAll("tr", {'class':'stripe'})

    found=False
k=0












from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# load some test data for demonstration and plot a wireframe
X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
plt.show()
# rotate the axes and update
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

plt.show()


6*******6