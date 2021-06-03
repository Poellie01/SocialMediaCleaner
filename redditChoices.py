# import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"


def deleteRedditCookie():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
    acceptCookie(driver)


def deleteRedditAccount():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
    acceptCookie(driver)


def acceptCookie(driver):
    driver.get("https://www.reddit.com/login")

    username = os.getenv("FBUSER")
    password = os.getenv("FBPASS")

    driver.execute_script(
        f'var element = document.getElementById("loginUsername"); element.value = "{username}";')
    driver.execute_script(
        f'var element = document.getElementById("loginPassword"); element.value = "{password}";')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@data-testid="cookie-policy-dialog-accept-button"]'))).click()
    driver.find_element_by_class(
        "AnimatedForm__submitButton m-full-width").click()


def downloadRedditData():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)
    acceptCookie(driver)
