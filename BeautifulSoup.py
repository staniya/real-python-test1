from bs4 import BeautifulSoup
from urllib.request import urlopen

my_address = "https://realpython.com/practice/dionysus.html"

html_page = urlopen(my_address)
html_text = html_page.read().decode('UTF-8')

my_soup  = BeautifulSoup(html_text)

print(my_soup.gettext())

image1, image2 = my_soup.find_all("img")
print(image1[src])
print(image2[src])

print(my_soup.title)
print(my_soup.title.string) #only prints out the string attribute stored in the title

print(my_soup).find_all("img", src="dionysus.jpg")
