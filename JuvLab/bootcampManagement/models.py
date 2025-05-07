from django.db import models


# Create your models here.

class Student(models.Model):
    STATUS = {
        'A': 'Active',
        'I': 'Inactive',
        'D': 'Deleted'
    }
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # code = models.CharField(max_length=255, unique=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default=STATUS['I'])
    # computer = models.ForeignKey(Computer, on_delete=models.PROTECT, null=True, to_field='name')
    program = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-updated', '-created']



