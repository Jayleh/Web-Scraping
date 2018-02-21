"""
This was my first web scraping project. I was scraping graphics cards information
from newegg. I couldn't finish it because I was halted by a 'Robot' check, 
<h1>Robot?</h1>.

No recaptcha at the moment. Made a few changes; fixed the traceback AatributeError
and wrote code so that commas were taken out of brand names, i.e. "PNY Tech, Inc"
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

with open("graphics_cards.csv", "w") as f:
    headers = "brand, product_name, shipping\n"
    f.write(headers)

for container in containers:
    # AttributeError of 'NoneType' here, fixed with try/except
    try:
        brand = container.div.div.a.img["title"]
    except AttributeError:
        pass

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + str(brand))
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand.replace(",", "") + "," + product_name.replace(",", "|") + "," + shipping + "\n")
