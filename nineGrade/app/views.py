from django.shortcuts import render
from .models import Student

def student_form(request):

    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('name'),
            usn=request.POST.get('usn'),
            subject=request.POST.get('subject'),
            grade=request.POST.get('grade')
        )

    data = Student.objects.filter(grade='O')

    return render(request, 'student.html', {'data': data})