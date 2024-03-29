from rest_framework import serializers

from .models import Women


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = '__all__'
