from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime,timezone
from .models import *
from .utilis import *
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def mobial_otp_logic(request):
    context = {}
    try:
        post_data = request.POST
        phone = post_data.get('mobile')
        if not phone:
            return JsonResponse({'error': 'Mobile number is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = Users.objects.get(phone=phone, is_active=True)
        if user:
            otp = generate_otp()
            # send_otp(phone, otp)
            user.otp = otp
            print('sending otp is :'+ otp)
            user.otp_timestamp = datetime.now()
            user.save()
            request.session['user_id'] = user.id
            return JsonResponse({'message': 'OTP Sent. Register Phone number successfully!', 'user_id': user.id}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'User not found or inactive'}, status=status.HTTP_400_BAD_REQUEST)

    except Users.DoesNotExist:
        return JsonResponse({'error': 'Phone number does not exist'}, status=status.HTTP_404_NOT_FOUND)


def mobial_otp_verify_logic(request):
    context = {}
    try:
        user_id = request.session.get('user_id')
        otp = request.POST['otp']
            
        user = Users.objects.get(id=user_id,is_active=True)
        current_time = datetime.now(timezone.utc)
        time_difference = user.otp_timestamp - current_time
        if (time_difference.total_seconds()/60) < 1:
            return JsonResponse({'error': 'OTP expired. Request for resend otp !!'}, status=status.HTTP_400_BAD_REQUEST)
            
        if int(otp) == user.otp:
            user.otp = None
            user.save()
            login(request, user)
            if user.role == "admin":
                print('admin')
                return JsonResponse({'path': '/admin/'},status=status.HTTP_200_OK)
                    
            elif user.role == "employee":
                print("employee")
                return JsonResponse({'path': '/dashboard/'},status=status.HTTP_200_OK)
            else:
                print("cluster")
                return JsonResponse({'path': '/cluster_dashboard/'},status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({'error': f'{e}'}, status=401)


@csrf_exempt
@login_required
def shop_owner_save_logic(request):
    if request.method == 'POST':
        try:
            # Extract form data
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            shop_name = request.POST['shop_name']
            shop_type = request.POST['shopType']
            rcb_agreement = request.POST['rcbAgreement']
            area = request.POST['area']
            city = request.POST['city']
            state = request.POST['state']
            zip_code = request.POST['zip_code']

            
            if len(first_name) < 2:
                return JsonResponse({'error': 'First name must be at least 2 characters long.'}, status=400)
            if len(phone) < 10:
                return JsonResponse({'error': 'Please enter a valid phone number.'}, status=400)
        
            user = Users()
            user.first_name = first_name
            user.last_name = last_name
            user.username = f'{first_name}{last_name}'
            user.phone = phone
            user.email = email
            user.pincode = zip_code
            user.created_at = datetime.now()
            user.updated_at = datetime.now()
            user.save()

            shop_owner = ShopOwner()
            shop_owner.shopowner_number = generate_shop_number()
            shop_owner.user = user
            shop_owner.shop_name=shop_name
            shop_owner.shop_type =shop_type
            shop_owner.rcb_agreement=bool(rcb_agreement)
            shop_owner.area=area
            shop_owner.city=city
            shop_owner.state=state
            shop_owner.created_at = datetime.now()
            shop_owner.updated_at = datetime.now()
            shop_owner.created_by = request.user
            shop_owner.save()

            return JsonResponse({'message': 'OTP Sent. Register Phone number successfully!','path': '/add_transaction/'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)