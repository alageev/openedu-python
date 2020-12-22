from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Курс OpenEdu'
        verbose_name_plural = 'Курсы OpenEdu'
