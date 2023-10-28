from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department
from employee_mng.models import Employee
from .serializers import DepartmentSerializer
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
        
    def get(self, request):
        try:
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return Response({"all_departments":serializer.data})
        except Exception as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):
        try:
            dep_id = request.query_params.get('dep_id')
            dep_instance = Department.objects.filter(id=dep_id).first()
            
            if not dep_instance:
                return Response('Department ID is not valid',status=status.HTTP_400_BAD_REQUEST)
            
            manager_id = request.query_params.get('manager_id')
            
            if manager_id:
                manager_instance = Employee.objects.filter(id=manager_id).first()
                
                if not manager_instance:
                    return Response('Manager ID is not valid',status=status.HTTP_400_BAD_REQUEST)
            
                dep_instance.manager_id = manager_instance
                dep_instance.save()
            
            dep_name = request.query_params.get('name')
            
            if dep_name:
                dep_instance.name = dep_name
                dep_instance.save()
            
            return Response({"message": "Department updated"},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request):
        try:
            dep_id = request.query_params.get('dep_id')
            dep_instance = Department.objects.filter(id=dep_id).first()
            
            if not dep_instance:
                return Response('Department ID is not valid',status=status.HTTP_400_BAD_REQUEST)
            
            emp_instance = Employee.objects.filter(current_department=dep_id)
            
            if emp_instance:
                for emp in emp_instance:
                    emp.current_department = 0
                    emp.save()
            
            dep_instance.delete()
            return Response('Department deleted successfully',status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
        
        
class AssignDepEmp(APIView):
    def post(self, request):
        try:
            dep_id = request.query_params.get('dep_id')
            emp_id = request.query_params.get('emp_id')
            
            dep_instance = Department.objects.filter(id=dep_id).first()
            
            if not dep_instance:
                return Response('Department ID is not valid',status=status.HTTP_400_BAD_REQUEST)
            
            emp_instance = Employee.objects.filter(id=emp_id).first()
            
            if not emp_instance:
                return Response('Employee ID is not valid',status=status.HTTP_400_BAD_REQUEST)
            
            emp_instance.current_department = dep_id
            emp_instance.save()
            
            return Response({"message": "Department assigned to employee"},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)