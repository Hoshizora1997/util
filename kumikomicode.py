import chromedriver_binary
import time
from selenium import webdriver
import re
import datetime

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

driver = webdriver.Chrome()

while True:
    driver.get('https://wall.sli.do/event/qzahwoxu?section=e161f411-c5b3-4b06-a3f0-94c82133ee51')
    time.sleep(5)
    texts = driver.find_elements_by_tag_name("fit-text")
    num = None
    for t in texts:
        num = re.match(r'[0-9]{9}', t.text)
        if num: # 数字9桁で構成される文字列が見つかった場合
            print(str(datetime.datetime.now()) + '出席コードが見つかりました。出席番号:' + num.group())
            respon(num.group())
            print(str(datetime.datetime.now()) + '出席処理を実施しました')
            break
    if num:
        break
    else:
        print(str(datetime.datetime.now()) + '出席コードが見つかりませんでした。60秒後に再確認します。')
    time.sleep(60)

driver.quit()