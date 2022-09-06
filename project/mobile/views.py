from django.shortcuts import render
from rest_framework import viewsets
from .models import humanInfo
from .serializers import hInfoSerializer
# Create your views here.

class hInfoViewSet(viewsets.ModelViewSet):
    queryset = humanInfo.objects.all()
    serializer_class = hInfoSerializer
    

