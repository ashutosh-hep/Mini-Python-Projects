import requests
from bs4 import BeautifulSoup

a = input("Enter the name of city:::")

page = requests.get("https://www.policybazaar.com/gold-rate-"+a)

#print(page)

scrapped_data = BeautifulSoup(page.content, "html.parser")

price = scrapped_data.find_all(class_="dailyGoldrate")

#print(price)

for i in price:
    print("Gold price for per 10 gram in "+a+" is : : INR "+i.get_text())
    break
