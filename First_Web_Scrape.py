"""
This was my first web scraping project. I was scraping graphics cards information
from newegg. I couldn't finish it because I was halted by a 'Robot' check, 
<h1>Robot?</h1>. Was a sad day :'(
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

'''
Here, I would have continue writing code to put the info in an csv file if it
weren't for the 'Robot' check. Here is what I would write tho:

with open("graphics_cards.csv", "w") as f:
	headers = "brand, product_name, shipping\n"
	f.write(headers)
'''

for container in containers:
	brand = container.div.div.a.img["title"] #traceback here
	'''brand_name = container.findAll("a", {"class":"item-brand"})
	brand = brand_name'''
	
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()
	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping: " + shipping)

	#f.write(brand + "," + product_name.replace(",", "|") + shipping + "\n")

'''
I had trouble printing out the brand name. It printed them out, however, I had a
traceback error. Either an attribute error of 'NoneType' or where index was out 
of bounds. I learned I can fix the latter with try: (dosomething)/except: pass.
'''
print(page_soup.h1) #prints out <h1>Robot?</h1>
