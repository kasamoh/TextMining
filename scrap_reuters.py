# coding: utf-8
import requests
import unittest
from bs4 import BeautifulSoup




import urllib
from lxml import etree
from lxml import html
import requests
import urllib

import re   # regex


link = "http://www.somesite.com/details.pl?urn=2344"

f = urllib.request.urlopen(url)


res = requests.get(url)

url =  "http://www.example.com/servlet/av/ResultTemplate=AVResult.html"
response= urllib.request.urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)

tree.xpath(xpathselector)
res = requests.post(url, data = {'q': query })


res = requests.get(url)
html_doc =  res.text
soup = BeautifulSoup(html_doc,"html.parser")
soup.find("span", {'style':'font-size: 23px;'}).text
change_rate=soup.find("td", {'class':'data'}).text



#//*[@id="headerQuoteContainer"]/div[1]/div/span[2]

url="https://www.reuters.com/finance/stocks/financial-highlights/LVMH.PA"



listetables=soup.findAll("tr", {'class':'stripe'})

str(aa).find("Quarter") != -1







def _handle_request_result_and_build_soup(request_result):
  if request_result.status_code == 200:
    html_doc =  request_result.text
    soup = BeautifulSoup(html_doc,"html.parser")
    return soup


def _convert_string_to_float(string):
    regex = re.compile(r'[\n\r\t]')
    s = regex.sub(" ", str(string))
    s=s.replace("€","")
    s=s.replace(",","")
    return float(s.strip())


def get_price_change_query(query):
    
    url="https://www.reuters.com/finance/stocks/financial-highlights/LVMH.PA"
    res = requests.get(url)
    soup = _handle_request_result_and_build_soup(res)
    change_class={'style':'font-size: 23px;'}
    stock_class = {'style':'font-size: 23px;'}
    stock_price =soup.find("span",change_class).text
    change=soup.find("span",stock_class).text

    return [_convert_string_to_float(stock_price),_convert_string_to_float(change)]


def get_quartermean (query):
    
    url="https://www.reuters.com/finance/stocks/financial-highlights/LVMH.PA"
    res = requests.get(url)
    soup = _handle_request_result_and_build_soup(res)
    
    listetables=soup.findAll("tr", {'class':'stripe'})

    found=False
    k=0

    while( found==False and k < len(listetables) ):
        found=str(listetables[k]).find("Quarter") != -1
        print(found)
        k=k+1

    if found : 
        quarterlist=listetables[k-1]
        quarterlist= quarterlist.findAll("td",{'class':'data'})[1]
        quartermean=quarterlist.findAll("td",{'class':'data'})[1].text
        
    return quartermean

def get_share_count_for_page(page_url):
  res = requests.get(page_url)
  soup = _handle_request_result_and_build_soup(res)
  specific_class = "c-sharebox__stats-number"
  share_count_text = soup.find("span", class_= specific_class).text
  return  _convert_string_to_int(share_count_text)

def get_popularity_for_people(people):
  query = people
  url_people = get_all_links_for_query(query)
  results_people = []
  for url in url_people:
      results_people.append(get_share_count_for_page(website_prefix + url))
  return sum(results_people)


class Lesson1Tests(unittest.TestCase):
    def testShareCount(self):
        self.assertEqual(get_share_count_for_page("http://www.purepeople.com/article/brigitte-macron-decroche-une-jolie-couv-a-l-etranger_a306389/1") , 86)

    def testConvertStringInt(self):
        self.assertEqual(_convert_string_to_int("\n                            86\n                    ") , 86)
        self.assertEqual(_convert_string_to_int("5,84K") , 5840)
        self.assertEqual(_convert_string_to_int("\n                            1,6K\n                   ") , 1600)
        
        
macron = get_popularity_for_people('macron')
melenchon = get_popularity_for_people('melenchon')

def main():
    unittest.main()

if __name__ == '__main__':
    main()