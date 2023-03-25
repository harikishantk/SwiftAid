from django.shortcuts import render
from .forms import HelpRequestForm, LocationForm
from django.contrib import messages
from .utils import send_sms
import requests, json
# Create your views here.
def helpreq(request):

    if request.method == "POST":
        form = HelpRequestForm(request.POST)
        form1 = LocationForm(request.POST)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            # sms logic comes here
            username = form.cleaned_data['username']
            mobile_number = form.cleaned_data['last_name']
            send_sms(username, mobile_number)
        else:
            messages.warning(request, "Some error occured")
    else:
        form = HelpRequestForm()
        form1 = LocationForm()

    return render(request, 'api/help_request.html', {'form':form, 'form1':form1})