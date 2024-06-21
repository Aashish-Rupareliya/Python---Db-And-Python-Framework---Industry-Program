from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import PolicyHolder
from .forms import PolicyHolderForm
from django.core.mail import send_mail
from django.conf import settings
import logging

# Set up logging
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'insurance/home.html')

def register_policy_holder(request):
    if request.method == 'POST':
        form = PolicyHolderForm(request.POST)
        if form.is_valid():
            try:
                policy_holder = form.save()
                send_mail(
                    'Registration Successful',
                    'Thank you for registering.',
                    settings.EMAIL_HOST_USER,
                    [policy_holder.email],
                    fail_silently=False,
                )
                return JsonResponse({'message': 'Registration successful!'}, status=200)
            except Exception as e:
                logger.error(f"Error during registration: {e}")
                return JsonResponse({'message': 'Registration failed due to server error.'}, status=500)
        else:
            logger.error(f"Form errors: {form.errors.as_json()}")
            return JsonResponse({'message': 'Registration failed due to invalid form data.'}, status=400)
    else:
        form = PolicyHolderForm()
    return render(request, 'insurance/register.html', {'form': form})
