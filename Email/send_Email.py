import email
from email import message
from click import password_option
import pywhatkit as kit
from mailer import mailer

#email=('omarassir12@gmail.com')
#kit.send_hmail('omarassir22@gmail.com','abcdef2030','test','hello','snjk12@yahoo.com')
mail = mailer(email='omarassir22@gmail.com',password='abcdef2030',message='السلام عليكم ',subject='العنوان')