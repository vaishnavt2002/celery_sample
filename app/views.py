from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .tasks import generate_sub_tasks


def trigger_task(request):
    generate_sub_tasks.delay()
    return JsonResponse({"status": "Parent task started!"})
