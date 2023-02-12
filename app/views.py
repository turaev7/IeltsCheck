from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class DateView(ListView):
    model= Full
    context_object_name="Date"
    template_name="date.html"

