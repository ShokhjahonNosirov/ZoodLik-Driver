from rest_framework import serializers
from .models import Taklif, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
class TaklifSerializer(serializers.ModelSerializer):
    Ism = serializers.CharField(source='Author.ism', read_only=True)
    Familiya = serializers.CharField(source='Author.familiya', read_only=True)
    # Author = serializers.CharField(source='Author.driver.username', read_only=True)
    class Meta:
        model = Taklif
        fields = [
            'Ism', 'Familiya', 'Author', 'Qayerdan', 'Qayerga', 'Orinlar_soni', 'Kun', 'Narx', 'Vaqt'
        ]

        #read_only_fields = ('Author',)

def get_author_id(self, comment):
    username = comment.user.username
    return username
