from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shopping():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Добавление товаров в корзину
    driver.find_element(
        By.XPATH, "//div[text()='Sauce Labs Backpack']"
                  "/following-sibling::button").click()
    driver.find_element(
        By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']"
                  "/following-sibling::button").click()
    driver.find_element(
        By.XPATH, "//div[text()='Sauce Labs Onesie']"
                  "/following-sibling::button").click()

    # Переход в корзину
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    driver.find_element(By.XPATH, "//button[text()='Checkout']").click()

    # Заполнение формы
    driver.find_element(By.NAME, "firstName").send_keys("Иван")
    driver.find_element(By.NAME, "lastName").send_keys("Петров")
    driver.find_element(By.NAME, "postalCode")
