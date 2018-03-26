from urllib.request import urlopen
import requests
import re

url = "https://realpython.com/practice/dionysus.html"
html_page = urlopen(url)
html_text = html_page.read().decode('utf-8')

print(html_text)

name = "Name:"
end_tag = "</h2>"
favorite_color = "Favorite Color:"
end_tag2 = "</center>"

index = html_text.find(name)
index_end = html_text.find(end_tag)
index2 = html_text.find(favorite_color)
index2_end = html_text.find(end_tag2)
print(html_text[index: index_end])
print(html_text[index2: index2_end])

match_results = re.search("<h2>.*</h2>", html_text, re.IGNORECASE)
match_results2 = re.search("<br>.*</center>", html_text, re.IGNORECASE)

for tag in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
    match_results = re.search(tag, html_text)
    group = match_results.group()
    results = re.sub("<.*?>", "", group)
    print(results.strip(" \n<"))
