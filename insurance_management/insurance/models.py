from django.db import models
from django.utils import timezone

class PolicyHolder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Policy(models.Model):
    holder = models.ForeignKey(PolicyHolder, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.policy_type} - {self.holder.name}'
