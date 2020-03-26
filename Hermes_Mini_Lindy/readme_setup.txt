Pip3 the following module:
   pip3 install requests
   pip3 install lxml
   pip3 install html5lib
   pip3 install BeautifulSoup4
   Pip3 install boto3

 Setup User from AWS Console:
 1) Add a new user here https://console.aws.amazon.com/iam/home#/users
 2) Create user with Access type = Programmatic access  
 3) Attach Existing Policies Directly
 4) AmazonSNSFullAccess
 5) Create User
 6) Download CSV - record Access Keys

 Install AWS CLI (Comand Line Interface)
 1) Follow instruction here: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
 2) In CMD or Terminal type: aws configure (if error, close cmd and reopen cmd to try again)
 3) enter Access key ID, Secret access key, Region Name = us-east-1, Output format = json
 
 On Raspberry Pi Terminal:
 1) pip3 install awscli --upgrade --user
 2) export PATH=/home/pi/.local/bin:$PATH
 3) confirm using: aws --version
 4) In CMD or Terminal type: aws configure (if error, close cmd and reopen cmd to try again)
 5) enter Access key ID, Secret access key, Region Name = us-east-1, Output format = json

Setup User Evironment Variables
-- 'GMAIL'
-- 'PEG_GMAIL'
-- 'GMAIL_SMTP_AUTH_PW'
-- 'MY_PHONE_NUM'
-- 'PEG_PHONE_NUM'
