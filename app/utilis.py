import random
from twilio.rest import Client
from django.conf import settings
import requests
import json
from .models import *
from django.db.models import Max


def generate_otp():
    return str(random.randint(1000, 9999))

def send_otp(mobile, otp):
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = {
        "route": "otp",
        "variables_values": otp,
        "numbers":mobile
    }

    headers = {
        "authorization": settings.FAST2SMS_API_KEY, 
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        # print(response.text)
        return response.text
    except requests.exceptions.RequestException as e:
        # print(f"Error: {e}")
        return str(e)
    


def generate_shop_number():
    max_value = Users.objects.aggregate(max_value=Max('id'))
    if max_value['max_value'] is None:
        id = 1
        shop_number = f'rcb-{id}'
    else:
        id = max_value['max_value'] + 1
        shop_number = f'rcb-{id}'

    return shop_number 
