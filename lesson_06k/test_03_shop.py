from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)  # Установка времени ожидания

    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавление товаров в корзину
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Переход в корзину
        driver.find_element(
            By.XPATH, "//a[@class='shopping_cart_link']").click()
        driver.find_element(
            By.XPATH, "//button[text()='Checkout']").click()

        # Заполнение формы
        driver.find_element(
            By.ID, "firstName").send_keys("Иван")
        driver.find_element(
            By.ID, "lastName").send_keys("Петров")
        driver.find_element(
            By.ID, "postalCode").send_keys("12345")

        # Продолжение покупки
        driver.find_element(By.ID, "continue").click()

        # Завершение заказа
        wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

        # Проверка успешного оформления
        success_message = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert "THANK YOU FOR YOUR ORDER" in success_message.text.upper()

    finally:
        driver.quit()
