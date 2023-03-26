from django.shortcuts import render, redirect
from .forms import HelpRequestForm, LocationForm
from django.contrib import messages
from .utils import send_sms
import requests, json
from .models import Location
# Create your views here.
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def helpreq(request):

    if request.method == "POST":
        form = HelpRequestForm(request.POST)
        # form1 = LocationForm(request.POST)
        
        if form.is_valid():
            data = form.save(commit=False)
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            print(latitude)
            print(longitude)

            a = Location.objects.create(user=request.user,latitude=latitude, longitude=longitude)
            a.save()
            data.save()
            # sms logic comes here
            username = request.user.username
            mobile_number = request.user.last_name
            send_sms(username, mobile_number)
            return redirect('index')
        else:
            return JsonResponse({'status': 'failure'})
        # else:
        #     print("some error occured")
    else:
        form = HelpRequestForm()
        form1 = LocationForm()

    return render(request, 'api/help_request.html', {'form':form, 'form1':form1})