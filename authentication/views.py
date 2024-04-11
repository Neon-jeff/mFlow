from django.shortcuts import render

# Create your views here.


def RegisterView(request):
    pass


def LoginView(request):
    return render(request,'pages/login.html')
    pass
