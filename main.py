import requests
from bs4 import BeautifulSoup
from events import eventList, mobileList
from login import username, password
import bs4
from functions import heading, ur_l

payload = {
    'email': username,
    'pass': password
}

POST_LOGIN_URL = "https://www.facebook.com"

for event in eventList:

    with requests.Session() as session:
        post = session.post(POST_LOGIN_URL, data=payload)
        page = requests.get(event)
    eventPage = bs4.BeautifulSoup(page.text, "lxml")
    data = eventPage.findAll("div", class_= "hidden_elem")
    eventName = heading(eventPage)
    eventImage = ur_l(eventPage)
    print(eventName)
    #print(eventImage)

for event in mobileList:
    print(event)
    with requests.Session() as session:
        posts = session.post(POST_LOGIN_URL, data=payload)
        pages = requests.get(event)

    
    eventPage = bs4.BeautifulSoup(pages.text, "lxml")
    print(eventPage.prettify()) #easier to read HTMl version
    


    desc = eventPage.find(class_='dx cm')
    print(desc.text)
    