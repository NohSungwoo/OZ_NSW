from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Address
from .serializer import AddressSerializer

class Addresses(APIView) :
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request) :
        addresses = Address.objects.all()
        # 여러 객체들을 사용할 때는 many = True 옵션으로 목록화 해 줘야 한다.
        selrializer = AddressSerializer(addresses, many = True)
        return Response(selrializer.data)

class AddressDetail(APIView) :
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, address_id) :
        try :    
            address = Address.objects.get(id = address_id)
        except Address.DoesNotExist :
            return None
        serializer = AddressSerializer(address)
        return Response(serializer.data)

class PutAddress(APIView) :

    def get_objects(self, address_id) :
        try :
            return Address.objects.get(id = address_id)
        except Address.DoesNotExist :
            return None
            
    def get(self, request, address_id) :
        address = self.get_objects(address_id)
        if address is None :
            return Response({'error' : 'Address not found'})
        
        serializer = AddressSerializer(address)
        return Response(serializer.data)
                                                                                                   
    def put(self, request, address_id) :
        address = self.get_objects(address_id)
        if address is None :
            return Response({'error' : 'Address not found'})
        
        serializer = AddressSerializer(address, data = request.data, partial = True)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DeleteAddress(APIView) :
    def get_objects(self, address_id) :
        try :
            return Address.objects.get(id = address_id)
        except Address.DoesNotExist :
            return None
            
    def get(self, request, address_id) :
        address = self.get_objects(address_id)
        if address is None :
            return Response({'error' : 'Address not found'})
        
        serializer = AddressSerializer(address)
        return Response(serializer.data)
    
    def delete(self, request, address_id) :
        address = self.get_objects(address_id)
        if address is None :
            return Response({'error' : 'Address not found'})
        address.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)