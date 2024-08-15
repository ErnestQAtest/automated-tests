from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import pyautogui

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    url = "https://avto-fes.ru"
    driver.get(url)
    yield driver

@pytest.mark.parametrize('name, password, expected_result', [('treydany@gmail.com', 'Ceckbr1975', 'https://avto-fes.ru/orders'), ('treydany', 'Ceckbr', 'https://avto-fes.ru/orders'), ('', '', 'https://avto-fes.ru/orders')])
def test_valid_data(driver, name, password, expected_result):
    try:

        driver.implicitly_wait(10)
        logInModal = driver.find_element(By.ID, 'logInModal')
        logInModal.click()

        nam = driver.find_element(By.ID, 'login')
        nam.click()
        nam.clear()
        nam.send_keys(name) #Ввели логин

        pas = driver.find_element(By.ID, 'pass')
        pas.click()
        pas.clear()
        pas.send_keys(password) #Ввели пароль

        button_login = driver.find_element(By.ID, 'go')
        button_login.click()

        logInModal = driver.find_element(By.ID, 'logInModal')
        logInModal.click()

        driver.implicitly_wait(5)
        clientName = driver.find_element(By.CLASS_NAME, 'clientName')
        clientName.click()
        pyautogui.screenshot('screen_log.png')

        if clientName:
            print(f'Вошли в аккаунт')

        logInModal = driver.find_element(By.ID, 'logInModal')
        logInModal.click()

        exet_button = driver.find_element(By.XPATH, '//div[2]/div[3]/a')
        exet_button.click()
        print('Вышли из аккаунта')

    except Exception as err:
        print(err)

    assert driver.current_url == expected_result


