from django.db import models

# Create your models here.
class tbl_bank(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

class tbl_branch(models.Model):
    value = models.CharField(max_length=255)
    bank = models.ForeignKey(tbl_bank, on_delete=models.CASCADE, related_name='branches')

    def __str__(self):
        return f"{self.value} ({self.bank.value})"

class tbl_application(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Submitted', 'Submitted'),
    )
    
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_name} ({self.account_number})"