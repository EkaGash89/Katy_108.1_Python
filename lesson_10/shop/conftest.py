"""
Конфигурационный файл pytest с общими фикстурами и настройками.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture
def driver(request):
    """
    Фикстура для создания драйвера браузера с расширенными возможностями.
    Отключает всплывающие окна сохранения паролей и другие уведомления.
    """
    with allure.step("Настройка Chrome драйвера с отключением всплывающих окон"):
        options = webdriver.ChromeOptions()
        
        # Отключаем всплывающие окна сохранения паролей
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.popups": 2,
            "profile.password_manager_leak_detection_enabled": False,
            "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": False
        })
        
        # Отключаем автоматическое сохранение паролей
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-password-generation")
        options.add_argument("--disable-password-leak-detection")
        
        # Отключаем уведомления и всплывающие окна
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        
        # Основные настройки для стабильной работы
        options.add_argument('--start-maximized')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        
        # Для запуска в headless режиме (раскомментировать при необходимости)
        # options.add_argument('--headless')
        
        # Удаляем автоматическое тестирование расширений
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        
        # Устанавливаем таймауты
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
    
    yield driver
    
    with allure.step("Завершение работы драйвера"):
        # Прикрепляем скриншот перед закрытием, если тест упал
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except:
                pass
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для получения статуса выполнения теста.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)