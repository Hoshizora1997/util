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
    time.sleep(60)
    driver.quit()

respon('012345678')