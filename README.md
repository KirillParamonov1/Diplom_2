DIPLOM_2

Цель: составить автоматизированные тесты для проверки api сайта: https://stellarburgers.nomoreparties.site/

Написание тестов произведено в PyCharm с подключенными модулями Pytest, Allure, requests
Команда для запуска тестов — pytest
Команда для запуска с записью отчета в allure_results: pytest --alluredir=allure_results

Структура проекта:
* allure_results - директория с отчетами allure
* test - директория, которая содержит тесты
* conftest -фикстуры
* data - содержит url, информацию о системных сообщениях
* helpers - содержит методы для генирации данных для курьера
* burger_api - содержит базовые методы для тестирования api в тестах
* requirements - необходимые модули