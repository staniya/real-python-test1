import mechanicalsoup

my_browser = mechanicalsoup.Browser()
login_page = my_browser.get("https://realpython.com/practice/login.php")
login = login_page.soup

form = login.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profile_page = my_browser.submit(form, login_page.url)
title = profile_page.soup.title
print("Title: ", title.text)

login_page = my_browser.get("https://realpython.com/practice/login.php")
title = login_page.soup.title
print("Title: ", title.text)

form = login.select("form")[0]
form.select("input")[0]["value"] = "shinn"
form.select("input")[1]["value"] = "jap"
error_page = my_browser.submit(form, login_page.url)

if error_page.soup.text.find("Wrong username or password!") != False:
    print("Login Failed")
else:
    print("Login Successful")

