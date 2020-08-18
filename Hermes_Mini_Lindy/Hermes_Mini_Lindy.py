### Last Updated
### 4/11/2020 on Pi Zero - reduce number of emails in the morning.
### 8/18/2020 on Yoga - Fixed errors caused by Hemes Website. Next fix is to loop thru code with two differnt URL for more accuracy.

from bs4 import BeautifulSoup
import requests
import email_setup
import aws_sns_texting as txt
import datetime as dt
import mylogin as ml

today_date = dt.datetime.now()
day_of_week = today_date.isoweekday()
current_datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

#Send an email out to remind me of the program still running.
if int(dt.datetime.now().strftime("%H")) == 8 and int(dt.datetime.now().strftime("%M")) > 30:

    # Content for the email
    subject = 'Message From Mini Lindy Python - '
    body = 'Hi, \nThis is Mini Lindy. \nI am still checking for you. Stay tuned!'
    to_email_addr = ml.get_email()
    print(current_datetime)
    print( '8 - 12 Email')
    ## Send an Email Notification of Execution
    email_setup.status_email(to_email_addr, subject, body, current_datetime)

else:     
    print("\n\n")  
    print(current_datetime)
    print('continue')

### Example of a search URL that brings back result (testing purpose)
#url = 'https://www.hermes.com/us/en/search/?s=jige%20elan#||'

### Target to get results from this search URL
url = 'https://www.hermes.com/us/en/search/?s=Mini%20Lindy#||Category'
url = 'https://www.hermes.com/us/en/search/?s=lindy+mini'

### Get the html from the URL and past it into BeautifulSoup with lxml parser
source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')

## look for this tag 
# after studying the results of website url, 
# identify the tags that give us the elements that we want to monitor.
# In this case, we lookg for the search result with is under div-> class_ 
# (underscore shows that it is not a reserved word in python)


try: #Not Found Item Page in Hermes - the page with items found will not have class_= 'sub-title ng-star-inserted'
    mini_lindy_please1 = soup.find('div', class_= 'main-title').text
    mini_lindy_please2 = soup.find('div', class_= 'sub-title').text
    results = '\n' + mini_lindy_please1 + '\n' + mini_lindy_please2 + '\n'
    print('No Results . . .')
    print(results)

    msg = 'Boo... :( ' + '\n'+ 'Mini Lindy is not available ' + url

except: ##Found Item Page in Hermes
    item_list=[]
    email_message = ""
    msg = 'Hurry up! ' + '\n'+ 'Check the website, Mini Lindy is here! ' + url
    mini_lindy_please1 = soup.find('div', class_= 'main-title').text
    #mini_lindy_please2 = soup.find('h3', class_= 'product-item-name').text
    for item in soup.find_all('div', class_='product-item-meta'):
        item_info = item.text.split(',')
        item_list.append(item_info)
        print('Found Items . . .')
        print(item_info)
        print('Start Parsing . . .')
        print(item_info[2]+item_info[3])
    print(item_list)
    
    for bag in item_list:
        name = bag[0]
        color = bag[1]
        price = bag[2] + bag[3]
        
        email_message += f'Name: {name} \nColor: {color} \nPrice: {price} \n\n'

    # Setup email with all the items found.
    subject = 'Hurry!!!! Mini Lindy Available - '
    body = f'Hurry Up!... I found these:\n {url} \n\n{email_message}'
    to_leo_email_addr = ml.get_email()
    to_peg_email_addr = ml.get_peg_email()
    
    # Send an Email Notification of Execution
    email_setup.status_email(to_leo_email_addr,subject, body, current_datetime)
    email_setup.status_email(to_peg_email_addr,subject, body, current_datetime)
    
    #Send Text Messages
    #txt.send_text_leo(msg)
    #txt.send_text_peg(msg)
