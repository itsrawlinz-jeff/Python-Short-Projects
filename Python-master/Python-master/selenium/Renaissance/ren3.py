from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
import xlsxwriter
from openpyxl import load_workbook
import getpass

#Prompt user to enter username and password, using get pass module to hide user's input for password
ren_user = 'Jmedina2'#input('Enter username: ')
ren_passwd = 'Donthackme27!' #getpass.getpass("Enter password: ")

#using to time module to get the total time it takes for the program to run
startTime = time.time()

#creating a variable that is equal to the current user
name = getpass.getuser()

#variable for holding the website url
url = "https://hosted13.renlearn.com/272178/public/rpm/login/Login.aspx?srcID=t"

# option for headless selenium chrome driver
options = Options()
chrome_path = '/Users/%s/Downloads/chromedriver' % str(name)
options.headless = True
chrome = webdriver.Chrome(executable_path=chrome_path) #, options=options)

# launching chrome with the desired url in the background
chrome.get(url)

newSite = chrome.find_element_by_id('btnGoNow')
newSite.click()
sleep(1)

# using selenium to find the username and password input element, and sending in the username and password to the input
username = chrome.find_element_by_id('Username')
username.send_keys(ren_user)

password = chrome.find_element_by_id('Password')
password.send_keys(ren_passwd)

#logging into website
login = chrome.find_element_by_id('btnLogIn')
login.click()
sleep(1)

#retrives the user of the account that was logged in
account_name = chrome.find_element_by_xpath('//*[@id="NG2_UPGRADE_0_app_c0"]/div/rl-header-ng2/div/div[3]/span[4]/rl-navitem/a/span[2]').text
print('Logged in as ' + account_name)

toggle = chrome.find_element_by_xpath('//*[@id="NG2_UPGRADE_0_app_c0"]/div/rl-header-ng2/div/div[3]/span[4]/rl-menu')
toggle.click()

# switching to student users page
usrs = chrome.find_element_by_xpath('//*[@id="NG2_UPGRADE_0_app_c0"]/div/rl-header-ng2/div/div[3]/span[4]/rl-menu/div[1]/div/rl-menuitem[2]')
usrs.click()
#sleep(1)

view = chrome.find_element_by_id('m_lnkViewStudent')
view.click()
sleep(1)

# creating lists for student name, student username, and password
name_list = []
username_list = []
pass_list = []

#using xlsx to create an excel workbook in the current user's Desktop
wb = xlsxwriter.Workbook('/Users/%s/Desktop/STAR.xlsx' % name)


def get_students(teacher_option, teacher_name):
    # choosing teacher options to view
    select = chrome.find_element_by_xpath(teacher_option)
    select.click()
    send = chrome.find_element_by_id('btnSearch')
    send.click()
    # switching to see student login information
    paswrds = chrome.find_element_by_id('ctl00_cp_Content_tabPasswords')
    paswrds.click()
    #creating a sheet in the excel workbook and calling it by the teachers' name
    sheet1 = wb.add_worksheet(teacher_name)
    
    sheet1.write(0, 0, 'Student Name')
    sheet1.write(0, 1, 'Username')
    sheet1.write(0, 2, 'Password')

    # creating lists for student name, student username, and password
    name_list = []
    username_list = []
    pass_list = []

    #variable to keep track of how many times to stay in while loop
    i = 0
    #starting number for list of students
    x = 1
    while i < 36:
        #if value of x is less than 10
        if x < 10:
            #break down the name_id, username_id, and pass_id to change the value of the elements using x 
            name_id = 'ctl00_cp_Content_rptPW_ctl0' + str(x) + '_tdStudent'
            username_id = 'ctl00_cp_Content_rptPW_ctl0' + str(x) + '_tdUserName'
            pass_id = 'ctl00_cp_Content_rptPW_ctl0' + str(x) + '_tdPW'
            student_name = chrome.find_elements_by_id(name_id)
            student_username = chrome.find_elements_by_id(username_id)
            student_passwd = chrome.find_elements_by_id(pass_id)

            #as we find the students name, username and password -> push it to the list it belongs to 
            for j in student_name:
                name_list.append(j.text)
            for j in student_username:
                username_list.append(j.text)
            for j in student_passwd:
                pass_list.append(int(j.text))

            #increment x to go to the next element id
            x += 1
        #else if x is greater than or equal to 10
        else:
            name_id = 'ctl00_cp_Content_rptPW_ctl' + str(x) + '_tdStudent'
            username_id = 'ctl00_cp_Content_rptPW_ctl' + str(x) + '_tdUserName'
            pass_id = 'ctl00_cp_Content_rptPW_ctl' + str(x) + '_tdPW'
            student_name = chrome.find_elements_by_id(name_id)
            student_username = chrome.find_elements_by_id(username_id)
            student_passwd = chrome.find_elements_by_id(pass_id)

            #as we find the students name, username and password -> push it to the list it belongs to
            for j in student_name:
                name_list.append(j.text)
            for j in student_username:
                username_list.append(j.text)
            for j in student_passwd:
                pass_list.append(int(j.text))

            #increment x to go to the next element id
            x += 1
        #increment i to go to the next student
        i += 1

    #loop into the name, username and password list -> export the data from the list into the sheet in its column
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
    print(teacher_name + '-> DONE')

#create an empty list of teachers and a list that holds all teachers name
teachers = []
teachers_name = ['Amori', 'Bruyneel', 'Cortez', 'DeAnda', 'Delhauer', 'Griffin', 'Herrera', 
'King', 'Johnson', 'Melcher', 'Mercado', 'Mestlin', 'Miller', 'Morris', 'Noriega', 'Ramos', 'Rodarte', 'Zataray']

#starting option value for teachers
x = 6
#append incremeneted option value into the teacher list 
for i in range(len(teachers_name)):
    teachers.append('//*[@id="ctl00_cp_Content_ddlClasses"]/option[' + str(x) + ']')
    x += 1

#loop through teachers and teacher name list and call the get_students function to create workbook that contains all teacher's sheet
#with all student information
for i, j in zip(teachers, teachers_name):
    get_students(teacher_option=i, teacher_name=j)

#close excel workbook
wb.close()

#stop the stop watch
endTime = time.time()
chrome.close()
#gets the overall time it took to run and changes the value to an integer
overallTime = int(endTime - startTime)

print('Finished, Program took %s seconds.' % overallTime)
