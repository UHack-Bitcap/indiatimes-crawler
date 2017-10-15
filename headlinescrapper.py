import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs



urls = []
finalJson_array = []
finalJson = {}


for i in range(20):
	print i
	url="http://indiatoday.intoday.in/advanced_search.jsp?advsearch=1&searchtext=arushi+talwar&searchphrase=all&searchtype=story&page=" + str(i)
	r=requests.get(url)
	 # print r
	soup = bs(r.text,"html.parser")

	data = soup.findAll("div", { "class" : "searchdotline" })
	print data

	for data in data:

		findurl = data.find("div", { "class" : "serchheadlien" })

		findurl = data.find('a', href=True)
		# print findurl

		src =  findurl['href']
		urls.append(src)

		url_of_headline= src
		r=requests.get(url_of_headline)
		print r
		soup2 = bs(r.text,"html.parser")
		########scrapping the various elements
		data = soup2.findAll("div", { "class" : "strleft" })[0]
		findHeadline = data.find_all('h1')
		# print findHeadline[0].text

		


		date = soup2.findAll("div", { "class" : "story-timedate" })[0]
		Date = date.text.encode('utf-8').split(' ')
		year = str(Date[3])
		finalDate = Date[0] + ' ' + Date[1] + ' ' + Date[2] + ' ' + year[:4]
		# print date.text





		######## returning the final json

		news_dict = { 
						"headline":str(findHeadline[0].text.encode('utf-8')), 
						"url_of_headline":url_of_headline.encode('utf-8'), 
						"date":finalDate
					}

		finalJson_array.append(news_dict)


finalJson = { "all_headlines" : finalJson_array}
f= open("all_headlines"+".json","w+")
f.write(str(finalJson_array))
f.close() 




