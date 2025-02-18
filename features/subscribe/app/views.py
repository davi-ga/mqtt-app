from django.shortcuts import render
from features.subscribe.app.forms import SubscribeForm
from features.subscribe.services.mosquitto import MqttClient
from django.conf import settings


def subscribe_view(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            selected_options = form.cleaned_data["select_field"]
            name = form.cleaned_data["name"]
            client = MqttClient(
                broker_ip=settings.MQTT_BROKER_HOST,
                client_name=name,
                topics=selected_options,
            )
            client.start_connection()
            return render(
                request, "result.html", context={"selected_options": selected_options}
            )
    else:
        form = SubscribeForm()

    return render(request, "subscribe.html", {"form": form})
