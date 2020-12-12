import requests  # Used to go to website
from bs4 import BeautifulSoup  # Used to breakdown HTML code
# Stores username and password to login to the facebook page
from login import username, password
import selenium
import os
from events import eventList as events
from datetime import date
import os.path
from os import path
from functions import heading, ur_l, date as day, Event_Details as details
import bs4


today = date.today()
eventListDate = today.strftime("%b-%d-%Y")

# This object contains the login information imported from another class
payload = {
    'email': username,
    'pass': password
}

# Specifies the name of the website we are targetting
POST_LOGIN_URL = "https://www.facebook.com"

if (os.path.isfile(eventListDate + '.txt') is False):
    eventsFile = open(eventListDate + '.txt', 'a')
else:
    print(eventListDate + '.txt already exists!')
    eventsFile = open(eventListDate + '.txt', 'w')

os.chdir('Events')


for event in events:
    with requests.Session() as session:
        post = session.post(POST_LOGIN_URL, data=payload)
        page = requests.get(event)
    print(event, page)
    # Verify that page has been stripped
    # print(page.content)

    # Variable that holds the HTML version of the page
    eventPage = bs4.BeautifulSoup(page.text, "lxml")
    data = eventPage.findAll("div", class_= "hidden_elem")
    
    # print(eventPage.prettify()) #easier to read HTMl version

    # Event Name
    eventName = heading(eventPage)
    fileName = eventName

    if (os.path.isfile(fileName + '.txt') is False):
        print("Creating New File")

        sourceFile = open(fileName+'.txt', 'w')
        print("Event Name: " + eventName, file=sourceFile)

    
        # Event Image URL
        print("Event Image URL: " + ur_l(eventPage), file=sourceFile)

        print(eventName + '.txt', file=eventsFile)
        sourceFile.close()

    else:
        print("This Event Already Exists!")
eventsFile.close()
os.chdir('../')
