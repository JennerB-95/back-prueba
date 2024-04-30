from django.db import models

# Create your models here.
class Unit(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    # ForeignKey
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Employee(models.Model):
    code = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    # ForeignKey
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} {} / {}'.format(self.first_name, self.last_name)