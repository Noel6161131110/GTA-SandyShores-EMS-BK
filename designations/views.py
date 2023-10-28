from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Designation
from .serializers import DesignationSerializer

class DesignationView(APIView):
    def post(self, request, format=None):
        try:
            serializer = DesignationSerializer(data=request.data)
            if serializer.is_valid():
                des_data = serializer.validated_data  
                des = Designation.objects.filter(name=des_data['name'])
                
                if des:
                    return Response({"message": "Designation already exists"}, status=status.HTTP_200_OK)
                else:
                    serializer.save()
                    return Response({"message": "Designation created successfully"}, status=status.HTTP_200_OK)   

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        try:
            des = Designation.objects.all()
            serializer = DesignationSerializer(des, many=True)
            return Response({"all_designations": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
