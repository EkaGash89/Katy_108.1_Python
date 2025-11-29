import pytest
from selenium import webdriver
from calc_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver  # Возвращаем драйвер тесту
    driver.quit()

def test_calculdtot(driver):
    calculator = CalculatorPage(driver)
    calculator.open()# Открыть страницу калькулятора
    calculator.set_delay(45)# Ввести значение 45 в поле задержки
    calculator.enter_calculation(7, '+', 8)# Нажать кнопки: 7, +, 8, =
    # Проверить, что в окне отобразится результат 15 через 45 секунд
    result = calculator.wait_for_calculation_to_complete()
    assert result == '15', f"Ожидался результат '15', но получен '{result}'"