from django.db import models
from django.core.validators import MinLengthValidator

class task(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    summary = models.TextField(max_length=100,validators=[MinLengthValidator(20)])
    issue = models.IntegerField(null=True)
    created_at = models.DateField()
    completed_at = models.DateField() 
    state_choices =[
        ('pending', 'pending'),
        ('active', 'active'),
        ('completed', 'completed'),
        ('dropped', 'dropped'),
    ]
    state = models.CharField(max_length=20, choices = state_choices,default='pending')
    assignee = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.title

