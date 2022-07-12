from phone_collector.settings import BOT_TOKEN
from output.output import send_result
from django.views import View
from django.http import JsonResponse
import requests
import json


class WebhookView(View):
    def post(self, request):
        data = json.loads(request.body)
        message_id = data.get('message').get('message_id')
        if data.get('message').get('contact'):
            login = data.get('message').get('from').get('username')
            phone = data.get('message').get('contact').get('phone_number')
            send_result(phone, login)
            return JsonResponse({200: "OK"})
        if message_id != 320:
            return JsonResponse({200: "OK"})
        chat_id = data.get('message').get('chat').get('id')
        keyboard = {
                "one_time_keyboard": True,
                "keyboard": [
                    [
                        {
                            "text": "дать",
                            "request_contact": True,
                        }
                    ]
                ]
            }
        body = {
            "chat_id": chat_id,
            "text": "Привет, а дай номер",
            "reply_markup": json.dumps(keyboard),
        }
        requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(BOT_TOKEN, 'sendMessage'),
            data=body
        ).json()
        return JsonResponse({200: "OK"})
