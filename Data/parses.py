from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
import gspread
from selenium.webdriver.chrome.options import Options
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from bs4 import BeautifulSoup
from math import ceil
import numpy as np
import pygsheets
import time
from selenium.webdriver.common.action_chains import ActionChains

def parsedata():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\newsite\\CraftDay\\supervisorparse\\User Data\\")
    driver = webdriver.Chrome(executable_path=r'C:/newsite/CraftDay/supervisorparse/chromedriver.exe', chrome_options=options)


    try:
        driver.get("https://supervisor.pallas-ludens.com/")
        username = driver.find_element_by_id("username")
        username.send_keys("MDY_mykola_ustymenko")
        password1 = driver.find_element_by_id("password")
        password1.send_keys("Unf0684px2!")
        butlog = driver.find_element_by_id("kc-login")
        butlog.click()
    except Exception:
        print("ok")


    driver.get("https://docs.google.com/spreadsheets/d/1Ws84at7ztvpZtifs1xVXxK4Lr_bYHH_szhSkdNbiLoo/edit#gid=0")

    time.sleep(4)

    sheet = driver.find_element_by_class_name("fixed4-inner-container")
    sheet.click()

    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    return print("ready")