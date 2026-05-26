from django.shortcuts import render

def name_form(request):
    name = ""

    if request.method == "POST":
        name = request.POST.get("name")

    return render(request, "form.html", {"name": name})