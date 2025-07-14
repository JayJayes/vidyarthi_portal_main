from django.contrib import admin
from .models import Assignment, AssignmentSubmission
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff')
    ordering = ('email',)
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'uploaded_at']

class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student_name', 'user', 'submitted_at']

def get_user_email(self, obj):
        return obj.user.email

get_user_email.short_description = 'User Email'

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(AssignmentSubmission, AssignmentSubmissionAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
