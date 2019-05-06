from django.shortcuts import render, HttpResponse

# Create your views here.


def login(request):

    if (request.method == "GET"):
        return render(request,'login.html')
    else:
        if (request.POST.get('user')=='123' and request.POST.get('pwd')=='xyz'):
            return HttpResponse('OK')
        else:
            return HttpResponse("Not OK")