import numpy as np
import requests
import bs4
from collections import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from df2gspread import df2gspread as d2g
from df2gspread import gspread2df as g2d
from PIL import Image
from firebase import firebase
import pyrebase
import glob
import datetime

# ==============return event heading=================#

def heading(soup):
	heading = soup.find(class_="_5gmx")
	print(("\nEvent data fectched: " + heading.string))
	head1 = str(heading.string)
	return str(head1)


# ==========return event image url =================#

def ur_l(soup):
	tags = soup.findAll('img', class_="scaledImageFitWidth img")
	Url_1 = "\n".join(set(tag['src'] for tag in tags))
	tags = soup.findAll('img', class_="scaledImageFitHeight img")
	Url_2 = "\n".join(set(tag['src'] for tag in tags))
	if Url_1:
		return str(Url_1)
	else:
		return str(Url_2)


# ======================return event details=====================#

def Event_Details(data):
	for item in data:
		commentedHTML = item.find('code').contents[0]
		more_soup = bs4.BeautifulSoup(commentedHTML, 'lxml')
		Event_Details = more_soup.findAll('div', {'class': '_2qgs'})
		if Event_Details:
			Event = Event_Details[0].text
	return Event

# ==========return event start date =================#

def date(soup):
	date = soup.find('span', class_="_5a4z")
	date1 = date.string
	return str(date1)
