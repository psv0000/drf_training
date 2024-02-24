from django.db.migrations import serializer
from django.forms import model_to_dict
from django.shortcuts import render
from django.template.base import kwarg_re
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import WomenSerializer
from .models import Women


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        Women.objects.filter(pk=pk).delete()

        return Response({'post': 'delete post ' + str(pk)})
