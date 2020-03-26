import os

def get_email(): 
    return os.environ.get('GMAIL')

def get_peg_email(): 
    return os.environ.get('PEG_GMAIL')

def get_authpw():
    return os.environ.get('GMAIL_SMTP_AUTH_PW')

def get_my_phone(): 
    return os.environ.get('MY_PHONE_NUM')

def get_peg_phone():
    return os.environ.get('PEG_PHONE_NUM')


#
# print(get_my_phone())
#print(get_email())


