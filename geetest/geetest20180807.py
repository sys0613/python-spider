# -*-coding:utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
class Crack():
    def __init__(self):
        self.url = 'http://www.geetest.com/type/';
        self.browser = webdriver.Chrome('D:/pythonlearn/python-spider/geetest/chromedriver.exe')
        self.wait = WebDriverWait(self.browser, 100)

    def open(self):
        """
        打开浏览器,并点击绑定按钮，滑动行为验证，点击登录，会出来验证码界面
        """
        self.browser.get(self.url)
        bandbutton = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/ul/li[2]/span')))
        bandbutton.click()

        slipbutton = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/div/ul/li[2]/h2')))
        slipbutton.click()

        time.sleep(3)

        loginbutton = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/div/form/a')))
        loginbutton.click()

    def crack(self):
        # 打开浏览器
        self.open()
if __name__ == '__main__':
    print('开始验证')
    crack = Crack()
    crack.crack()