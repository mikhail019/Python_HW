import pytest
from selenium import webdriver
from lesson_10.CalcPage import CalcPage
from time import sleep
import allure

@pytest.fixture
def driver():
    """
    Фикстура для инициализации веб-драйвера.

    Returns:
        webdriver: Экземпляр веб-драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Тестирование калькулятора")
@allure.description("Проверка функциональности калькулятора с использованием Selenium и Allure.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calc(driver):
    """
    Тест для проверки функциональности калькулятора.

    Args:
        driver (webdriver): Экземпляр веб-драйвера.

    Returns:
        None
    """
    with allure.step("Открытие страницы калькулятора"):
        calc_page = CalcPage(driver)
        calc_page.open()

    with allure.step("Выполнение расчета"):
        calc_page.do_calc()

    sleep(5)

    with allure.step("Прокрутка страницы вниз"):
        calc_page.scroll_down()

    with allure.step("Выполнение арифметической операции"):
        calc_page.perform_element()

    sleep(5)
