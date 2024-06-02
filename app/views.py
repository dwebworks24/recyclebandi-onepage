from django.shortcuts import redirect, render
from django import template
from django.conf import settings
from django.template import loader
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.serializers import serialize
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

def hometwo(request):
    context ={}
    try:
        return render(request, 'uifiles/twohome.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    

@login_required
def dashboard(request):
    context ={}
    try:
        context['users'] = Users.objects.filter(id=request.user.id).first()
        context['transaction'] = PickupTransaction.objects.filter(created_by= request.user.id,shop_owner__user__role='cluster')

        return render(request, 'uifiles/dashboard.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required
def clusterdashboard(request):
    context ={}
    try:
        context['transactionwaste'] = PickupWastData.objects.filter(pickup_transaction__shop_owner__user__id=request.user.id)
        return render(request, 'uifiles/cluster_dashboard.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))



def cluster_form(request):
    context ={}
    try:
        context['owners'] = ShopOwner.objects.all()
        context['waste'] = WasteType.objects.all()
        context['waste_obj_json'] = serialize('json', context['waste'])
        return render(request, 'uifiles/add_cluster_transcration.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))



def add_shop(request):
    context ={}
    try:
        return render(request, 'uifiles/add_shop.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(context, request))
    


def login_logic(request):
    if request.method == "POST":
        try:
            email = request.POST.get("emailId")
            password = request.POST.get("password")
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if user:
                    if user.role == "admin":
                        print('admin')
                        return JsonResponse({'redirect_url': '/admin/'})
                    
                    elif user.role == "employee":
                        print("employee")
                        return JsonResponse({'redirect_url': '/dashboard/'})
                    else:
                        print("cluster")
                        return JsonResponse({'redirect_url': '/cluster_dashboard/'})
            else:
                msg = 'Invalid credentials'
        
        except KeyError:
            return JsonResponse({'message': 'Invalid request parameters.'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
            return JsonResponse({'message': 'Method not allowed.'}, status=405)
    

@login_required
def logout_view(request):
    context ={}
    try:
        logout(request)
        return redirect('/')
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
def mobial_otp_view(request):
    context ={}
    try:
       return render(request, 'uifiles/mobial_login.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
    
def verified_otp_view(request):
    context ={}
    try:
       return render(request, 'uifiles/otp_verification.html',context)
    
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('uifiles/page-404.html')
        return HttpResponse(html_template.render(request))
    except:
        html_template = loader.get_template('uifiles/page-500.html')
        return HttpResponse(html_template.render(request))
