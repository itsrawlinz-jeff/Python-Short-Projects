from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import selenium.common.exceptions
from time import sleep
import time
import xlsxwriter
from openpyxl import load_workbook
import getpass
import xlrd
import json
from passwords import ren_pass, ren_user

#website url
url = "https://global-zone51.renaissance-go.com/welcomeportal/272178"

# option for headless selenium chrome driver
options = Options()
chrome_path = '/Users/jesusmedina/Downloads/chromedriver'
options.headless = True
chrome = webdriver.Chrome(executable_path=chrome_path, options=options)

#username = input('Enter your username: ')
#password = getpass.getpass('Enter your password: ')

startTime = time.time()

# launching chrome with the desired url in the background
chrome.get(url)

#redirecting to new site page 
redirect_page = chrome.find_element_by_xpath('//*[@id="NG2_UPGRADE_0_app_c0"]/div/div[1]/div/home/div/role-selector/role[2]')
redirect_page.click()

#sending in username and password to textboxes and clicking login button
username = chrome.find_element_by_id('Username')
username.send_keys(ren_user)
passwd = chrome.find_element_by_id('Password')
passwd.send_keys(ren_pass)
login = chrome.find_element_by_id('btnLogIn')
login.click()

#redirecting to users' page
find_users = chrome.get('https://global-zone51.renaissance-go.com/sismanagement/')
sleep(0.5)
users = chrome.find_element_by_xpath('/html/body/app/div/div[4]/ng-component/div/div[2]/div[1]/div[2]/div/div[1]/a')
users.click()

#opening existing excel workbook that contains student data
wb = xlrd.open_workbook('/Users/jesusmedina/Downloads/Marshall/ELPAC.xlsx')
sheet1 = wb.sheet_by_index(0)

#creating a new excel workbook which will contain all the necessary data
workbook = xlsxwriter.Workbook('/Users/jesusmedina/Downloads/Marshall/elpac_cards.xlsx')
sheet = workbook.add_worksheet('ELPAC Data')

#creating a dictionary which will contain all the students and their info
students = {}
students['students'] = []

#setting up new workbook
sheet.write(0, 0, "Student Name")
sheet.write(0, 1, "ID")
sheet.write(0, 2, "SSID")
sheet.write(0, 3, "Grade")
sheet.write(0, 4, 'Teacher')

i = 1
row = 1
#while sheet1.cell_value(i, 16) != None:
#for loop to loop through existing workbook until it reaches the end 
for j in range (1, sheet1.nrows):
    try:

        #reading the data from the existing workbook and storing it into variables: student_id, SSID, and student_name
        student_id = int(sheet1.cell_value(i, 16))
        SSID = str(sheet1.cell_value(i, 4))
        student_name = str(sheet1.cell_value(i, 6) + ', ' + sheet1.cell_value(i, 5))

        #converting student id from an int to a string
        student_id = str(student_id)
        
        #finding the search bar and clearing its content, then sending in the student id
        search = chrome.find_element_by_xpath('//*[@id="search-type"]')
        search.clear()
        search.send_keys(student_id)
        sleep(0.5)

        #if the loop reaches to 40, 60, 90, 120 then sleep for 5 seconds and print new line
        #if i == 40 or i == 60 or i == 80 or i == 100 or i == 120:
        #    sleep(5)
        #    print('')

        #click the search button 
        search_button = chrome.find_element_by_xpath('//*[@id="studentsList"]/div[2]/div/searchv2/div/div[3]/button')
        search_button.click()
        sleep(1)
    except selenium.common.exceptions.ElementClickInterceptedException:
        pass
        sleep(10)
        #click the search button 
        search_button = chrome.find_element_by_xpath('//*[@id="studentsList"]/div[2]/div/searchv2/div/div[3]/button')
        search_button.click()
        sleep(1)
        print("WAITING FOR BUTTON TO BE CLICKABLE ......")


    #grab the student grade as a string 
    grade = chrome.find_element_by_xpath('//*[@id="studentsList"]/div[3]/div/div/table/tbody/tr[1]/td[4]').text

    #grab the teacher name as a string
    teacher_name = chrome.find_element_by_xpath('//*[@id="studentsList"]/div[3]/div/div/table/tbody/tr[2]/td[6]').text
    #if the teacher is "Reclassification Candidates, then change the xpath data"
    if teacher_name == 'Reclasification Candidates':
        teacher_name = chrome.find_element_by_xpath('//*[@id="studentsList"]/div[3]/div/div/table/tbody/tr[1]/td[6]').text
    
    #modify the teacher name to just contain the teacher name and nothing else
    splitting = teacher_name.split(' -')
    teacher = splitting[0]

    #append each student into the dictionary along with its information
    students['students'].append({
        'name' : student_name,
        'student_id' : student_id,
        'student_ssid' : SSID,
        'student_grade' : grade.replace('Grade ', ''),
        'teacher' : teacher
    }
    )

    #write the student_name, student_id, SSID, grade, and teacher into the new excel workbook 
    sheet.write(row, 0, student_name)
    sheet.write(row, 1, student_id)
    sheet.write(row, 2, SSID)
    sheet.write(row, 3, str(grade.replace('Grade ', '')))
    sheet.write(row, 4, teacher)

    print(str(i) + ". " + student_name + " : " + grade.replace('Grade ', '') + " : " + teacher + " : " + student_id)
    i += 1
    row += 1

#close the workbook once done and then close chrome
workbook.close()
chrome.quit()

print('')

#create a json file and dump all information of students from the python dictionary to the json file
with open('data.json', 'w') as outfile:
    json.dump(students, outfile, indent=4)

#with open('data.json') as json_file:
#    data = json.load(json_file)
#    for p in data['students']:
#        print('Name: ' + p['name'])
#        print('ID: ' + p['student_id'])
#        print('SSID: ' + p['student_ssid'])
#        print('Grade: ' + p['student_grade'])
#        print('')

endTime = time.time()
overallTime = int((endTime - startTime)/60)
print('Finished, Program took %s minutes' % overallTime)



