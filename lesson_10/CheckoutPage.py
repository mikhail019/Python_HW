from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CheckoutPage:
    """
    Класс CheckoutPage представляет страницу оформления заказа.
    """

    def __init__(self, driver):
        """
        Инициализация класса CheckoutPage.

        :param driver: WebDriver, экземпляр драйвера Selenium для управления браузером.
        """
        self.driver = driver
        self.driver.implicitly_wait(15)  # Установка неявного ожидания в 15 секунд
        self.driver.maximize_window()  # Максимизация окна браузера

    @allure.step("Заполнение данных для оформления заказа")
    def made_cart(self) -> None:
        """
        Метод для заполнения данных покупателя на странице оформления заказа.

        Вводит имя, фамилию и почтовый код, затем нажимает кнопку продолжения.

        :return: None
        """
        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#first-name")
        text_input.send_keys("Марина")  # Ввод имени

        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#last-name")
        text_input.send_keys("Игамназарова")  # Ввод фамилии

        text_input = self.driver.find_element(By.CSS_SELECTOR, "input#postal-code")
        text_input.send_keys("352680")  # Ввод почтового кода

        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()  # Нажатие кнопки продолжения

    @allure.step("Получение общей суммы заказа")
    def get_total_amount(self) -> float:
        """
        Метод для получения общей суммы заказа.

        Находит элемент с общей суммой и возвращает его значение.

        :return: float, общая сумма заказа или None в случае ошибки.
        """
        try:
            total_cost = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
            ).text
            total_cost_value = float(total_cost.split("$")[1])  # Извлечение числового значения
            return total_cost_value
        except Exception as e:
            print(f"An error occurred while retrieving the total amount: {e}")
            return None
