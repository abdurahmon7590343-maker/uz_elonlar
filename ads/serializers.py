from rest_framework import serializers
from .models import Category, Advertisement, Resume

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AdvertisementSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Advertisement
        fields = '__all__'
        read_only_fields = ('author',)

class ResumeSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ('user',)
