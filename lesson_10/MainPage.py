from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure

class MainPage:
    """
    Класс MainPage представляет главную страницу магазина.
    """

    def __init__(self, driver):
        """
        Инициализация класса MainPage.

        :param driver: WebDriver, экземпляр драйвера Selenium для управления браузером.
        """
        self.driver = driver

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self, product_selector: str) -> None:
        """
        Метод для добавления товара в корзину.

        Находит кнопку добавления товара по селектору и кликает по ней.

        :param product_selector: str, CSS-селектор кнопки добавления товара.
        :return: None
        """
        product_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, product_selector))
        )
        product_button.click()

    @allure.step("Покупка товаров")
    def get_shop(self) -> None:
        """
        Метод для добавления нескольких товаров в корзину и перехода к оформлению заказа.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()  # Добавление рюкзака
        self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()  # Добавление футболки
        self.driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()  # Добавление комбинезона
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()  # Переход в корзину
        self.driver.find_element(By.CSS_SELECTOR, "button#checkout").click()  # Переход к оформлению заказа
        sleep(10)  # Ожидание 10 секунд (можно заменить на более надежное ожидание)
