import mysql.connector
import xlrd
import xlsxwriter
import pandas as pd
import getpass
import csv
from passwords import local_user, local_pass, sql_file, elpac, output_file

#file to excel file that we will read
file = elpac

#open up file
wb = xlrd.open_workbook(file)
sheet1 = wb.sheet_by_index(0)

#passwd = getpass.getpass('Enter MySQL password: ')

#name of the database we will be creating
database = 'elpac'

#connect to our mysql database
db_connection = mysql.connector.connect(
    host="localhost", 
    user=local_user, 
    passwd=local_pass,
    auth_plugin='mysql_native_password'
)


cur = db_connection.cursor(buffered=True) 
cur.execute("CREATE DATABASE IF NOT EXISTS %s;" % database)
db_connection.commit()
cur.execute("USE %s;" % database)

print('DATABASE %s CREATED' % database.upper())
student_data = "students"
cur.execute('CREATE TABLE IF NOT EXISTS ' + student_data + 
    '('
        'LEA_CDS_CODE VARCHAR(25) NOT NULL, '
        'LEA_NAME VARCHAR(30) NOT NULL, '
        'SCHOOL_CDS_NAME VARCHAR(20) NOT NULL, '
        'SCHOOL_NAME VARCHAR(20) NOT NULL, '
        'SSID VARCHAR(10) NOT NULL, '
        'F_NAME VARCHAR(20) NOT NULL, '
        'L_NAME VARCHAR(25) NOT NULL, '
        'GRADE VARCHAR(2) NOT NULL, '
        'ENTRY_DATE DATE NOT NULL, '
        'SPECIAL_ED BOOLEAN NOT NULL, '
        '504_PLAN BOOLEAN NOT NULL, '
        'START_DATE DATE NOT NULL, '
        'EXIT_DATE DATE, '
        'PRIMARY_DISABILITY_CODE VARCHAR(3), '
        'DOB DATE NOT NULL, '
        'STUDENT_ID VARCHAR(6) NOT NULL, '
        'PRIMARY_LANGUAGES VARCHAR(27) NOT NULL'
    ');'
)

print('\n\nTABLE %s CREATED\n\n' % student_data.upper())

#cur.execute("USE %s;" % database)
cur.execute('DESCRIBE %s' % student_data)
for p in cur:
    print(p)

row = 1
for i in range(1, sheet1.nrows):
    LEA_CDS_CODE = (sheet1.cell_value(row, 0))
    LEA_NAME = (sheet1.cell_value(row, 1))
    SCHOOL_CDS_NAME = (sheet1.cell_value(row, 2))
    SCHOOL_NAME = (sheet1.cell_value(row, 3))
    SSID = (sheet1.cell_value(row, 4))
    F_NAME = (sheet1.cell_value(row, 5))
    L_NAME = (sheet1.cell_value(row, 6))
    GRADE = (sheet1.cell_value(row, 7))
    if sheet1.cell_value(row, 7) == 'KN':
        GRADE = '00'
    ENTRY_DATE  = (sheet1.cell_value(row, 8))
    SPECIAL_ED = (sheet1.cell_value(row, 9))
    FIVE_PLAN = (sheet1.cell_value(row, 10))
    if SPECIAL_ED == 'Yes' or FIVE_PLAN == 'Yes':
        SPECIAL_ED = True
        FIVE_PLAN = True
    elif SPECIAL_ED == 'No' or FIVE_PLAN == 'No':
        SPECIAL_ED = False
        FIVE_PLAN = False
    START_DATE = (sheet1.cell_value(row, 11))
    EXIT_DATE = (sheet1.cell_value(row, 12))
    if EXIT_DATE == '':
        EXIT_DATE = None
    PRIMARY_DISABILITY_CODE = (sheet1.cell_value(row, 13))
    DOB = (sheet1.cell_value(row, 14))
    STUDENT_ID = int(sheet1.cell_value(row, 15))
    PRIMARY_LANGUAGES = (sheet1.cell_value(row, 16))

    query = """insert into students ( LEA_CDS_CODE, LEA_NAME, SCHOOL_CDS_NAME, SCHOOL_NAME, SSID, 
            F_NAME, L_NAME, GRADE, ENTRY_DATE, SPECIAL_ED, 504_PLAN, START_DATE, EXIT_DATE, 
            PRIMARY_DISABILITY_CODE, DOB, STUDENT_ID, PRIMARY_LANGUAGES ) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
   
    values = (LEA_CDS_CODE, LEA_NAME, SCHOOL_CDS_NAME, SCHOOL_NAME, SSID, F_NAME, L_NAME, 
            GRADE, ENTRY_DATE, SPECIAL_ED, FIVE_PLAN, START_DATE, EXIT_DATE, 
            PRIMARY_DISABILITY_CODE, DOB, str(STUDENT_ID), PRIMARY_LANGUAGES)
    
    cur.execute(query, values)
    row += 1

query = cur.execute("""select F_NAME 'FIRST NAME', L_NAME 'LAST NAME', 
            STUDENT_ID 'STUDENT #', SSID 'SSID', GRADE 'GRADE', 
            IF(special_ed, 'true', 'false') 'SPECIAL ED' from students;""")

cur.execute(query)
with open(output_file,"w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(col[0] for col in cur.description)
    for row in cur:
        writer.writerow(row)

print('\n\nQUERY COMPLETED\nPROGRAM FINISHED! GOODBYE')
cur.close()
db_connection.commit()
