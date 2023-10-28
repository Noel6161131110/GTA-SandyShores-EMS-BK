from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Projects
from .serializers import ProjectsSerializer
from department_mng.models import Department
from employee_mng.models import Employee
class ProjectFn(APIView):
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
            
            proj_data = request.data.copy()
            proj_data['dep_id'] = dep_id
            proj_data['project_lead'] = emp_id
            
            serializer = ProjectsSerializer(data=proj_data)
            if serializer.is_valid():
                serializer.save()
                
                proj_id = serializer.instance.id
                
                emp_instance.current_project = proj_id
                emp_instance.save()
                
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            projects = Projects.objects.all()
            serializer = ProjectsSerializer(projects, many=True)
            return Response({"all_projects":serializer.data})
        except Exception as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request):
        try:
            proj_id = request.query_params.get('proj_id')
            proj_instance = Projects.objects.filter(id=proj_id).first()
            
            if not proj_instance:
                return Response('Project ID is not valid',status=status.HTTP_400_BAD_REQUEST)
            
            emp_instance = Employee.objects.filter(current_project=proj_id)
            
            if emp_instance:
                for emp in emp_instance:
                    emp.current_project = 0
                    emp.save()
            
            proj_instance.delete()
            return Response('Project deleted successfully',status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):
        try:
            proj_id = request.query_params.get('proj_id')
            proj_instance = Projects.objects.filter(id=proj_id).first()
            
            if not proj_instance:
                return Response('Project ID is not valid',status=status.HTTP_400_BAD_REQUEST)
            
            serializer = ProjectsSerializer(proj_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response('Project updated successfully',status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)