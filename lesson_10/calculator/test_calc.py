import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from calc_page import CalculatorPage
from typing import Any
import allure


@pytest.fixture
def driver() -> Any:
    """
    Фикстура для создания и завершения работы веб-драйвера.
    Yields:
        WebDriver: Экземпляр веб-драйвера Chrome
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver  # Возвращаем драйвер тесту
    driver.quit()

@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест сложения с задержкой")
@allure.description("Проверка работы калькулятора с задержкой вычисления 45 секунд")
def test_calculator_with_delay(driver: WebDriver) -> None:
    """
    Тест проверяет корректность работы калькулятора с установленной задержкой.
    Шаги:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Выполнить вычисление 7 + 8
    4. Дождаться результата
    5. Проверить, что результат равен 15
    Args:
        driver: Фикстура WebDriver
    Returns:
        None
    """
    with allure.step("Инициализация страницы калькулятора"):
        calculator = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator.open()

    with allure.step("Установить задержку 45 секунд"):
        calculator.set_delay(45)

    with allure.step("Выполнить вычисление 7 + 8"):
        calculator.enter_calculation(7, '+', 8)

    with allure.step("Ожидать завершения вычисления"):
        result = calculator.wait_for_calculation_to_complete()

    with allure.step("Проверить результат вычисления"):
        allure.attach(
            f"Ожидаемый результат: '15', Фактический результат: '{result}'",
            name="Результат проверки",
            attachment_type=allure.attachment_type.TEXT
        )
        assert result == '15', f"Ожидался результат '15', но получен '{result}'"