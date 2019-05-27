# testing a couple of website
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})
# for container in containers:
#     brand = container.div.div["title"]
#     brand[0].text
    # title_container = container.findAll("a",{"class":"item-title"})
    # product_name = title_container[0].text
print (containers)