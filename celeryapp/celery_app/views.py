from .models import ApiResponse
from django.forms.models import model_to_dict
import websockets
import json
from django.http import HttpResponse
from asgiref.sync import sync_to_async


@sync_to_async
def fetch_latest_record_from_db():

    model_queryset = ApiResponse.objects.all().order_by("-created_at").first()
    model_dict = model_to_dict(model_queryset)

    return json.dumps(model_dict)


async def BroadCastLatestData(request):
    async with websockets.connect("ws://localhost:8765") as websocket:
        model_dict = await fetch_latest_record_from_db()
        await websocket.send(model_dict)
        await websocket.recv()

        return HttpResponse("Data sent : " + model_dict)
