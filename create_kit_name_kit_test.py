import sender_stand_request
import data


# Функция получения токена
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token


# Функция, изменяющая тело запроса
def get_kit_body(name):
    # из data копирование в current_body словаря с телом запроса
    current_kit_body = data.kit_body.copy()
    # изменение значения ключа на переменную name
    current_kit_body["name"] = name
    # выводится новый словарь с необходимым значением name
    return current_kit_body


# Функция позитивной проверки
def positive_assert(name):
    # сохраняется новое тело запроса в kit_body :
    kit_body = get_kit_body(name)
    # Передаётся auth_token
    auth_token = get_new_user_token()
    # сохраняется результат запроса при создании набора в kit_responce  :
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверка кода ответа = 201
    assert kit_response.status_code == 201
    # Проверка, что в наборе имя соответствует заданному
    assert kit_response.json()["name"] == name


 # Функция негативной проверки
def negative_assert_code_400(name):
    # В переменную kit_body сохраняется новое тело запроса:
    kit_body = get_kit_body(name)
    # Передаётся auth_token
    auth_token = get_new_user_token()
    # В переменную response сохраняется результат
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    #  Проверяется, что код ответа = 400
    assert kit_response.status_code == 400


# Тест 1. Допустимое количество символов
#  Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")


# Тест 2. Допустимое количество символов
#   511  символов
def test_create_kit_511_letters_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Негативный тест. Количество символов меньше допустимого (0). Параметр name не передан
def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_code_400("")


# Тест 4. Негативный тест. Количество символов больше допустимого
# 512  символов
def test_create_kit_512_letters_in_kit_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Рвзрешены английские буквы

def test_create_kit_english_letters_in_kit_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Рвзрешены русские буквы

def test_create_kit_russian_letters_in_kit_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Рвзрешены спецсимволы

def test_create_kit_special_symbols_in_kit_name_get_success_response():
    positive_assert('"№%@",')


# Тест 8. Рвзрешены пробелы

def test_create_kit_spaces_in_kit_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Рвзрешены цифры

def test_create_kit_numbers_in_kit_name_get_success_response():
    positive_assert("123")


# Тест 10. Негативный тест. Параметр не передан в запросе
def test_create_kit_empty_in_kit_name_get_error_response():
    negative_assert_code_400("")


# Тест 11. Негативный тест. Передан другой тип данных
# В параметре name number type
def test_create_kit_type_number_in_kit_name_get_error_response():
    negative_assert_code_400(123)