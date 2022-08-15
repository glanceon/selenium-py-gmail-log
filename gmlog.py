from decouple import config
from time import sleep

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    
    config.encoding = 'cp1251'
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = uc.Chrome(options=options)
    driver.get('https://mail.google.com/')
    driver.maximize_window()

    #enter email
    email=driver.find_element(By.ID,"identifierId")
    email.send_keys(config('EMAIL'))
    sleep(3)

    #click on next button
    next=driver.find_element(By.XPATH,"(//div[@class='VmOpGe']/preceding::span[@class='VfPpkd-vQzf8d'])[2]").click()
    sleep(3)

    #enter password
    password=driver.find_element(By.XPATH,"//input[@type='password']")
    password.send_keys(config('PASS'))
    sleep(3)

    #next button
    next1=driver.find_element(By.XPATH,"(//span[@class='VfPpkd-vQzf8d'])[2]").click()
    sleep(10)

    driver.close()