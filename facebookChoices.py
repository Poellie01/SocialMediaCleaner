# import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os

load_dotenv()
PATH = "C:\Program Files (x86)\chromedriver.exe"


def deleteFacebookCookie():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
    acceptCookie(driver)


def deleteFacebookAccount():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
    acceptCookie(driver)


def acceptCookie(driver):
    driver.get("https://www.facebook.com/login")

    username = os.getenv("FBUSER")
    password = os.getenv("FBPASS")

    driver.execute_script(
        f'var element = document.getElementById("email"); element.value = "{username}";')
    driver.execute_script(
        f'var element = document.getElementById("pass"); element.value = "{password}";')

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@data-testid="cookie-policy-dialog-accept-button"]'))).click()
    driver.find_element_by_id("loginbutton").click()


def downloadFacebookData():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
    acceptCookie(driver)
    time.sleep(2)
    driver.get("https://www.facebook.com/dyi/?referrer=yfi_settings")
    # time.sleep(5)
    source = driver.page_source()
    sourceSplit = source(filter("Bestand maken"))
    print(sourceSplit)
    clear_button = driver.find_element_by_link_text("Bestand maken")
    clear_button.click()
