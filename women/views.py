from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import WomenSerializer
from .models import Category, Women


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        """Добавление нестандартного маршрута"""

        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
