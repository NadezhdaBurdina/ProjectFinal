from locators import *
from settings import *

"""ТС-027 Табы"""
def test_tab_switch(driver):
    driver.find_element(*AutoPageLoc.MAIL_TAB).click()
    assert driver.find_element(*AutoPageLoc.MAIL_FIELD).text == 'Электронная почта'
    print("\nвкладка 'Почта' активна")

    driver.find_element(*AutoPageLoc.PHONE_TAB).click()
    assert driver.find_element(*AutoPageLoc.PHONE_FIELD).text == 'Мобильный телефон'
    print("\nвкладка 'Tелефон' активна")

    driver.find_element(*AutoPageLoc.LOGIN_TAB).click()
    assert driver.find_element(*AutoPageLoc.LOGIN_FIELD).text == 'Логин'
    print("\nвкладка 'Логин' активна")

    driver.find_element(*AutoPageLoc.LS_TAB).click()
    assert driver.find_element(*AutoPageLoc.LS_FIELD).text == 'Лицевой счёт'
    print("\nвкладка 'Лицевой счёт' активна")

    print("\nТС-027 прошел успешно")

"""ТС-028 Автопереход телефон-почта"""
def test_tab_switch_phone(driver):
    driver.find_element(*AutoPageLoc.MAIL_TAB).click()
    driver.find_element(*AutoPageLoc.MAIL_FIELD_ACTIV).send_keys(LOGIN)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).click()

    assert driver.find_element(*AutoPageLoc.PHONE_FIELD).text == 'Мобильный телефон'
    print("\n ТС-028 прошел успешно ")


"""ТС-029 Автопереход с почты"""
def test_tab_switch_mail(driver):
    driver.find_element(*AutoPageLoc.PHONE_FIELD_ACTIV).send_keys(EMAIL)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).click()
    assert driver.find_element(*AutoPageLoc.MAIL_FIELD).text == 'Электронная почта'
    print("\nПереход на таб 'Почта'с таб 'Телефон' произошел ")

    driver.find_element(*AutoPageLoc.LS_TAB).click()
    driver.find_element(*AutoPageLoc.LS_FIELD_ACTIV).send_keys(EMAIL)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).click()
    assert driver.find_element(*AutoPageLoc.MAIL_FIELD).text == 'Электронная почта'
    print("\nПереход на таб 'Почта' с таб 'Лицевой счет' произошел ")

    driver.find_element(*AutoPageLoc.LOGIN_TAB).click()
    driver.find_element(*AutoPageLoc.LOGIN_FIELD_ACTIV).send_keys(EMAIL)
    driver.find_element(*AutoPageLoc.PASSWORD_TAB).click()
    assert driver.find_element(*AutoPageLoc.MAIL_FIELD).text == 'Электронная почта'
    print("\nПереход на таб 'Почта' с таб 'Логин' произошел ")
    print("\n ТС-029 прошел успешно ")



"""ТС-030 Страница восстановления пароля"""
def test_recovery(driver):
    driver.find_element(*AutoPageLoc.FORGOT_PASSWORD).click()

    assert driver.find_element(*AutoPageLoc.FOGPASSW_FIELD).text == 'Восстановление пароля'
    print("\nТС-030 прошел успешно ")

