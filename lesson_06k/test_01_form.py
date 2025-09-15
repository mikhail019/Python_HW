from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Edge()

try:
    # Переход на страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Ожидание появления элемента с именем "firstname"
    firstname_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    )

    # Ввод имени в поле
    firstname_input.send_keys("Иван")


except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие драйвера
    driver.quit()
