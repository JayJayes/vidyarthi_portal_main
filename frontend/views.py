#from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import AssignmentSubmission,Assignment
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
# from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# For Student Dashboard

def signup_page(request):  # हे आता signup page ani landing page होईल
    return render(request, 'frontend/Signup_Page.html')

# def login_page(request):
#     return render(request, 'frontend/Login_Page.html')

@login_required
def main_dashboard(request):
    return render(request, 'frontend/Main_Dashboard.html')

def department_selection(request):
    return render(request, 'frontend/Department_Selection.html')

@login_required
def assignments_page(request):
    return render(request, 'frontend/Assignments_Page.html')

def query_corner(request):
    return render(request, 'frontend/Query_Corner.html')

# For Teachers Dashboard

@login_required
def teacher_dashboard(request):
    return render(request, 'frontend/Teacher_Dashboard.html')

# def teacher_assignment_management(request):
#     return render(request, 'frontend/Teacher_Assignment_Management.html')

def teacher_query_management(request):
    return render(request, 'frontend/Teacher_Query_Management.html')

def teacher_assignment_upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')

        Assignment.objects.create(
            title=title,
            description=description,
            file=file,
            uploaded_at=timezone.now()  # ✅ current date & time
        )
        messages.success(request, "Assignment uploaded successfully!")
        return redirect('teacher_dashboard')

    return render(request, 'frontend/teacher_assignment_upload.html')


@login_required
def submit_assignment(request):
    print("✅ Logged in user:", request.user.email)
    print("✅ Is Authenticated:", request.user.is_authenticated)

    submitted_assignments = AssignmentSubmission.objects.filter(user=request.user).values_list('assignment_id', flat=True)
    assignments = Assignment.objects.exclude(id__in=submitted_assignments)

    if request.method == 'POST':
        assignment_id = request.POST.get('assignment_id')
        student_name = request.POST.get('student_name')
        file = request.FILES.get('file')

        try:
            assignment = Assignment.objects.get(id=assignment_id)
            student_name = request.user.email  # ✅ Important line added

            # Double check: who is logged in
            print("🟡 Submitting Assignment:", assignment.title)
            print("🟢 request.user.email:", request.user.email)

            if AssignmentSubmission.objects.filter(user=request.user, assignment=assignment).exists():
                messages.warning(request, "You have already submitted this assignment.")
                return redirect('student_assignment_submit')

            AssignmentSubmission.objects.create(
                assignment=assignment,
                student_name=student_name,
                user=request.user,  # ✅ This must match logged in user
                file=file
            )

            messages.success(request, "Assignment submitted successfully!")
            return redirect('student_assignment_submit')
        except Assignment.DoesNotExist:
            messages.error(request, "Invalid assignment selected.")

    return render(request, 'frontend/student_assignment_submit.html', {
        'assignments': assignments
    })

def view_submissions(request):
    submissions = AssignmentSubmission.objects.all().order_by('-submitted_at')
    return render(request, 'frontend/all_assignment_submissions.html', {
        'submissions': submissions
    })
def upload_assignment(request):
    message = ""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Assignment.objects.create(title=title, description=description)
        message = "असाईनमेंट यशस्वीरित्या अपलोड झाली!"
    return render(request, 'frontend/assignment_upload.html', {'message': message})

# views.py
@login_required
def assignment_dashboard(request):
    user = request.user
    submitted_assignments = AssignmentSubmission.objects.filter(user=user).select_related('assignment').order_by('-submitted_at')
    submitted_ids = submitted_assignments.values_list('assignment_id', flat=True)
    pending_assignments = Assignment.objects.exclude(id__in=submitted_ids).order_by('-uploaded_at')

    return render(request, 'frontend/Assignment_Dashboard.html', {
        'submitted_assignments': submitted_assignments,
        'pending_assignments': pending_assignments,
    })

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)  # ✅ Session तयार करतो
            return redirect('main_dashboard')  # तुझ्या मुख्य dashboard चा path
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'frontend/Login_Page.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # जे login_view आहे तेच

@api_view(["GET"])
@permission_classes([AllowAny])
def test_cors(request):
    return JsonResponse({"message": "CORS setup working!"})
