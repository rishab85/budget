from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from .models import user
from .serializer import userSerializer

class userList(APIView):

    def get(self, request, format=None):
        use = user.objects.all()
        serializer = userSerializer(use, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userDetail(APIView):
    def get_object(self, user_name):
        try:
            return user.objects.get(user_name=user_name)
        except user.DoesNotExist:
            raise Http404

    def authenticate(self, user_name):
        user = get_object()
        if(user):
            return true
        else:
            return false

    def get(self, request, user_name, format=None):
        use = self.get_object(user_name)
        serializer = userSerializer(use)
        return Response(serializer.data)

    def put(self, request, user_name, format=None):
        use = self.get_object(user_name)
        serializer = budzetSerializer(use, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_name, format=None):
        use = self.get_object(user_name)
        use.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

