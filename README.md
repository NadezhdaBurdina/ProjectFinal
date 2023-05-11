# ProjectFinal
Тестирование интерфейса авторизации в личном кабинете  Ростелеком Информационные Технологии 
Объект тестирования: https://b2c.passport.rt.ru
Тест - кейсы и баг репорты доступны по ссылке https://docs.google.com/spreadsheets/d/12gY4gbWwMpLAWTHAnC7ErufBYbFGcoAyzOfC5InpaKk/edit?usp=sharing
Для запуска тестов необходимо:
а)установить библиотеки pytest, selenium
б) в файле settings.py изменить значение переменных LOGIN, PASSWORD, EMAIL на валидные
В папке tests находятся файлы:
а) test_auth.py - проверка внешнего вида главной страницы, авторизаций
б) test_regis.py - проверка регистраций
в) test_tab.py - проверка работы переходов и автопереходов, страницы восстановления пароля
В корне проекта находятся файлы:
г)conftest.py - файл с фикстурами
д)locators.pt - используемые локаторы
у)settings.py - файл с данными для ввода 
! Некоторые тесты могут работать некорректно из-за наличия капчи на сайте
Проект содержит позитивные и негативные тесты
Тесты отмечены кодами совпадающими с тест-кейсами
