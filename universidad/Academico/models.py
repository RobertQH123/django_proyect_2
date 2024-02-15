from django.db import models

# Create your models here.

class Curso(models.Model):
    name = models.CharField(max_length=30)
    credit = models.PositiveSmallIntegerField()
    class Meta:
        verbose_name = ("Curso")
        verbose_name_plural = ("Cursos")

    def __str__(self):
        return self.name
