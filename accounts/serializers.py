from django.contrib.auth.models import User
from rest_framework import serializers



class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # phone_number = serializers.IntegerField(style={'input_type': 'phone_number'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"Error": "Password Does not match"})

        account = User(username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account

