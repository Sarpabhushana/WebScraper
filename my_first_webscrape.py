from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


#target url
my_url = 'https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=graphic+cards'

# opening up connection and grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing

page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"s-item-container"})


filename = "products.csv"
f = open(filename,"w")

headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
	brand = container.div.div.a.img["alt"]
	title_container = container.findAll("h2", {"class":"a-size-medium s-inline s-access-title a-text-normal"})
	product_name = title_container[0].text
	shipping_container = container.findAll("span",{"class":"a-size-small a-color-secondary"})
	shipping = shipping_container[2].text.strip()
	print("brand :" + brand)
	print("product_name :" + product_name)
	print("shipping :" + shipping) 

	f.write(brand + "," + product_name + "," + shipping+"\n")



f.close()