from django.shortcuts import render
from .forms import HelpRequestForm
# Create your views here.
def helpreq(request):
    form = HelpRequestForm()
    return render(request, 'api/help_request.html', {'form':form})