# import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"


def deleteInstagramCookie():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
    acceptCookie(driver)


def deleteInstagramAccount():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
    acceptCookie(driver)


def acceptCookie(driver):
    driver.get("https://www.instagram.com")

    username = os.getenv("FBUSER")
    password = os.getenv("FBPASS")

    driver.execute_script(
        f'var element = document.getElementByName("username"); element.value = "{username}";')
    driver.execute_script(
        f'var element = document.getElementByName("password"); element.value = "{password}";')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@data-testid="cookie-policy-dialog-accept-button"]'))).click()
    driver.find_element_by_class("sqdOP  L3NKy   y3zKF     ").click()


def downloadInstagramData():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
    acceptCookie(driver)
