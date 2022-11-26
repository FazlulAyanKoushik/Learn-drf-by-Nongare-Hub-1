from django.shortcuts import get_object_or_404
from myapp.models import Profile
from myapp.serializers import ProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class ProfileViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving datas.
    """
    def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Profile.objects.all()
        data = get_object_or_404(queryset, pk=pk)
        serializer = ProfileSerializer(data)
        return Response(serializer.data)    
    
    def create(self, request):
        serializer = ProfileSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        queryset = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

    def destroy(self, request, pk=None):
        queryset = Profile.objects.get(pk=pk)

        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   












# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view

# from myapp.models import Profile
# from myapp.serializers import ProfileSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.reverse import reverse

# from rest_framework import mixins
# from rest_framework import generics
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated


# class GenericList(generics.ListCreateAPIView):
    
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
    
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
        
#         print(content)
        
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)
    
# class GenericDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
    

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
    
    
    
    


# class ProfileList(APIView):
#     """
#     List all profiles, or create a new profile.
#     """

#     def get(self, request, format=None):
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProfileDetail(APIView):
#     """
#     Retrieve, update or delete a profile instance.
#     """

#     def get_object(self, pk):
#         try:
#             return Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         profile = self.get_object(pk)
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # Create your views here.
# @api_view(['GET', 'POST'])
# def profile_list(request):
#     """
#     List all code profiles, or create a new profile.
#     """
#     if request.method == 'GET':
#         try:
#             profiles = Profile.objects.all()
#         except Profile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def profile_detail(request, pk):
#     """
#     profile Retrieve, update or delete code.
#     """
#     try:
#         profile = Profile.objects.get(pk=pk)
#     except Profile.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
