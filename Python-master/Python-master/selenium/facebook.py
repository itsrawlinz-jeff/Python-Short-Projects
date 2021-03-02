from selenium import webdriver
from time import sleep
import getpass

class Facebook:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        url = 'https://hosted13.renlearn.com/272178/public/rpm/login/Login.aspx?srcID=t'
        chrome = webdriver.Chrome('/Users/jesusmedina/Downloads/chromedriver')
        chrome.get(url)

        username_text = chrome.find_element_by_id('tbUserName')
        password_text = chrome.find_element_by_id('tbPassword')

        username_text.send_keys(self.username)
        password_text.send_keys(self.password)

        login = chrome.find_element_by_id('btnLogIn')
        login.click()
        sleep(5)

user = input('Enter the username: ')
passwd = getpass.getpass("Enter password: ")

fb = Facebook(user, passwd)

fb.login()