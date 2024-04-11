from django.shortcuts import render

# Create your views here.



def UserDashboard(request):
    return render(request,'bases/dashboardbase.html')
