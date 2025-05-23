from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Computer
from .serializers import StudentSerializer, ComputerSerializer
from rest_framework import serializers, status
import json


# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'view_students': '/',
        'search by email': '/?email=student_email',
        'Add_Students': '/add_students',
        'Update_Students': '/update_students/pk',
        'Change_Students_Status': '/change_p_status/pk',
        'view_computers': '/',
        'search by host name': '/?host_name=host_name',
        'Add_Computers': '/add_computers',
        'Update_Computers': '/update_students/pk',
    }

    return Response(api_urls)


@api_view(['POST'])
def add_students(request):
    student = StudentSerializer(data=request.data)
    # validating for already existing data
    if Student.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Student already exists')

    if student.is_valid():
        student.save()
        print('Student saved successfully')
        return Response(student.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_computers(request):
    computer = ComputerSerializer(data=request.data)
    # validating for already existing data
    if Computer.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Computer already exists')
    print(computer)
    if computer.is_valid():
        computer.save()
        print('Computer saved successfully')
        return Response(computer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_students(request):
    # checking for the parameters from the URL

    if request.query_params:
        students = Student.objects.filter(**request.query_params.dict())
    else:
        students = Student.objects.all()

    if students:
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_computers(request):
    # checking for the parameters from the URL
    if request.query_params:
        computers = Computer.objects.filter(**request.query_params.dict())
    else:
        computers = Computer.objects.all()

    if computers:
        serializer = ComputerSerializer(computers, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_students(request, pk):
    student = Student.objects.get(id=pk)
    data = StudentSerializer(instance=student, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_computers(request, pk):
    computer = Computer.objects.get(id=pk)
    data = StudentSerializer(instance=computer, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def change_participant_status(request, pk):
    student = Student.objects.get(id=pk)
    current_status = student.status
    student.status = request.data['new_status'] if request.data['new_status'] != current_status else current_status
    if student.status in ['A', 'I']:

        student.save()
        return Response({'Message': 'Status Changed'})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
