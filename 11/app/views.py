from django.shortcuts import render
from .models import Faculty
# Create your views here.
def faculty_form(request):
    if request.method=="POST":
        Faculty.objects.create(
            fid=request.POST.get('fid'),
            title=request.POST.get('title'),
            name=request.POST.get('name'),
            branch=request.POST.get('branch')
        )
    data = Faculty.objects.filter(branch='CSE',title='Professor')
    return render(request,'faculty.html',{'data':data})
    
