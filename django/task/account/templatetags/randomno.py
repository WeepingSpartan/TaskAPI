import random
from django import template
import requests 
from django.http import HttpResponse
import json

register = template.Library()

@register.simple_tag
def random_int(b=None):
    response= requests.get("http://localhost:8000/")
    return response.text
