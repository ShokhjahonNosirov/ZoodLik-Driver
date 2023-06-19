from rest_framework import serializers
from .models import Taklif, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
class TaklifSerializer(serializers.ModelSerializer):
    # story_post_video = serializers.CharField(source='story_post.video')
    class Meta:
        model = Taklif
        fields = [
            'Author', 'Qayerdan', 'Qayerga', 'Orinlar_soni', 'Narx', 'Vaqt'
        ]
