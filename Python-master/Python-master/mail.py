import time, datetime
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imapclient
import pprint

def send_mail(email, passwd):

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()

    gmail.login(email, str(passwd))

    recipient = 'alexm276@yahoo.com'
    subject = 'Python SMTP Test'
    message = 'This is a test email sent using the smtp module which is connected to google server'

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()

    gmail.sendmail(email, recipient, text)

    gmail.quit()

email = input('Enter email: ')
passwd = getpass.getpass('Enter password: ')

startTime = datetime.datetime(2019, 10, 29, 18, 24, 0)

while datetime.datetime.now() < startTime:
    time.sleep(1)

send_mail(email, passwd)

date = datetime.datetime.now()
exaxct = date.strftime('%B %d on %I:%M %p')
print('Email Sent on ' + exaxct)


############### IMAP ###############
#imap_gmail = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#imap_gmail.login(email, passwd)
#imap_gmail.select_folder('INBOX',readonly=True)

#UID = imap_gmail.gmail_search('New form Submission')
#print(UID)
#emails = imap_gmail.fetch([1964], ['BODY[]'])

#pprint.pprint(emails)

#imap_gmail.logout()
