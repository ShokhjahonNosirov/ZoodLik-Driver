from rest_framework import serializers
from .models import Taklif, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
class TaklifSerializer(serializers.ModelSerializer):
    Ism = serializers.CharField(source='Author.ism')
    Familiya = serializers.CharField(source='Author.familiya')
    class Meta:
        model = Taklif
        fields = [
            'Ism', 'Familiya', 'Author', 'Qayerdan', 'Qayerga', 'Orinlar_soni', 'Kun', 'Narx', 'Vaqt'
        ]

