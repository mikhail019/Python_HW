import pytest
from selenium import webdriver
from lesson_10.IntPage import IntPage
from lesson_10.MainPage import MainPage
from lesson_10.CartPage import CartPage
from lesson_10.CheckoutPage import CheckoutPage
from time import sleep
import allure


@pytest.fixture
def driver() -> webdriver.Firefox:
    """
    Фикстура для инициализации драйвера Selenium.

    :return: webdriver.Firefox, экземпляр драйвера Firefox.
    """
    driver = webdriver.Firefox()  # Инициализация драйвера Firefox
    driver.maximize_window()  # Максимизация окна браузера
    driver.implicitly_wait(5)  # Установка неявного ожидания в 5 секунд
    driver.get("https://www.saucedemo.com/")  # Переход на страницу входа
    yield driver  # Возврат драйвера для использования в тестах
    driver.quit()  # Закрытие драйвера после завершения тестов


@allure.title("Тест страницы оформления заказа")
@allure.description("Проверка процесса оформления заказа на сайте")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_page(driver: webdriver.Firefox) -> None:
    """
    Тест для проверки процесса оформления заказа.

    :param driver: webdriver.Firefox, экземпляр драйвера Selenium.
    :return: None
    """
    int_page = IntPage(driver)

    with allure.step("Вход в систему"):
        int_page.do_int()  # Выполнение входа
    sleep(5)

    main_page = MainPage(driver)

    with allure.step("Добавление товаров в корзину"):
        main_page.get_shop()  # Добавление товаров в корзину
    sleep(5)

    cart_page = CartPage(driver)

    with allure.step("Переход в корзину и оформление заказа"):
        cart_page.shop_cart()  # Переход в корзину
    sleep(5)

    checkout_page = CheckoutPage(driver)

    with allure.step("Заполнение данных для оформления заказа"):
        checkout_page.made_cart()  # Заполнение данных для оформления заказа

    with allure.step("Проверка общей суммы заказа"):
        total_amount = checkout_page.get_total_amount()  # Получение общей суммы
        assert total_amount == 58.29, f"Ожидалось 58.29, но получено {total_amount}"  # Проверка суммы
