import requests
from bs4 import BeautifulSoup


html = requests.get("http://www.w3schools.com/cssref/css_colors.asp").text

soup = BeautifulSoup(html)

rows = soup.findAll("div", {"class": "w3-col l4 m6 w3-center colorbox"})

print("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
print("<resources>")

for row in rows:
    colorName = row.find("span", {"class": "colornamespan"}).text
    colorValue = row.find("span", {"class": "colorhexspan"}).text
    print("    <color name=\"{}\">{}</color>".format(colorName, colorValue))

print("</resources>")
