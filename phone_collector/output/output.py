import requests
import json


URL = "https://s1-nova.ru/app/private_test_python/"


def send_result(phone: str, login: str) -> None:
    """Функция вывода, отправляет post-запрос с данными в нужный сервис."""
    result = {"phone": phone, "login": login}
    result = json.dumps(result)
    requests.post(
        URL, headers={"Content-Type": "application/json"}, data=result
    )
