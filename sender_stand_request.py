import configuration
import requests
import data



# создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)



def get_auth_token():
    auth_token = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.headers).json()["Authorization"]
    return auth_token



# создание нового набора
def post_new_client_kit(kit_body, auth_token):
    auth_headers = data.headers.copy()
    auth_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=auth_headers)
