# Phone collector

## Description

Django app that gets phone number from telegram bot and sends data to another service. Application uses webhooks. After the first message the bot will ask you to take your phone number.

## Getting Started

### Dependencies

* python 3.7
* django 4.0.4

### Installing

Clone repository and register a telegram bot by using BotFather.

Make your own venv:

```bash
python3 -m venv venv
```

Install requirements:

```bash
pip install -r requirements.txt
```

Don't forget to create  your .env file in settings.py dirrectory and save there SECRET_KEY and BOT_TOKEN.

Make migrations:

```bash
python manage.py migrate
```

### Executing program

Run the server:

```bash
python manage.py runserver
```
