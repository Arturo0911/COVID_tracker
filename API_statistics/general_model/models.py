from django.db import models


class Universal_cases(models.Model):

    country = models.CharField(max_length = 200)
    cases = models.IntegerField()

    def __str__(self):

        return self.country

    class Meta:

        verbose_name = "country"
        verbose_name_plural = "Countries"


# Create your models here.
