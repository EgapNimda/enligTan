from bs4 import BeautifulSoup
import requests

url = "https://www.almanac.com/astronomy/moon/calendar"

res = requests.get(url)
res.encoding =  "utf-8"

if res.status_code == 200:
    print("Successful")
elif res.status_code == 404:
    print("Error 404 page not found")

soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
