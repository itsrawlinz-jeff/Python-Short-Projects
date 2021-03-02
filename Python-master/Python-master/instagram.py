from instapy_cli import client
import random
import time
import getpass
from passwords import image 

username = input('Enter username: ')
password = getpass.getpass('Enter password: ')

caption = input('Enter a caption: ')

with client(username, password) as cli:
    cli.upload(image, caption)

print('Post has been uploaded')
