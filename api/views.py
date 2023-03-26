from django.shortcuts import render, redirect
from .forms import HelpRequestForm, LocationForm,CombinedForm
from django.contrib import messages
from .utils import send_sms

def helpreq(request):   
    # form = HelpRequestForm()
    # form2 = LocationForm()
    form = CombinedForm()
    if request.method == "POST":
        form = CombinedForm(request.POST)
        # form2 = LocationForm(request.POST)
        if form.is_valid():
            
            form.save()
            # form2.save(commit=False)
            # form2.user = request.user
            # form2.save()
            
            
            # sms logic comes here
            username = request.user.username
            mobile_number = request.user.last_name
            send_sms(username, mobile_number)
            return redirect('index')
        # except Exception as e:
        #     return JsonResponse({'success': False, 'message': str(e)})
        

        

    return render(request, 'api/help_request.html', {'form':form,'user_id': request.user.id
    })