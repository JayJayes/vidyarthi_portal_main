from django.shortcuts import render, redirect
from .models import Assignment

def teacher_assignment_upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']

        Assignment.objects.create(
            title=title,
            description=description,
            file=file
        )

        return render(request, 'frontend/Teacher_Assignment_Upload.html', {
            'success': 'असाईनमेंट यशस्वीरित्या अपलोड झाली!'
        })

    return render(request, 'frontend/Teacher_Assignment_Upload.html')
