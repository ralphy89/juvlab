from django.db.models import fields
from rest_framework import serializers
from .models import Student, Computer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name',
                  'email', 'phone', 'status',
                  'program', 'created', 'updated')


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ('host_name', 'mac_adr',
                  'status', 'created', 'updated',
                  'pc_model')
