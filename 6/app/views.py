from django.shortcuts import render
from .models import Student

# Form page
def student_form(request):
    if request.method == "POST":
        Student.objects.create(
            usn=request.POST.get('usn'),
            name=request.POST.get('name'),
            subject=request.POST.get('subject'),
            cie=request.POST.get('cie')
        )
    return render(request, 'form.html')

# Display page
def low_cie_students(request):
    students = Student.objects.filter(cie__lt=20)
    return render(request, 'display.html', {'data': students})