from django.db.migrations import serializer
from django.forms import model_to_dict
from django.shortcuts import render
from django.template.base import kwarg_re
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import WomenSerializer
from .models import Women


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
