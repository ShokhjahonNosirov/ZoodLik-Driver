from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Taklif
from .serializers import TaklifSerializer, ProfileSerializer
from rest_framework.views import APIView
from .permissions import IsAdminUserOrReadOnly
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class TaklifView(APIView):
    def get(self, request, format = None):
        takliflar = Taklif.objects.all()
        serializer = TaklifSerializer(takliflar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = TaklifSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self):

class ProfileView(APIView):
    # user only have reading permission
    #permission_classes = [IsAdminUserOrReadOnly]

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