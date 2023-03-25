from django.shortcuts import render
from .forms import HelpRequestForm
from django.contrib import messages
from utils import send_sms
# Create your views here.
def helpreq(request):

    if request.method == "POST":
        form = HelpRequestForm(request.POST)
        if form.is_valid:
            form.save()
            # sms logic comes here

        else:
            messages.warning(request, "Some error occured")
    else:
        form = HelpRequestForm()

    return render(request, 'api/help_request.html', {'form':form.as_div()})