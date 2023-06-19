from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from .models import Profile, Taklif
from .serializers import TaklifSerializer, ProfileSerializer
from rest_framework.views import APIView


class TaklifView(ListAPIView):
    serializer_class = TaklifSerializer
    queryset = Taklif.objects.all()

class ProfileView(APIView):
    def get(self, request, format=None, **kwargs):
        course = Profile.objects.all()
        serializer = ProfileSerializer(course, many=True)
        return Response(serializer.data)