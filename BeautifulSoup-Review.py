from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = "https://realpython.com/practice/"
address = base_url + "profiles.html"
html_page = urlopen(address)
html_text = html_page.read().decode('utf-8')
print(html_text)

my_soup = BeautifulSoup(html_text, "html.parser")

for urls in my_soup.find_all("a"):
    # You can use the code below for urlparse.urljoin()
    # aphrodite = new_url + "aphrodite.html"
    # poseidon = new_url + "poseidon.html"
    # dionysus = new_url + "dionysus.html"
    #
    # aprodite_page = urlopen(aphrodite)
    # aphroidte_text = aphrodite_page.read().decode('utf-8')
    #
    # poseidon_page = urlopen(poseidon)
    # poseidon_text = poseidon_page.read().decode('utf-8')
    #
    # dionysus_page = urlopen(dionysus)
    # dionysus_text = dionysus_page.read().decode('utf-8')
    # soupA = BeautifulSoup(aphoridte_text, "html.parser")
    # soupB = BeautifulSoup(poseidon_text, "html.parser")
    # soupC = BeautifulSoup(dionysus_text, "html.parser")
    new_url = base_url + urls["href"]
    new_pages = urlopen(new_url)
    new_text = new_pages.read().decode('utf-8')
    new_soup = BeautifulSoup(new_text, "html.parser")
    print(new_soup.get_text())
