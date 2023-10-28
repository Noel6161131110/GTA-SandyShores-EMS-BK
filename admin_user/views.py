from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from employee_mng.models import Employee
from datetime import datetime, timedelta
from employee_mng.serializers import EmployeeSerializer
class UserAuth(APIView):
    def post(self, request, format=None):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user_data = serializer.validated_data  # Use validated_data instead of data
                user = User.objects.filter(
                    user_name=user_data['user_name'],
                    user_email=user_data['user_email'],
                    user_role=user_data['user_role']
                )
                if user:
                    return Response({"message": "User already exists"}, status=status.HTTP_200_OK)
                else:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, format=None):
        try:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response({"all_users": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class UserLogin(APIView):
    def post(self, request, format=None):
        try:
            user_email = request.GET.get('user_email')
            
            user = User.objects.filter(user_email=user_email).first()
            
            if user:
                return Response({"message": "User exists", "user_role": user.user_role}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "User does not exists"}, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class EmployeePromote(APIView):
    def post(self, request, format=None):
        try:
            user_role = request.GET.get('user_role')
            employee_id = request.GET.get('employee_id')
            
            if user_role == "manager" or user_role =="superadmin":
                
                user_instance = Employee.objects.filter(id=employee_id).first()
                date_of_joining = datetime.strptime(user_instance.date_of_joining, '%d/%m/%Y').date()

           
                today = datetime.now().date()


                difference = today - date_of_joining
                
                if difference > timedelta(days=365 * 5):
                    user_instance.assigned_role = "manager"
                    user_instance.save()
                    
                    return Response({"message": "Employee promoted to manager"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Employee can not be promoted because date of joining is less than 5 years"}, status=status.HTTP_200_OK)
               
            else:
                return Response({"message": "User does not exists"}, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)                
class GetEmployeeFiveYear(APIView):
    def get(self, request):
        try:
            emp_instances = Employee.objects.all()
            emp_list = []

            today = datetime.now().date()

            for emp in emp_instances:
                date_of_joining = datetime.strptime(emp.date_of_joining, '%d/%m/%Y').date()

                difference = today - date_of_joining

                if difference > timedelta(days=365 * 5):
                    # Append the serialized data of the employee to the list
                    serializer = EmployeeSerializer(emp)
                    emp_data = serializer.data
                    emp_list.append(emp_data)

            return Response({"employee_list": emp_list}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
