from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from admin_user.serializers import UserSerializer

class EmployeeOperations(APIView):
    def post(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                emp_data = serializer.validated_data  
                emp = Employee.objects.filter(name=emp_data['name'])
                
                if emp:
                    return Response({"message": "Employee already exists"}, status=status.HTTP_200_OK)
                else:
                    serializer.save()
                    
                    admin_user_data = {
                        "user_name": emp_data['name'],
                        "user_email": emp_data['email'],
                        "user_role": "employee"
                    }
                    
                    admin_user_serializer = UserSerializer(data=admin_user_data)
                    
                    if admin_user_serializer.is_valid():
                        admin_user_serializer.save()
                    
                        return Response({"message": "Employee created successfully"}, status=status.HTTP_200_OK)   
                    
                    else:
                        return Response({"message": "Employee created successfully but user creation failed"}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        try:
            emp = Employee.objects.all()
            serializer = EmployeeSerializer(emp, many=True)
            return Response({"all_employees": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request): 
        try:
            emp_id = request.query_params.get('emp_id')
            emp_instance = Employee.objects.filter(id=emp_id).first()
            
            if not emp_instance:
                return Response({"message": "Employee ID is not valid"}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = EmployeeSerializer(emp_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Employee updated successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request):
        try:
            emp_id = request.query_params.get('emp_id')
            emp_instance = Employee.objects.filter(id=emp_id).first()
            
            if not emp_instance:
                return Response({"message": "Employee ID is not valid"}, status=status.HTTP_400_BAD_REQUEST)
            
            emp_instance.delete()
            return Response({"message": "Employee deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)