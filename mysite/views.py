from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import Form
def home(requests):
    Students = Form.objects.all()
    context = {
        'Students':Students,
    }
    return render(requests,'home.html', context)