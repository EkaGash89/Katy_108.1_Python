# Проект автоматизации тестирования Saucedemo

## Описание проекта

Автоматизированные тесты для интернет-магазина [Saucedemo](https://www.saucedemo.com/). 
Проект реализует Page Object Model паттерн и включает тестирование полного цикла покупки товара.

## Технологии

- Python 3.11+
- pytest
- Selenium WebDriver
- Allure Reporting
- WebDriver Manager

## Структура проекта
├── LoginPage.py # Класс страницы авторизации
├── InventoryPage.py # Класс страницы товаров
├── CartPage.py # Класс страницы корзины
├── CheckoutPage.py # Класс страницы оформления заказа
├── test_shop.py # Тестовые сценарии
└── README.md # Документация

## Запуск тестов

pytest - Базовый запуск всех тестов
pytest --alluredir=allure-results - Запуск с формированием Allure отчетов
pytest test_shop.py::test_saucedemo_purchase_robust - Запуск конкретного тестового файла
pytest -v --alluredir=allure-results - Запуск с подробным выводом

allure generate allure-results -o allure-report --clean - Генерация отчета из результатов
allure serve allure-results - Автоматическая генерация и открытие отчета
allure open allure-results - открыть отчет
allure generate allure-results - Генерация отчета

## Тестовые данные

Логин: standard_user
Пароль: secret_sauce
Имя: John
Фамилия: Doe
Почтовый индекс: 12345
Ожидаемая сумма: $58.29

