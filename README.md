﻿# Тесты на проверку параметра Name набора внутри конкретного пользователя в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
- В файл `configuration.py` в переменную URL_SERVICE внесено `https://c24f0f88-8930-46b8-a526-bead6b0a8b8c.serverhub.praktikum-services.ru`
- Предварительно выполнить запрос на создание нового пользователя и запомнить токен авторизации authToken.
- Предварительно выполнить запрос на создание личного набора для этого пользователя. Обязательно передать заголовок Authorization.
- Выполнение чек-листа create_kit_name_kit_test.py   
