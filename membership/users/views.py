from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.exceptions import NotFound
from addresses.models import Address
from addresses.serializer import AddressSerializer
class User(APIView) :
    def get_object(self, user_id) :
        try :
            return Address.objects.get(id = user_id)
        except Address.DoesNotExist :
            raise NotFound
        
    def get(self, request, user_id) :
        user = self.get_object(user_id)
        serializer = AddressSerializer(user)
        return Response(serializer.data)
    
    def post(self, request) :
        serializer = AddressSerializer(data = request.data)

        if serializer.is_valid() :
            address = serializer.save(user = request.user)

            serializer = AddressSerializer(address)
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        
    