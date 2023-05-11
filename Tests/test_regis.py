from locators import *
from settings import *
import pytest


"""ТС-017 Переход на страницу регистрации"""
def test_reg_page(driver):
    driver.find_element(*AutoPageLoc.REG_TAB).click()
    assert driver.find_element(*RegisPage.REG_FIELD).text == 'Регистрация'
    print("\n ТС-017 прошел успешно ")


"""ТС-018 Регистрация с валидными данными"""
def test_reg_page_registr(driver_regis_page):

    input_field = driver_regis_page.find_elements(*RegisPage.INPUT_FIELD)
    input_field[0].send_keys(NAME)
    input_field[1].send_keys(SURNAME)
    input_field[3].send_keys(EMAIL)
    input_field[4].send_keys(PASSWORD)
    input_field[5].send_keys(PASSWORD)
    driver_regis_page.find_element(*RegisPage.REGIS_BUTTON).click()

    assert driver_regis_page.find_element(*RegisPage.REGISTRATION_CODE_FIELD).text == 'Подтверждение email'
    print("\nТС-018 прошел успешно ")

"""ТС-019 Регистрация с уже зарегистрированныи email"""
def test_already_reg(driver_regis_page):

    input_field = driver_regis_page.find_elements(*RegisPage.INPUT_FIELD)
    input_field[0].send_keys(NAME)
    input_field[1].send_keys(SURNAME)
    input_field[3].send_keys(ALREADY_MAIL)
    input_field[4].send_keys(PASSWORD)
    input_field[5].send_keys(PASSWORD)
    driver_regis_page.find_element(*RegisPage.REGIS_BUTTON).click()

    assert driver_regis_page.find_element(*RegisPage.ALREADY_EXS).text == 'Войти'
    print("\n ТС-019 прошел успешно ")

"""ТС-020 Регистрация имени латиницей"""
def test_invalid_name(driver_regis_page):
    input_field = driver_regis_page.find_elements(*RegisPage.INPUT_FIELD)
    input_field[0].send_keys(INVALID_NAME)
    input_field[1].send_keys(SURNAME)
    input_field[3].send_keys(EMAIL)
    input_field[4].send_keys(PASSWORD)
    input_field[5].send_keys(PASSWORD)
    driver_regis_page.find_element(*RegisPage.REGIS_BUTTON).click()
    error_message = driver_regis_page.find_elements(*RegisPage.ERROR_MESS)
    name_error_message = error_message[0]


    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    print("\n ТС-020 прошел успешно  ")


""" ТС-021 Длина пароля менее 8 символов"""
def test_invalid_password(driver_regis_page):
    input_field = driver_regis_page.find_elements(*RegisPage.INPUT_FIELD)
    input_field[0].send_keys(NAME)
    input_field[1].send_keys(SURNAME)
    input_field[3].send_keys(EMAIL)
    input_field[4].send_keys('32147')
    input_field[5].send_keys("32147")
    driver_regis_page.find_element(*RegisPage.REGIS_BUTTON).click()
    error_message = driver_regis_page.find_elements(*RegisPage.ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Длина пароля должна быть не менее 8 символов'

    print("\n ТС-021 прошел успешно ")


"""ТС-022 Пароль с символами кириллицы"""
def test_invalid_password_kir(driver_regis_page):
    input_field = driver_regis_page.find_elements(*RegisPage.INPUT_FIELD)
    input_field[0].send_keys(NAME)
    input_field[1].send_keys(SURNAME)
    input_field[3].send_keys(EMAIL)
    input_field[4].send_keys('Я12345678')
    input_field[5].send_keys('Я12345678')
    driver_regis_page.find_element(*RegisPage.REGIS_BUTTON).click()
    error_message = driver_regis_page.find_elements(*RegisPage.ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать только латинские буквы'

    print("\n ТС-022 прошел успешно")

""" ТС-023 Пароль без буквенных символов"""
def test_invalid_password_without_letter(driver_regis_page):
    input_field = driver_regis_page.find_elements(*RegisPage.INPUT_FIELD)
    input_field[0].send_keys(NAME)
    input_field[1].send_keys(SURNAME)
    input_field[3].send_keys(EMAIL)
    input_field[4].send_keys('12345678')
    input_field[5].send_keys("12345678")
    driver_regis_page.find_element(*RegisPage.REGIS_BUTTON).click()
    error_message = driver_regis_page.find_elements(*RegisPage.ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать хотя бы одну заглавную букву'

    print("\n ТС-023 прошел успешно ")

"""ТС-024 Пароль только с заглавными буквами"""
def test_reg_page_invalid_password_low(driver_regis_page):
    input_field = driver_regis_page.find_elements(*RegisPage.INPUT_FIELD)
    input_field[0].send_keys(NAME)
    input_field[1].send_keys(SURNAME)
    input_field[3].send_keys(EMAIL)
    input_field[4].send_keys('SS12345678')
    input_field[5].send_keys("SS12345678")
    driver_regis_page.find_element(*RegisPage.REGIS_BUTTON).click()
    error_message = driver_regis_page.find_elements(*RegisPage.ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать хотя бы одну строчную букву'

    print("\n ТС-024 прошел успешно")

""" ТС-025 Пароль со строчными буквами"""
def test_invalid_password_up(driver_regis_page):
    input_field = driver_regis_page.find_elements(*RegisPage.INPUT_FIELD)
    input_field[0].send_keys(NAME)
    input_field[1].send_keys(SURNAME)
    input_field[3].send_keys(EMAIL)
    input_field[4].send_keys('ss12345678')
    input_field[5].send_keys("ss12345678")
    driver_regis_page.find_element(*RegisPage.REGIS_BUTTON).click()
    error_message = driver_regis_page.find_elements(*RegisPage.ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароль должен содержать хотя бы одну заглавную букву'

    print("\n ТС-025 прошел успешно ")

"""ТС-026 Ввод несовпадающих паролей"""
def test_invalid_password_not_same_pswr(driver_regis_page):
    input_field = driver_regis_page.find_elements(*RegisPage.INPUT_FIELD)
    input_field[0].send_keys(NAME)
    input_field[1].send_keys(SURNAME)
    input_field[3].send_keys(EMAIL)
    input_field[4].send_keys('Ss12345678')
    input_field[5].send_keys("Ss12345677")
    driver_regis_page.find_element(*RegisPage.REGIS_BUTTON).click()
    error_message = driver_regis_page.find_elements(*RegisPage.ERROR_MESS)
    password_error_message = error_message[0]

    assert password_error_message.text == 'Пароли не совпадают'

    print("\n ТС-026 прошел успешно ")



