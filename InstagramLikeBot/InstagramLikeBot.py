from selenium import webdriver
import time


class getData():
    login = ''
    password = ''
    timing = 3
    userlogin = ''

driver = None

def instalogin():
    global driver
    driver = webdriver.Chrome('D:/chromedriver.exe')
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(getData.timing)
    driver.find_element_by_name('username').send_keys(getData.login)
    driver.find_element_by_name('password').send_keys(getData.password)
    driver.find_element_by_xpath('//button[1]').click()
    time.sleep(getData.timing)

def instaLikeUser():
    global driver
    driver.get('https://www.instagram.com/' + getData.userlogin)
    time.sleep(getData.timing)
    driver.find_element_by_xpath('//div/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//section/a/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div/div/div/div/div/div/div/a').click()
    time.sleep(1)
    while True:
        driver.find_element_by_xpath('//section/a/span').click()
        if len(driver.find_elements_by_xpath('//div/div/div/div/div/div/div/a')) == 1 : break
        driver.find_elements_by_xpath('//div/div/div/div/div/div/div/a')[1].click()
        time.sleep(1.5)

instalogin()
instaLikeUser()
time.sleep(30)
