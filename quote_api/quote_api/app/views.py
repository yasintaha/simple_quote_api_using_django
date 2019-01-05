from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quote_model
from .serializer import Quote_Serializer
# Create your views here.
class QuoteView(APIView):
    def get(self,request):
        db_data = Quote_model.objects.all()
        ser_data = Quote_Serializer(db_data,many=True)
        return Response(ser_data.data,status=status.HTTP_200_OK)

    def post(self,request):
        ser_data = Quote_Serializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.data,status=status.HTTP_404_BAD_REQUEST)    