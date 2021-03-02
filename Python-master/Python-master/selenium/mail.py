from mailmerge import MailMerge
from datetime import date
import json
import xlrd

template = "EX1.docx"
document = MailMerge(template)

print(document.get_merge_fields())

wb = xlrd.open_workbook('/Users/jesusmedina/Downloads/Marshall/test2.xlsx')
sheet1 = wb.sheet_by_index(0)

with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    for p in data:
        document.merge(
            StudentName=data[p][0]['student_name'],
            SSID=data[p][0]['student_ssid'],
            Teacher=data[p][0]['teacher'],
            Grade=data[p][0]['student_grade'],
            StudentID=p
        )

document.write('test.docx')