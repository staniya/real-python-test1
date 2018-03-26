import mechanicalsoup
from time import sleep

my_browser = mechanicalsoup.Browser()

#obtain 1 stock quote per minute for the next 3 minutes
for i in range(0, 3):
    page = my_browser.get("https://finance.yahoo.com/quote/ES=F?p=ES=F")
    html_text = page.soup
    #return a list of all the tags where the id is 'yfs_184_yhoo'
    my_tags = html_text.select('.Trsdu(0.3s) ')
    my_time = html_text.select('.Trsdu(0.3s) ')
    #take the BeautifulSoup string out of the first (and only) <span> tag
    #my_price = my_tags[0].text
    print("The price of E-mini S&P 500 Index Futures is {} at {}".format(my_tags, my_time))
    if i<2: #wait a minute if this isn't the last request
        sleep(60)
