# Проверяем уведомление о добавлении в корзину

import pytest
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = "https://avto-fes.ru/parts/AREON/LX03?source=car_freshners_catalog"
driver.get(url)

@pytest.mark.parametrize('expected_result', [('Товар добавлен в корзину')])
def test_message(expected_result):
    try:

        by_areonlux = driver.find_element(By.XPATH, '//div[1]/div[3]/div/div[2]/button')
        by_areonlux.click()
        print('by_areonlux Элемент найден')

        driver.implicitly_wait(2)
        product_to_the_cart = driver.find_element(By.CLASS_NAME, 'ui-tooltip-content')

    except Exception as err:
        print(err)
    assert product_to_the_cart.text == expected_result
    print(product_to_the_cart.text)

# Добавить товар в корзину и удалить отмеченный товар
def test_korzina():
    try:

        driver.implicitly_wait(5)
        korzina = driver.find_element(By.CLASS_NAME, 'cartLink')
        print('Заходим в корзину')
        korzina.click()
        pyautogui.screenshot('screen_korzina.png')

        driver.implicitly_wait(5)
        delete_marked = driver.find_element(By.XPATH, '//*[@id="formTrash"]/div[1]/div/div/div[1]/button[2]')
        delete_marked.click()
        print('Удалить отмеченное')

        driver.implicitly_wait(5)
        delit = driver.find_element(By.ID, 'popup_msg_ok')
        delit.click()
        print('Товар удален')

    except Exception as err:
        print(err)
