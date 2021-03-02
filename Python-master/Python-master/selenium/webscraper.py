from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'http://kenhan.org'

chrome_path = '/Users/jesusmedina/Downloads/chromedriver'

options = Options()
options.headless = True

chrome = webdriver.Chrome(executable_path=chrome_path, options=options)

chrome.get(url)

name = chrome.find_element_by_xpath('//*[@id="latestnews"]/li/table/tbody/tr/td[2]/div/p/a[1]').text
email = chrome.find_element_by_xpath('//*[@id="latestnews"]/li/table/tbody/tr/td[2]/div/p/a[2]').text
phone = chrome.find_element_by_xpath('//*[@id="latestnews"]/li/table/tbody/tr/td[2]/div/p/a[4]').text
office = chrome.find_element_by_xpath('//*[@id="latestnews"]/li/table/tbody/tr/td[2]/div/p/a[3]').text
office_hours = chrome.find_element_by_xpath('//*[@id="latestnews"]/li/table/tbody/tr/td[2]/div/p/a[5]').text

print(str(name) + "\n"
        + email + "\n"
        + phone + "\n"
        + office + "\n"
        + office_hours)


input('Enter any key to quit')
chrome.close()
chrome.quit()
print('finished')

