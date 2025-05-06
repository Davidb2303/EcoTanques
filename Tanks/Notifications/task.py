from celery import shared_task
import requests

@shared_task
def enviar_notificacion_whatsapp(mensaje, telefono):
    url = "https://tu-api-de-whatsapp.com/send"
    data = {
        "phone": telefono,
        "message": mensaje
    }
    response = requests.post(url, json=data)
    return response.status_code
