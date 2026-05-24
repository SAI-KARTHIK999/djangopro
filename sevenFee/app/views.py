from django.shortcuts import render
from .models import Student

def student_form(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('name'),
            usn=request.POST.get('usn'),
            semester=request.POST.get('semester'),
            fee_paid=request.POST.get('fee_paid') == 'on'
        )

    # delete students who have NOT paid fee
    Student.objects.filter(fee_paid=False).delete()

    data = Student.objects.all()

    return render(request, 'student.html', {'data': data})