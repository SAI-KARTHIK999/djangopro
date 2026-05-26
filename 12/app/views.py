from django.shortcuts import render
from .models import Student

def student_form(request):

    if request.method == "POST":

        if 'add' in request.POST:

            Student.objects.create(
                name=request.POST.get('name'),
                usn=request.POST.get('usn'),
                department=request.POST.get('department'),
                grade=request.POST.get('grade')
            )

        elif 'update' in request.POST:

            Student.objects.filter(
                name=request.POST.get('name')
            ).update(
                grade=request.POST.get('grade')
            )

    data = Student.objects.all()

    return render(request,'student.html',{'data':data})