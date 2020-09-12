from django.db import models

# Create your models here.



# Each class is a table with properties such varchar, int, bool, etc.

class User_values(models.Model):

    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contacto'