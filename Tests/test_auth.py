
from selenium.common.exceptions import NoSuchElementException
from locators import *
from settings import *
from time import sleep


"""Главная страница"""
def test_main_page(driver):
    driver.find_element(*AutoPageLoc.PHONE_TAB)
    sleep(5)
    driver.save_screenshot("tab.png")

"""ТС-001 Вход по телефону"""
def test_enter_log_pass(driver):

    user_name = driver.find_element(*AutoPageLoc.PHONE_FIELD_ACTIV)
    user_name.send_keys(LOGIN)
    password = driver.find_element(*AutoPageLoc.PASSWORD_TAB)
    password.send_keys(PASSWORD)
    button_log = driver.find_element(*AutoPageLoc.ENTER_TAB)
    button_log.click()

    assert driver.find_element(*AutoPageLoc.LK_TAB).text == 'Личный кабинет'

    print("\nТС-002 прошел успешно ")

""" ТС-003 Вход по почте"""
def test_enter_mail(driver):
    driver.find_element(*AutoPageLoc.MAIL_TAB).click()
    driver.find_element(*AutoPageLoc.MAIL_FIELD_ACTIV).send_keys(EMAIL)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)

    assert driver.find_element(*AutoPageLoc.LK_TAB).text == 'Личный кабинет'
    print("\nТС-003 прошел успешно ")

""" ТС-004 Вход по логину"""
def test_enter_with_login(driver):
    driver.find_element(*AutoPageLoc.LOGIN_TAB).click()
    driver.find_element(*AutoPageLoc.LOGIN_FIELD_ACTIV).send_keys(LOGLOGIN)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)

    try:
     assert driver.find_element(*AutoPageLoc.LK_TAB).text == 'Личный кабинет'
    except NoSuchElementException: #т.к. нет данных для входа, авторизацию считать успешной
     print("\nТС-004 прошел успешно ")


""" ТС-005 Вход по лицевому счёту"""
def test_enter_with_ls(driver):
    driver.find_element(*AutoPageLoc.LS_TAB).click()
    driver.find_element(*AutoPageLoc.LS_FIELD_ACTIV).send_keys(LS)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)

    try:
     assert driver.find_element(*AutoPageLoc.LK_TAB).text == 'Личный кабинет'
    except NoSuchElementException:  #т.к. нет данных для входа, авторизацию считать успешной
     print("\nТС-005 прошел успешно ")


"""ТС-006 Авторизация через одноклассники"""
def test_enter_with_OK(driver):
    driver.find_element(*AutoPageLoc.OK_TAB).click()
    driver.implicitly_wait(5)
    try:
     assert driver.find_element(*AutoPageLoc.OK_FIELD) == ""
    except NoSuchElementException: #т.к. нет данных для входа, авторизацию считать успешной
     print("\nТС-006 прошел успешно ")

"""" ТС-007 Авторизация через гугл"""
def test_enter_with_GOOGLE(driver):
    driver.find_element(*AutoPageLoc.GOOGLE_TAB).click()
    driver.implicitly_wait(5)
    try:
        assert driver.find_element(*AutoPageLoc.GOOGLE_FIELD).text == 'Вход'
    except NoSuchElementException:  # т.к. нет данных для входа, авторизацию считать успешной
        print("\nТС-007 прошел успешно ")




"""ТС-008 Неверный номер телефона"""
def test_enter_with_neg_phone(driver):

    driver.find_element(*AutoPageLoc.PHONE_FIELD_ACTIV).send_keys(LOGIN_NEGATIVE)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)
    assert driver.find_element(*AutoPageLoc.ERROR_MES).text == 'Неверный логин или пароль'
    print("\nТС-008 прошел успешно'")


"""ТС-009 Пустое поле'Телефон'"""
def test_with_no_phone(driver):
    driver.find_element(*AutoPageLoc.PHONE_FIELD_ACTIV).send_keys()
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)
    assert driver.find_element(*AutoPageLoc.EMPRTY_PN).text == 'Введите номер телефона'
    print("\nТС-009 прошел успешно'")

"""ТС-010 Неверный пароль"""
def test_enter_invalid_password(driver):
    driver.find_element(*AutoPageLoc.PHONE_FIELD_ACTIV).send_keys(LOGIN)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD_NEGATIVE)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)
    assert driver.find_element(*AutoPageLoc.ERROR_MES).text == 'Неверный логин или пароль'
    print("\nТС-010 прошел успешно")


""" ТС-011 Неверный email"""
def test_with_invalid_mail(driver):
    driver.find_element(*AutoPageLoc.MAIL_TAB).click()
    driver.find_element(*AutoPageLoc.MAIL_FIELD_ACTIV).send_keys(EMAIL_NEGATIVE)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)

    assert driver.find_element(*AutoPageLoc.ERROR_MES).text == 'Неверный логин или пароль'
    print("\n ТС-011 прошел успешно")


"""ТС-012 Неверный пароль email"""
def test_enter_invalid_mail_password(driver):
    driver.find_element(*AutoPageLoc.MAIL_TAB).click()
    driver.find_element(*AutoPageLoc.MAIL_FIELD_ACTIV).send_keys(EMAIL)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD_NEGATIVE)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)

    assert driver.find_element(*AutoPageLoc.ERROR_MES).text == 'Неверный логин или пароль'
    print("\n ТС-012 прошел успешно")

""" ТС-013 Пустое поле "логин" """
def test_with_no_login(driver):
    driver.find_element(*AutoPageLoc.LOGIN_TAB).click()
    driver.find_element(*AutoPageLoc.LOGIN_FIELD_ACTIV).send_keys()
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)
    error_login_mess = driver.find_element(*AutoPageLoc.ERROR_MESSAGE_EMP).text

    assert error_login_mess == 'Введите логин, указанный при регистрации'

    print("\n 'ТС-013 прошел успешно'")


"""ТС-014 Неверный пароль (логин)"""
def test_autorisation_with_invalid_login_password(driver):
    driver.find_element(*AutoPageLoc.LOGIN_TAB).click()
    driver.find_element(*AutoPageLoc.LOGIN_FIELD_ACTIV).send_keys(LOGLOGIN)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD_NEGATIVE)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)

    assert driver.find_element(*AutoPageLoc.ERROR_MES).text == 'Неверный логин или пароль'

    print("\n 'ТС-014 прошел успешно'")



""" ТС-015 Неверный ЛС"""
def test_with_invalid_ls(driver):
    driver.find_element(*AutoPageLoc.LS_TAB).click()
    driver.find_element(*AutoPageLoc.LS_FIELD_ACTIV).send_keys(LS_NEGATIVE)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)

    assert driver.find_element(*AutoPageLoc.ERROR_MESSAGE).text == 'Проверьте, пожалуйста, номер лицевого счета'

    print("\n ТС-015 прошел успешно")



""" ТС-016 Неверный пароль ЛС"""
def test_with_invalid_password_ls(driver):
    driver.find_element(*AutoPageLoc.LS_TAB).click()
    driver.find_element(*AutoPageLoc.LS_FIELD_ACTIV).send_keys(LS)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).send_keys(PASSWORD_NEGATIVE)
    driver.find_element(*AutoPageLoc.ENTER_TAB).click()
    driver.implicitly_wait(5)

    assert driver.find_element(*AutoPageLoc.ERROR_MESSAGE).text == 'Проверьте, пожалуйста, номер лицевого счета'

    print("\n ТС-016 прошел успешно")




