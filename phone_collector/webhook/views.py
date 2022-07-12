from phone_collector.settings import BOT_TOKEN
from output.output import send_result
from django.views import View
from django.http import JsonResponse
from .models import Chat
import requests
import json


class WebhookView(View):
    """Класс webhook в которов организовано взаимодействие с ботом."""

    def post(self, request) -> JsonResponse:
        data = json.loads(request.body)
        if data.get("message"):
            if data.get("message").get("contact"):
                login = data.get("message").get("from").get("username")
                phone = data.get("message").get("contact").get("phone_number")
                send_result(phone, login)
                return JsonResponse({200: "OK"})
            if (
                len(
                    Chat.objects.filter(
                        chat_id=int(data.get("message").get("chat").get("id"))
                    )
                )
                == 1
            ):
                return JsonResponse({200: "OK"})
            chat_id = int(data.get("message").get("chat").get("id"))
            Chat.objects.create(chat_id=chat_id)
            requests.post(
                url="https://api.telegram.org/bot{0}/{1}".format(
                    BOT_TOKEN, "sendMessage"
                ),
                data=json_construct(chat_id),
            ).json()
            return JsonResponse({201: "Created"})
        else:
            return JsonResponse({200: "OK"})


def json_construct(chat_id: int) -> dict:
    keyboard = {
        "one_time_keyboard": True,
        "keyboard": [
            [
                {
                    "text": "дать",
                    "request_contact": True,
                }
            ]
        ],
    }
    body = {
        "chat_id": chat_id,
        "text": "Привет, а дай номер",
        "reply_markup": json.dumps(keyboard),
    }
    return body
