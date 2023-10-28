from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department
from employee_mng.models import Employee

class DepartmentFn(APIView):
    def post(self, request):
        try:
            department_name = request.query_params.get('name')
            manager_id = request.query_params.get('manager_id')
            
            print(department_name, manager_id)
            manager_instance = Employee.objects.filter(id=manager_id).first()
            
            if manager_instance.assigned_role == 'manager':
                department = Department(name=department_name, manager_id=manager_instance)
                department.save()
                return Response({"message": "Department created"},status=status.HTTP_201_CREATED)
            
            return Response('Manager ID is not valid',status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)