from django.shortcuts import render

# Create your views here.
from .models import Employee

def employee_form(request):

    if request.method == "POST":
        Employee.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            doj=request.POST.get('doj'),
            job=request.POST.get('job'),
            salary=request.POST.get('salary')
        )

    data = Employee.objects.filter(salary__gt=50000)

    return render(request, 'employee.html', {'data': data})