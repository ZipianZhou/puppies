from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.


def login(request):

    if (request.method == "GET"):
        return render(request,'login.html')
    else:
        user_set = User.objects.all()

        for u in user_set:
            if (request.POST.get('user')==u.username and request.POST.get('pwd')==u.password):
                return HttpResponse('OK')
    return HttpResponse("Not OK")

def signup(request):

    if (request.method == "GET"):
        return render(request, "signup.html")
    else:
        new_user = User(username=request.POST.get('user'), password=request.POST.get('pwd'))
        new_user.save()
        return render(request, 'login.html')