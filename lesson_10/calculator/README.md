# Проект тестирования калькулятора с задержкой

Проект содержит автоматизированные тесты для веб-калькулятора с задержкой вычислений. Тесты написаны с использованием Selenium WebDriver и Pytest, с формированием отчетов в Allure.

## Структура проекта

project/
│
├── calc_page.py          # Page Object для страницы калькулятора
├── test_calc.py          # Тесты калькулятора
├── README.md            # Документация проекта
│
├── allure-results/      # Директория с результатами тестов (создается автоматически)
└── allure-report/       # Директория с сгенерированным отчетом (создается автоматически)

## Запуск тестов

pytest - Базовый запуск всех тестов
pytest --alluredir=allure-results - Запуск с формированием Allure отчетов
pytest test_calc.py --alluredir=allure-results - Запуск конкретного тестового файла
pytest -v --alluredir=allure-results - Запуск с подробным выводом

allure generate allure-results -o allure-report --clean - Генерация отчета из результатов
allure serve allure-results - Автоматическая генерация и открытие отчета
allure open allure-results - открыть отчет
allure generate allure-results - Генерация отчета
