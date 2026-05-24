from django.shortcuts import render
from .models import Alumni

def alumni_form(request):

    data = []

    if request.method == "POST":

        if 'add' in request.POST:

            Alumni.objects.create(
                name=request.POST.get('name'),
                usn=request.POST.get('usn'),
                year=request.POST.get('year'),
                company=request.POST.get('company')
            )

        elif 'search' in request.POST:

            y = request.POST.get('year')

            data = Alumni.objects.filter(year=y)

    return render(request,'alumni.html',{'data':data})