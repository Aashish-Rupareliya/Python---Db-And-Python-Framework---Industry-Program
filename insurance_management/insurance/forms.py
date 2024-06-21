from django import forms
from .models import PolicyHolder, Policy

class PolicyHolderForm(forms.ModelForm):
    class Meta:
        model = PolicyHolder
        fields = ['name', 'email', 'phone', 'address']

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['holder', 'policy_type', 'start_date', 'end_date', 'premium']
