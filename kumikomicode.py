import chromedriver_binary
import time
from selenium import webdriver
import re
import respon

driver = webdriver.Chrome()

while True:
    driver.get('https://wall.sli.do/event/qzahwoxu?section=e161f411-c5b3-4b06-a3f0-94c82133ee51')
    time.sleep(5)
    texts = driver.find_elements_by_tag_name("fit-text")
    num = None
    for t in texts:
        num = re.match(r'[0-9]{9}', t.text)
        if num: # 数字9桁で構成される文字列が見つかった場合
            print(num)
            respon(num)
            break

    time.sleep(60)
    if num:
        break

driver.quit()