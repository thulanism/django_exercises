from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def help(request):
    my_dict = {'help_me' : "I am here to help you."}
    return render(request,'AppTwo/help.html',context=my_dict)
    #return HttpResponse("<em>This is my 2nd App!</em>")