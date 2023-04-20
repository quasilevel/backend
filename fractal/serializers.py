from rest_framework import serializers
from rest_framework.serializers import *
from .models import task

class taskserializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields =  ['id', 'title', 'summary', 'issue',
                     'created_at', 'completed_at', 'state', 'assignee',]