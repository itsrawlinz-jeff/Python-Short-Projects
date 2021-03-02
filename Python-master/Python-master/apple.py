from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
chrome_path =  "/Users/jesusmedina/Downloads/chromedriver"
options.headless = True

chrome = webdriver.Chrome(executable_path=chrome_path, options=options)
chrome.get("https://www.apple.com/us-hed/shop/refurbished/mac/macbook-pro")
sleep(3)

prod = chrome.find_elements_by_class_name('as-producttile-tilelink')
prod_price = chrome.find_elements_by_class_name("as-price-currentprice")

apple_macbooks = []
macbook_prices = []

for i in prod:
    print(i.text)
for i in prod_price:
    print(i.text)
for i in prod:
    apple_macbooks.append(i.text)

for i in prod_price:
    macbook_prices.append(i.text)


print ("# of results : ", len(prod))



