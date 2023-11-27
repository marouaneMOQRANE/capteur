from .models import Dht11
from .serializers import DHT11serialize
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import rest_framework
#alerte
from .models import Dht11
from .serializers import DHT11serialize
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import rest_framework

import vonage
import telepot



@api_view(["GET","POST"])
def dhtser(request):
    if request.method=="GET":
        all=Dht11.objects.all()
        dataSer=DHT11serialize(all,many=True)
        return Response(dataSer.data)
    elif request.method=="POST":
        serial=DHT11serialize(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.id, status=status.HTTP_400_CREATED)

#################"




###############""



#alerte


@api_view(["GET","POST"])
def dhtser(request):
    if request.method=="GET":
        all=Dht11.objects.all()
        dataSer=DHT11serialize(all,many=True) # les donnée se form fichier
        return Response(dataSer.data)
    elif request.method=="POST":
        serial=DHT11serialize(data=request.data)
        if serial.is_valid():
            serial.save()
            derniere_temperature = Dht11.objects.last().temp
            print(derniere_temperature)
            if (int(derniere_temperature) > 30):
                subject = 'Alerte DHT'
                message = 'Il y a une alerte importante sur votre Capteur la température dépasse le seuil'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['marouane.moqrane@ump.ac.ma','yaromeaicha@gmail.com']
                send_mail(subject, message, email_from, recipient_list)
                ##############
                client = vonage.Client(key="fcda4169", secret="myA9MvW96mBVkmKF")
                responseData = client.sms.send_message(
                    {
                        "from": "vonage",
                        "to": "212654849412",
                        "text": "Il y a une alerte importante sur votre Capteur la température dépasse le seuil",
                    }
                )

                if responseData["messages"][0]["status"] == "0":
                    print("Message sent successfully.")
                else:
                    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
                    #####
                token = '6977845764:AAE1Ikldk3C8x7IO8NgBsubmC5dKjYuLVH8'
                rece_id = -4031673212
                bot = telepot.Bot(token)
                bot.sendMessage(rece_id, f'la température {derniere_temperature} depasse la normale')
                ###########

                return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.id, status=status.HTTP_400_CREATED)


# Alertwhatsapp

# Alertwhatsapp

