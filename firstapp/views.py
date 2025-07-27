from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from firstapp.models import Form
# Create your views here.
def student_profile(request, id):
    profile = get_object_or_404 (Form, id = id )
    context = {
        'profile':profile,
    }
    return render(request, r'D:\Django Project\templates\student_profile.html',context)
    