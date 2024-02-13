import requests
import pandas
from bs4 import BeautifulSoup
# import openpyxl
content = requests.get("https://www.flipkart.com/laptops-store").text
soup = BeautifulSoup(content, "html.parser")
laptop_details = []
title = soup.find_all(class_="s1Q9rs")
price = soup.find_all(class_="_30jeq3")
laptop_list = [(each.getText().split("-")[0]) for each in title]
price_details = [(each.getText()) for each in price]
data_dict = {
    "model": laptop_list,
    "price": price_details
}

df = pandas.DataFrame(data_dict)
df.to_excel('laptops.xlsx')
