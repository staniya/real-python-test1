from urllib.request import urlopen
import requests
import re

my_adress = "https://realpython.com/practice/aphrodite.html"

html_page = urlopen(my_adress)

html_text = html_page.read().decode('utf-8')

start_tag = "<title>"
end_tag = "</title>"

start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

print(html_text[start_index:end_index])

print(re.findall("ab*c", "ABC", re.IGNORECASE))
#returns all functions that starts with a and ends with c with 0 or more bs in between

print(re.findall("a.c", "acc"))
#returns all functions where there is a character in between a and c

print(re.findall("a.*c", "abc"))
#returns all functions where any character between is being repeated any number of times

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())

my_string = "Everything is <replaced> if it's in <tags>."
my_string = re.sub("<.*?>", "ELEPHANTS", my_string)
#*? tries to match the shortest possible string of text
print(my_string)


my_address2 = "https://realpython.com/practice/dionysus.html"

html_page = urlopen(my_address2)
html_text = html_page.read().decode('utf-8')
#Python 3: html_text = html_page.read().decode('utf-8')

match_results = re.search("<title.*?>.*</title.*?>", html_text, re.IGNORECASE)

title = match_results.group()
title = re.sub("<.*?>", "", title) #remove HTML tags

print(title)
