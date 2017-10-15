import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
# driver = webdriver.Firefox()  # Optional argument, if not specified will search path.
# driver.get('http://indiatoday.intoday.in/advanced_search.jsp?option=com_search&searchword=arushi+talwar');
# time.sleep(1) 
# # search_box = driver.find_element_by_name('email')
# # search_box.send_keys('shivamkohli5522@rocketmail.com')
# #search_box.submit()
# #time.sleep(5)
# content = driver.find_elements_by_class_name('searchdotline')
# print content

# for i in content:
# 	main_window = driver.current_window_handle

# 	i.click()
# 	driver.get('http://indiatoday.intoday.in/advanced_search.jsp?option=com_search&searchword=arushi+talwar');
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




		# content = soup2.findAll("div", { "class" : "mediumcontent" })[0]
		# findContent = content.find_all('p')
		# a = 0
		# content = ''
		# for i in findContent:
		# 	# print findContent[a].text
		# 	content = content + findContent[a].text
		# 	a = a + 1

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




# http://indiatoday.intoday.in/advanced_search.jsp?advsearch=1&searchtext=arushi+talwar&searchphrase=all&searchtype=story&page=2

# http://indiatoday.intoday.in/advanced_search.jsp?option=com_search&searchword=arushi+talwar




	
# search_box.send_keys('mathsmaths')
# search_box.submit()
# #src=requests.get("").text
# time.sleep(5)
# src=driver.page_source
# soup=bs(src,"html.parser")
# soup1=soup.find_all('a',class_="_2s25")[0]
# print (soup1)
# link=soup1["href"]
# #driver.find_elements_by_class_name("_2s25")[0].is_selected
# #driver2 = webdriver.Chrome('/home/harsh/Desktop/chromedriver')  # Optional argument, if not specified will search path.
# driver.get(link);
# src=driver.page_source
# soup=bs(src,"html.parser")
# soup1=soup.find_all('a',class_="_6-6")
# for i in soup1:
# 	if i["data-tab-key"] == "friends" :
# 		k=i["href"]
# 		break

# print (k)
# link=k
# print ("done")
# driver.get(link);
# src=driver.page_source
# soup=bs(src,"html.parser")
# soup1=soup.find_all('a',class_="_3c_")
# for i in soup1:
# 	if i["name"] == "Birthdays" :
# 		k=i["href"]
# 		break

# print (k)
# link=k
# print ("done")
# driver.get(link);
# src=driver.page_source
# soup=bs(src,"html.parser")
# soup1=soup.find_all('div',class_="_3i9")[0]
# soup2=soup1.find_all('a',class_="pvs _39g5")
# #_50f8 _50f4
# print ("2")
# k=0
# for i in soup2:
# 	print ("1")
# 	soup3=i.find_all('div',class_="_50f8 _50f4")[0]
# 	title="".join([str(j) for j in soup3.contents])
# 	print (title)
# 	if title == "Birthday is in 3 days" :
# 		k=i["href"]
# 		break
# print (k)
# link=k
# print ("done")
# driver.get(link)
# print (link)
# time.sleep(15) 
# try:
# 	print (dir(search_box))
# 	search_box=driver.find_elements_by_xpath('//*[@id="js_1"]/form')
# 	print ("rolling today")
# #[@id="js_23"]/div[1]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div/div
# except:
# 	pass

# print (dir(search_box))
# #search_box.click()
# #search_box.send_keys('testing')
# #search_box.submit()

# #use the #collection_wrapper_2356318349 to uniquely pinpoint birthdays
# time.sleep(100) # Let the user actually see something!
# driver.quit()
