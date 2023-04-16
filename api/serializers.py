from rest_framework import serializers
from rest_framework.serializers import *
from fractal.models import task

class fractalserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = task
        fields =  ['id', 'title', 'summary', 'issue',
                     'created_at', 'completed_at', 'state', 'assignee',]