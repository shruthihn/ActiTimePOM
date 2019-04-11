from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

def test_launchbrowser():
    global driver
    driver = webdriver.Chrome();
    driver.get('http://localhost/login.do#page-1');
    driver.maximize_window();
    driver.implicitly_wait(30)

def test_login():
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('pwd').send_keys('manager')
    driver.find_element_by_xpath('//*[@id="loginButton"]').click()
    time.sleep(10)

def logout():
    pass


    # driver.find_element_by_xpath('//*[text()="USERS"]').click()
    # driver.find_element_by_xpath('//*[text()="Add User"]').click()
    # driver.find_element_by_name('firstName').send_keys('check')
    # driver.find_element_by_name('lastName').send_keys('test')
    # driver.find_element_by_name('email').send_keys('test@gmail.com')
    # driver.find_element_by_name('username').send_keys('test')
    # driver.find_element_by_name('password').send_keys('test123')
    # driver.find_element_by_name('passwordCopy').send_keys('test123')
    # Time_zone=driver.find_element_by_xpath('//*[@id="ext-gen145"]/td[2]').click()
    # Time_zone1=Select(Time_zone)
    # Time_zone1.select_by_visible_text('London Office')






