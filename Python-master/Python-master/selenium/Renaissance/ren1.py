from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import xlwt
from xlwt import Workbook
import getpass

#from seleniuminformation import ren_user, ren_passwd

ren_user = input('Enter username: ')
ren_passwd = getpass.getpass("Enter password: ")

url = "https://hosted13.renlearn.com/272178/public/rpm/login/Login.aspx?srcID=t"

#option for headless selenium chrome driver
options = Options()
chrome_path = '/Users/jesusmedina/Downloads/chromedriver'
options.headless = True
chrome = webdriver.Chrome(executable_path=chrome_path, options=options)

#launching chrome with the desired url in the background
chrome.get(url)

#logging into account
username = chrome.find_element_by_id('tbUserName')
username.send_keys(ren_user)

password = chrome.find_element_by_id('tbPassword')
password.send_keys(ren_passwd)

login = chrome.find_element_by_id('btnLogIn')
login.click()
sleep(1)

#switching to student users page
usrs = chrome.find_element_by_id('app-users')
usrs.click()
sleep(1)

view = chrome.find_element_by_id('m_lnkViewStudent')
view.click()
sleep(1)

teacher_name = ''
teacher = input('Enter the teachers name: ')
if teacher == 'amori' or teacher == 'Amori':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[6]'
    teacher_name = 'Amori'
if teacher == 'bruyneel' or teacher == 'Bruyneel':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[7]'
    teacher_name = 'Bruyneel'
if teacher == 'cortez' or teacher == 'Cortez':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[8]'
    teacher_name = 'Cortez'
if teacher == 'deanda' or teacher == 'DeAnda':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[9]'
    teacher_name = 'DeAnda'
if teacher == 'delhauer' or teacher == 'Delhauer':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[10]'
    teacher_name = 'Delahuer'
if teacher == 'griffin' or teacher == 'Griffin':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[11]'
    teacher_name = 'Griffin'
if teacher == 'herrera' or teacher == 'Herrera':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[12]'
    teacher_name = 'Herrera'
if teacher == 'king' or teacher == 'King':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[13]'
    teacher_name = 'King'
if teacher == 'johnson' or teacher == 'Johnson':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[14]'
    teacher_name = 'Johnson'
if teacher == 'melcher' or teacher == 'Melcher':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[15]'
    teacher_name = 'Melcher'
if teacher == 'mercado' or teacher == 'Mercado':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[16]'
    teacher_name = 'Mercado'
if teacher == 'mestlin' or teacher == 'Mestlin':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[17]'
    teacher_name = 'Mestlin'
if teacher == 'miller' or teacher == 'Miller':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[18]'
    teacher_name = 'Miller'
if teacher == 'morris' or teacher == 'Morris':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[19]'
    teacher_name = 'Morris'
if teacher == 'noriega' or teacher == 'Noriega':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[20]'
    teacher_name = 'Noriega'
if teacher == 'ramos' or teacher == 'Ramos':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[21]'
    teacher_name = 'Ramos'
if teacher == 'rodarte' or teacher == 'Rodarte':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[22]'
    teacher_name = 'Rodarte'
if teacher == 'zataray' or teacher == 'Zataray':
    teacher_option = '//*[@id="ctl00_cp_Content_ddlClasses"]/option[23]'
    teacher_name = 'Zataray'

#choosing teacher options to view
select = chrome.find_element_by_xpath(teacher_option)
select.click()

send = chrome.find_element_by_id('btnSearch')
send.click()

#switching to see student login information
paswrds = chrome.find_element_by_id('ctl00_cp_Content_tabPasswords')
paswrds.click()

#creating lists for student name, student username, and password
name_list = []
username_list = []
pass_list = []

#create an excel workbook object and set its sheet layout
wb = Workbook()

sheet1 = wb.add_sheet(teacher_name)
sheet1.write(0, 0 , 'Student Name')
sheet1.write(0, 1, 'Username')
sheet1.write(0, 2, 'Password')

i = 0
x = 1

def create_list(name_id, username_id, student_name):

    while i != 25:

        if x < 10:
            name_id = 'ctl00_cp_Content_rptPW_ctl0' + str(x) + '_tdStudent'
            username_id = 'ctl00_cp_Content_rptPW_ctl0' + str(x) + '_tdUserName'
            pass_id = 'ctl00_cp_Content_rptPW_ctl0' + str(x) + '_tdPW'
            create_list(name_id, username_id, student_name)

        if x >= 10:
                name_id = 'ctl00_cp_Content_rptPW_ctl' + str(x) + '_tdStudent'
                username_id = 'ctl00_cp_Content_rptPW_ctl' + str(x) + '_tdUserName'
                pass_id = 'ctl00_cp_Content_rptPW_ctl' + str(x) + '_tdPW'
                create_list(name_id, username_id, student_name)

        student_name = chrome.find_elements_by_id(name_id)
        student_username = chrome.find_elements_by_id(username_id)
        student_passwd = chrome.find_elements_by_id(pass_id)
        for j in student_name:
            name_list.append(j.text)
        for j in student_username:
            username_list.append(j.text)
        for j in student_passwd:
            pass_list.append(int(j.text))

        x += 1

        i += 1

x = 1
for j in name_list:
    sheet1.write(x, 0, j)
    x += 1
x = 1
for j in username_list:
    sheet1.write(x, 1, j)
    x += 1
x = 1
for j in pass_list:
    sheet1.write(x, 2, j)
    x += 1

wb.save('/Users/jesusmedina/Desktop/STAR2.xls')

print('Finished')