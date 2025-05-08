from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import datetime
from bootcampManagement.models import Student, Computer


def home(request):
    template = 'home.html'
    participant = Student.objects.all()
    computers = Computer.objects.all()
    page_object = {
        'participants': participant,
        'computers' : computers,
    }
    return render(
        request,
        template,
        page_object,
    )
