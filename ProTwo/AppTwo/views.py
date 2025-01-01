from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<em>This is my 2nd App!</em>"+"<div>This is a Div line.</div>"+"<p>The main thrust of the story is in the intepretation you choose to adopt as the meaning.</p>")