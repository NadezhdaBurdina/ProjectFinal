import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
s=Service("C:\\firefoxdriver\\geckodriver.exe")
firefox_options = Options()
driver = webdriver.Firefox(service=s, options=firefox_options)



BASE_URL = 'https://b2c.passport.rt.ru'
#фикстура открытия и закрытия браузера
@pytest.fixture(scope = "session")
def driver():
    print('запуск браузера')
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver

    print('конец сессии')
    driver.quit()


@pytest.fixture(scope = "session")
def driver_regis_page():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.find_element(By.ID, 'kc-register').click()
    yield driver

    print('конец сессии')
    driver.quit()



@pytest.fixture(scope = "session")
def driver_PasRec_page():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.find_element(By.ID, 'forgot_password').click()
    yield driver

    print('конец сессии')
    driver.quit()

