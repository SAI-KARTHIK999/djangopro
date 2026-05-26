from django.shortcuts import render


feedback_list = []

def feedback_page(request):
    if request.method == "POST":
        name = request.POST.get('name')
        fb = request.POST.get('feedback')

        feedback_list.append({'name': name, 'fb': fb})

    return render(request, 'feedback.html', {'data': feedback_list})