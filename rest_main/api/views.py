from django.http import JsonResponse
from django.shortcuts import render
from students.models import students
from employee.models import Employee
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import StudentsSerializer, EmployeeSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .paginators import LargeResultsSetPagination

# Create your views here.
@api_view(['GET','POST'])
def students_all(request):
  if request.method == 'GET':
    students1 = students.objects.all()
    serializer = StudentsSerializer(students1, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = StudentsSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
@api_view(['GET', 'PUT','DELETE'])
def student_detail(request, student_id):
  try:
    student = students.objects.get(student_id=student_id)
  except students.DoesNotExist:
    return Response(status=404)

  if request.method == 'GET':
    serializer = StudentsSerializer(student)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = StudentsSerializer(student, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=200)
    return Response(serializer.errors, status=400)
  elif request.method == 'DELETE':
    student.delete()
    return Response(status=204)
"""
class EmployeeAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
class Employee_Detail(APIView):
    def get_object(self, emp_id):
        try:
            return Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            return None

    def get(self, request, emp_id):
        employee = self.get_object(emp_id)
        if employee is None:
            return Response(status=404)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, emp_id):
        employee = self.get_object(emp_id)
        if employee is None:
            return Response(status=404)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, emp_id):
        employee = self.get_object(emp_id)
        if employee is None:
            return Response(status=404)
        employee.delete()
        return Response(status=204)
"""
#listcreateupdate api view
from employee.filters import EmployeeFilter
class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = LargeResultsSetPagination
    filterset_class = EmployeeFilter

class Employee_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'emp_id'