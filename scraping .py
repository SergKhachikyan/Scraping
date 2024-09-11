import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


user_agent = UserAgent()

options = uc.ChromeOptions()
options.add_argument(f'user-agent={user_agent.random}')

driver = uc.Chrome(options=options)

try:
    driver.get(url='https://www.list.am/')
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#dlgLangSel > div.bar > a:nth-child(1)').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#hcontent > div.stripc > div:nth-child(2) > a').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#ff > div.section.cat > div > div:nth-child(2) > a:nth-child(1)').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(4) > div > div.lsw > div.me').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(4) > div > div.lsw > div.l.top > div:nth-child(11)').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#idprice1').send_keys(10000)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > a').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(8) > div:nth-child(2) > div.r > div:nth-child(1) > div.me').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(8) > div:nth-child(2) > div.r > div:nth-child(1) > div.l.top > div:nth-child(5)').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div > div.me').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#ff > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div > div.l > div:nth-child(4)').click()
    time.sleep(3)
    price_list = []
    index = 1
    while True:
        try:
            price = driver.find_element(By.CSS_SELECTOR, f'#tp > div.dl > div > a:nth-child({index}) > div.p').text
            time.sleep(1)
            price_list.append(price)
            index += 1
        except:
            break
    
    print(price_list)

except Exception as ex:
    print(ex.__class__.__name__)
finally:
    driver.close()
    driver.quit()