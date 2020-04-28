import chromedriver_binary
import time
from selenium import webdriver
import re

def respon(code):
    driver = webdriver.Chrome()
    driver.get('https://atmnb.tsukuba.ac.jp/attend/tsukuba')
    time.sleep(5)
    inputBox = driver.find_elements_by_id("form-input-text")
    inputBox[0].send_keys(code)
    time.sleep(1)
    inputBox[0].submit()
    time.sleep(5)
    username = driver.find_elements_by_id("username")
    username[0].send_keys('0012020206003')
    password = driver.find_elements_by_id("password")
    password[0].send_keys('Daityan123')
    time.sleep(1)
    driver.find_element_by_name('_eventId_proceed').click()
    time.sleep(5)
    driver.find_element_by_name('insertdb').click()
    driver.quit()

respon('530645578')