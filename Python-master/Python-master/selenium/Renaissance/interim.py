import xlsxwriter
import xlrd
import mysql.connector
import csv
from passwords import local_user, local_pass, elpac_file, interim_file, new_file

#read from existing excel files to export information to new file
wb = xlrd.open_workbook(interim_file)
wb1 = xlrd.open_workbook(elpac_file)
sheet1 = wb.sheet_by_index(0)
sht = wb1.sheet_by_index(0)

#create file that we will putting information to
wb2 = xlsxwriter.Workbook(new_file)
sheet2 = wb2.add_worksheet('INTERIM')


database = 'caaspp'
db = mysql.connector.connect(
    host="localhost",
    user=local_user,
    passwd=local_pass,
    auth_plugin="mysql_native_password"
)
cur = db.cursor(buffered=True)
cur.execute("CREATE DATABASE IF NOT EXISTS %s;" % database)
db.commit()

cur.execute("USE %s;" % database)
print("DATABASE %s CREATED" % database.upper())

db_table = "students"
cur.execute('CREATE TABLE IF NOT EXISTS '  + db_table +
    '('
        'GROUP_NAME VARCHAR(30) NOT NULL, '
        'SCHOOL_NATURAL_ID VARCHAR(30) NOT NULL, '
        'SCHOOL_YEAR VARCHAR(4) NOT NULL, '
        'SUBJECT_CODE VARCHAR(5) NOT NULL, '
        'STUDENT_NAME VARCHAR(45) NOT NULL, '
        'STUDENT_SSID VARCHAR(15) NOT NULL PRIMARY KEY, '
        'GROUP_USER_LOGIN VARCHAR(40) NOT NULL'
    ');'
)

print("\n\nTABLE %s CREATED IN %s" % (db_table.upper(), database.upper()))

cur.execute("\n\nDESCRIBE %s" % db_table)
for p in cur:
    print(p)

#set the width of the columns
sheet2.set_column('A:A', 27)
sheet2.set_column('B:B', 17)
sheet2.set_column('C:C', 10)
sheet2.set_column('D:D', 28)
sheet2.set_column('E:E', 13)
sheet2.set_column('F:F', 15)

#Write Column Names
sheet2.write(0, 0, "group_name")
sheet2.write(0, 1, "school_natural_id")
sheet2.write(0, 2, "school_year")
sheet2.write(0, 3, "subject_code")
sheet2.write(0, 4, "student_name")
sheet2.write(0, 5, "student_ssid")
sheet2.write(0, 6, "group_user_login")

#retrieve school code from elpac file
school_code = int(sht.cell_value(1, 2))

#start for loop that will end until reaches end of number of rows in ELPAC file
for i in range (1, sheet1.nrows):
    school = sheet1.cell_value(i, 0)
    student_id = int(sheet1.cell_value(i, 1))
    student_name = sheet1.cell_value(i, 2)
    ssid = int(sheet1.cell_value(i, 3))
    teacher = sheet1.cell_value(i, 4)
    splitting = teacher.split(',')
    teacher = splitting[0]
    school_year = "2020"
    subject = "ALL"
    
    query = """INSERT INTO students (GROUP_NAME, SCHOOL_NATURAL_ID, SCHOOL_YEAR,
                   SUBJECT_CODE, STUDENT_NAME, STUDENT_SSID, GROUP_USER_LOGIN)
                   VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    values = (teacher, str(school_code), school_year, subject, 
                student_name, str(ssid), 'NULL')
    cur.execute(query, values)
    
    sheet2.write(i, 0, teacher)
    sheet2.write(i, 1, str(school_code))
    sheet2.write(i, 2, school_year)
    sheet2.write(i, 3, subject)
    sheet2.write(i, 4, student_name)
    sheet2.write(i, 5, str(ssid))
    #sheet2.write(i, 6, email)

cur.close()
db.commit()
wb2.close()