from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# views 2
from rest_framework.generics import RetrieveAPIView, ListAPIView
from driver.models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


# login register
@api_view(["POST", ])
def logout_user(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)


@api_view(["POST", ])
def user_register_view(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Account has been created'
            data['username'] = account.username

            # token = Token.objects.get(user=account).key
            # data['token'] = token

            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            data = serializer.errors
        return Response(data)

# end login register

# profile api views


class ProfileView(APIView):
    # user only have reading permission
    # permission_classes = [IsAdminUserOrReadOnly]
    def get(self, request, format=None, **kwargs):
        course = Profile.objects.all()
        serializer = ProfileSerializer(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


