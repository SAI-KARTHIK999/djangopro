from django.shortcuts import render
from .models import Alumni

def alumni_form(request):

    if request.method == "POST":

        Alumni.objects.create(
            name=request.POST.get('name'),
            usn=request.POST.get('usn'),
            year=request.POST.get('year'),
            company=request.POST.get('company')
        )
    data = Alumni.objects.filter(company = 'Amazon') 

    return render(request,'alumni.html',{'data':data})