from django.shortcuts import render
from django import template
from django.conf import settings
from django.template import loader
from django.http import JsonResponse,HttpResponse
# Create your views here.

def home(request):
    context ={}
    try:
        return render(request, 'uifiles/home.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
