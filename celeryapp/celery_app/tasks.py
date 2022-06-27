from celery import Celery
from celery.utils.log import get_task_logger
import requests
from requests.auth import HTTPBasicAuth
from .serializers import ApiResponseSerializer

logger = get_task_logger(__name__)

app = Celery()


@app.task
def call_api():
    url = "https://api.ambeedata.com/weather/latest/by-lat-lng?lat=22.572645&lng=88.363892&filter=minutely"
    header = {
        "x-api-key": "d2f507144ddf6415c0a26410ae1e0d7671e066addb133a821f82b850bea655c5"
    }
    response = requests.get(url, headers=header)
    response_dict = response.json()["data"]

    response_serializer = ApiResponseSerializer(data=response_dict)
    if response_serializer.is_valid(raise_exception=True):
        response_serializer.save()
