from django.views.generic.base import View # it's here because this is views.py. Ya might need it
from rest_api.models import Student
from rest_api.serializers import DataModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

class Students(APIView):
    # retrieve a list of the Student records in the DB
    def get(self, request):
        students = Student.objects.all()
        serializer = DataModelSerializer(students, many=True) # use many to serialize a queryset
        return Response(serializer.data) # status is 200 by default
    
    # add in a student with the passed in name
    def post(self, request):
        new_stdt_name = request.data.get('name', None)
        if not new_stdt_name:
            return no_name_error()
        student = Student()
        student.name = new_stdt_name
        student.save()
        serializer = DataModelSerializer(student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# a couple utility functions
def no_name_error():
    return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"No name provided"})

def nonexistent_id_error():
    return Response(status=status.HTTP_404_NOT_FOUND, data={'message':"No student with that ID"})

class StudentInstance(APIView):
    # retrieve an existing student with the id from the URL
    def get(self, request, id):
        student = Student.objects.filter(id=id).first()
        if not student:
            return nonexistent_id_error()
        serializer = DataModelSerializer(student)
        return Response(serializer.data)
    
    # delete a student with the id from the URL
    def delete(self, request, id):
        student = Student.objects.filter(id=id)
        if not student:
            return nonexistent_id_error()
        student.delete()
        return Response(status.HTTP_200_OK)

    # modify name of student with the id in the URL
    # to make that student's name the passed in name
    def put(self, request, id):
        student = Student.objects.filter(id=id).first()
        if not student:
            return nonexistent_id_error()
        new_name = request.data.get('name', None)
        if not new_name:
            return no_name_error()
        student.name = new_name
        student.save()
        serializer = DataModelSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

