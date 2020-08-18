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

Setup User Evironment Variables:
-- 'GMAIL'
-- 'PEG_GMAIL'
-- 'GMAIL_SMTP_AUTH_PW'
-- 'MY_PHONE_NUM'
-- 'PEG_PHONE_NUM'

On windows, go to search for "View Advanced Systems Setting" >> Click on the "Environment Variable" button to setup the variables.

On linux, create script to export user variables. 
1) Go to pi@raspi0:/etc/profile.d
2) Create the file with the following as my_env_var.sh:

        export GMAIL="[Your Email]"
        export PEG_GMAIL="[Peg Email"
        export GMAIL_SMTP_AUTH_PW="[GMAIL AUTH Access Key]"
        export MY_PHONE_NUM="[+1[Phone Numbber]]"
        export PEG_PHONE_NUM="[+1[Phone Numbber]]"
        

Scheduling the Tasks
On Windows,
    Search for "Task Scheduler".
    1) Create Task ...
    2) Go to Action Tab Enter: 
        Program/Script (Python Location) : C:\Users\leohu\AppData\Local\Programs\Python\Python37-32\python.exe
        Add Argument (Script Name): Hermes_Mini_Lindy.py
        Start In (Script Location): C:\Users\leohu\Desktop\Python\GitHub\Python_Project\Project_2_Hermes_Mini_Lindy
    3) Create the desired time for triggering from the "Tiggers" Tab


On Linux,
    1)Setup Cron Job, type crontab -e, 
    1.1) use nano, if asked.
    2)Enter the following:
    
      # m h  dom mon dow   command
      0 8-14/2 * * * . $HOME/.profile; /usr/bin/python3 /home/pi/Documents/Finding_Hermes/Hermes_Mini_Lindy/Hermes_Mini_Lindy.py >> ~/cr$
      */15 14-22 * * * . $HOME/.profile;  /usr/bin/python3 /home/pi/Documents/Finding_Hermes/Hermes_Mini_Lindy/Hermes_Mini_Lindy.py >> ~$
    3) Save the crontab 


  
