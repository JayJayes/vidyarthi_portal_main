from django.urls import path
from django.urls import path, include
from frontend import views as views 
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Student Dashboard
    path('', views.signup_page, name='signup'),
    #path('', views.home, name='home'),
    # path('login/', views.login_page, name='login'),
    path('department/', views.department_selection, name='department_selection'),
    path('dashboard/', views.main_dashboard, name='dashboard'),
    path('assignments/', views.assignments_page, name='assignments'),
    path('query/', views.query_corner, name='query_corner'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='frontend/Login_Page.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    


    #Teacher Dashboard
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    #path('teacher_assignment_management/', views.teacher_assignment_management, name='teacher_assignment_management'),
    path('teacher_query_management/', views.teacher_query_management, name='teacher_query_management'),
    path('teacher_assignment_upload/', views.teacher_assignment_upload, name='teacher_assignment_upload'),
    path('student_assignment_submit/', views.submit_assignment, name='student_assignment_submit'),  # ✅ New Route
    path('assignment_dashboard/', views.assignment_dashboard, name='assignment_dashboard'),
    # path('submit_assignment/', views.submit_assignment, name='submit_assignment'),
    path('view_submissions/', views.view_submissions, name='view_submissions'),
    # path('upload_assignment/', views.upload_assignment, name='upload_assignment'),

    
    path('student/dashboard/', TemplateView.as_view(template_name="frontend/Main_Dashboard.html"), name='student_dashboard'),
    path('teacher/dashboard/', TemplateView.as_view(template_name="frontend/Teacher_Dashboard.html"), name='teacher_dashboard'),
    
    # Auth endpoints via djoser
    path('api/auth/', include('djoser.urls')),         
    path('api/auth/', include('djoser.urls.authtoken')),        
    path('', include('assignments.urls')),  
]
