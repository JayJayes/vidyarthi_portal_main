
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vidyarthi_portal.settings')
django.setup()

from frontend.models import AssignmentSubmission

AssignmentSubmission.objects.all().delete()
print("[✔] Old assignment submissions deleted.")
