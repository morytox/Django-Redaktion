# Create your views here.
from django.shortcuts import render_to_response
from models import *
from redaktion.werbung.models import *

def home(request, template_name):
    return render_to_response(template_name, {"ads":werbung.objects.all()})

def published(request, template_name):
    return render_to_response(template_name, {"storys":story.objects.filter(status="P"), "ads":werbung.objects.all()})

def archive(request, template_name):
    return render_to_response(template_name, {"storys":story.objects.filter(status="A"), "ads":werbung.objects.all()})

def draft(request, template_name):
    return render_to_response(template_name, {"storys":story.objects.filter(status="D"), "ads":werbung.objects.all()})