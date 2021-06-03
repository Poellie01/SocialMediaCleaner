# Social Media Cleaner
import requests
import os
import json
import pprint
import selenium
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from facebookChoices import *
from redditChoices import *
from instagramChoices import *
from pyfiglet import Figlet

PATH = "C:\Program Files (x86)\chromedriver.exe"


# def Install_Chromedriver(PATH):
#     chromedriver_autoinstaller.install()


def banner():
    smcbanner = Figlet(font='slant')
    print(smcbanner.renderText('Social Media Cleaner'))


def ServiceSelect():
    print("Which social media platform would you like to perform on ?")
    select = input("[1] Facebook | [2] Instagram | [3] Reddit | [4] All [1-4] ")
    if select == "1":
        print("\n[1] Delete Cookies")
        print("[2] Download all data Facebook has")
        print("[3] Strip profile")
        print("[4] Delete profile \n")
        ProfileChoice = input("What would you like to do? [1-3] ")
        if ProfileChoice == "1":
            deleteFacebookCookie()
        if ProfileChoice == "2":
            downloadFacebookData()
        if ProfileChoice == "3":
            deleteFacebookAccount()
    elif select == "2":
        print("\n[1] Delete Cookies")
        print("[2] Strip profile")
        print("[3] Delete profile \n")
        ProfileChoice = input("What would you like to do? [1-3] ")
        if ProfileChoice == "1":
            deleteInstagramCookie()
        if ProfileChoice == "2":
            downloadInstagramData()
        if ProfileChoice == "3":
            deleteInstagramAccount()
    elif select == "3":
        print("\n[1] Delete Cookies")
        print("[2] Strip profile")
        print("[3] Delete profile \n")
        ProfileChoice = input("What would you like to do? [1-3] ")
        if ProfileChoice == "1":
            deleteRedditCookie()
        if ProfileChoice == "2":
            downloadRedditData()
        if ProfileChoice == "3":
            deleteRedditAccount()
    elif select == "4":
        serivceAll()
    else:
        print("Idk what you're talking about bro")


banner()
ServiceSelect()
