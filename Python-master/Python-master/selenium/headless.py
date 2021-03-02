from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
#mport xlwt
#from xlwt import Workbook

options = Options()
chrome_path = "/Users/jesusmedina/Downloads/chromedriver"
options.headless = True

chrome = webdriver.Chrome(executable_path=chrome_path, options=options)
chrome.get("https://www.sephora.com/beauty/new-makeup?icid2=meganav_new_justarrived_makeup_link")
sleep(3)
chrome.get_screenshot_as_file("capture.png")
name = chrome.find_elements_by_class_name("css-ktoumz")
price = chrome.find_elements_by_class_name("css-68u28a")

for i in name:
    print(i.text)

name_list = []
price_list = []

for i in name:
    name_list.append(i.text)

for j in price:
    price_list.append(j.text)

wb = Workbook()

sheet1 = wb.add_sheet('sephora')
sheet1.write(0,0, 'Product Name')
sheet1.write(0, 1, 'Price')

x = 1

for i in name_list:
    sheet1.write(x, 0, i)
    x += 1
x = 1
for i in price_list:
    sheet1.write(x, 1, i)
    x += 1

wb.save('sephora.xls')

#mapped = [shoe_list, price_list]

#for i in zip(*mapped):
#  print(*i)

input("Enter anything to quit")
chrome.close()
chrome.quit()
print("finished")