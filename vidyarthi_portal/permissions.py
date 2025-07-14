# permissions.py

from rest_framework import permissions

class IsTeacherOrReadOnly(permissions.BasePermission):
    """
    कस्टम परमिशन: फक्त शिक्षकांना बदल (edit) करण्याची परवानगी.
    विद्यार्थी आणि इतर वापरकर्ते फक्त पाहू (view) शकतात.
    """

    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS (पाहण्यासाठीच्या) रिक्वेस्टसाठी सर्वांना परवानगी आहे.
        if request.method in permissions.SAFE_METHODS:
            return True

        # POST, PUT, DELETE (बदल करण्यासाठीच्या) रिक्वेस्टसाठी,
        # वापरकर्ता 'teacher' असणे आवश्यक आहे.
        # (आपण असे मानत आहोत की प्रत्येक user ला एक profile जोडलेले आहे, ज्यात role आहे)
        return request.user.is_authenticated and hasattr(request.user, 'profile') and request.user.profile.role == 'teacher'

class IsStudentOwner(permissions.BasePermission):
    """
    कस्टम परमिशन: फक्त विद्यार्थ्यांना काही विशिष्ट क्रिया करण्याची परवानगी.
    उदा. असाइनमेंट सबमिट करणे.
    """

    def has_permission(self, request, view):
        # ही क्रिया फक्त 'student' भूमिकेतील वापरकर्तेच करू शकतात.
        return request.user.is_authenticated and hasattr(request.user, 'profile') and request.user.profile.role == 'student'

    def has_object_permission(self, request, view, obj):
        # ऑब्जेक्ट-लेव्हल परवानगीसाठी (उदा. विद्यार्थी फक्त स्वतःचे सबमिशन पाहू/बदलू शकतो).
        # SAFE_METHODS साठी नेहमी परवानगी द्या.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # ऑब्जेक्टचा मालक (student) आणि रिक्वेस्ट करणारा वापरकर्ता एकच आहे का ते तपासा.
        # (उदा. obj हे Submission मॉडेलचे ऑब्जेक्ट असेल तर)
        # return obj.student == request.user
        
        # सध्याच्या वापरासाठी, has_permission पुरेसे आहे.
        return True
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    ऑब्जेक्टचा मालक असल्यास त्याला बदल करण्याची परवानगी, इतरांना फक्त पाहण्याची.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # उदा. Query चा मालक (student) आणि रिक्वेस्ट करणारा एकच आहे का?
        return obj.student == request.user

class IsTeacher(permissions.BasePermission):
    """
    फक्त 'teacher' भूमिकेतील वापरकर्त्यांना परवानगी.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'profile') and request.user.profile.role == 'teacher'


