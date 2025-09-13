from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввод значения
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
    driver.find_element(By.XPATH, "//button[text()='7']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='8']").click()
    driver.find_element(By.XPATH, "//button[text()='='']").click()

    # Ожидание результата
    result = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )
    assert result.text == "15"

    driver.quit()
