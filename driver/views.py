from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Profile, Taklif
from .serializers import TaklifSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions

# from .permissions import TaklifUserOrReadOnly
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# custom permission: if user is admin, he ca do CRUD


class TaklifUserOrReadOnly(BasePermission):
    message = 'Editing posts is restricted to the author only.'
    def has_object_permission(self, request, view, obj):
        # print(request.user, "heelo1")
        # print(obj.Author.driver.username, "heelo")
        if request.method in SAFE_METHODS:
            return True
        print(obj.Author.username)
        print(str(request.user))
        return obj.Author.username == str(request.user)



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


class TaklifDetailView(generics.RetrieveUpdateDestroyAPIView, TaklifUserOrReadOnly):
    permission_classes = [TaklifUserOrReadOnly]
    queryset = Taklif.objects.all()
    serializer_class = TaklifSerializer



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


# class TaklifDetailView(APIView, TaklifUserOrReadOnly):
#
#     permission_classes = [TaklifUserOrReadOnly]
#
#     def get(self, request, pk):
#         taklif = Taklif.objects.get(pk=pk)
#         serializer = TaklifSerializer(taklif)
#         #print("heelo")
#         return Response(serializer.data, status = status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         taklif = Taklif.objects.get(pk=pk)
#         serializer = TaklifSerializer(taklif, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         taklif = Taklif.objects.get(pk=pk)
#         taklif.delete()
#         return Response(status=status.HTTP_200_OK)