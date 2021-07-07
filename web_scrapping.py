import numpy as np
import pandas as pd
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphic+cards'
# opening up connection, grabbing the page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
# html parse
page_soup = soup(page_html, 'html.parser')
print(page_soup.h1)
print(page_soup.p)
print(page_soup.body.span)

containers = page_soup.findAll('div', {'class':'item-container'})
print(len(containers))

print(containers[0])
container = containers[0]
print(container.a)
print(container.div)
print(container.div.div.a)
print(container.div.div.a.img['title'])

filename = 'products.csv'
f = open(filename, 'w')

headers = 'brand,product_name, shipping \n '
f.write(headers)
for container in containers:
    brand = container.div.div.a.img['title']
    title_container = container.findAll('a', {'class': 'item-title'})
    product_name = title_container[0].text
    shipping_container = container.findAll('li',{'class':'price-ship'})
    # strip function is used to strip the text from new line and any other spaces leaving the needed text behind
    shipping = shipping_container[0].text.strip()
    print('brand:' + brand)
    print('product_name:' + product_name)
    print('shipping' + shipping)

    f.write(brand + ',' + product_name.replace(',', '|') +','+ shipping+"\n")

f.close()




