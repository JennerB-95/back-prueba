from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import *
from .models import *
# Create your views here.
class UnitView(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()


class DepartmentView(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentListView(generics.ListAPIView):
    serializer_class = CreateDepartmentSerializers

    def get_queryset(self):
        unit_id = self.kwargs['unit_id']
        return Department.objects.filter(unit_id=unit_id)


class CreateDepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = CreateDepartmentSerializers
    queryset = Department.objects.all()


class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    

class CreateEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = CreateEmployeeSerializers
    queryset = Employee.objects.all()


class RecordCountView(APIView):
    def get_queryset(self):
        return Unit.objects.none()

    def get(self, request):
        unit_count = Unit.objects.count()
        department_count = Department.objects.count()
        employee_count = Employee.objects.count()

        return Response({
            'unit_count': unit_count,
            'department_count': department_count,
            'employee_count': employee_count,
        })