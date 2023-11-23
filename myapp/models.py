# models.py

from django.db import models

class Постачальники(models.Model):
    код_постачальника = models.AutoField(primary_key=True)
    назва_компанії_постачальника = models.CharField(max_length=255)
    контактна_особа = models.CharField(max_length=255)
    телефон = models.CharField(max_length=20)
    розрахунковий_рахунок = models.CharField(max_length=30)

    def __str__(self):
        return self.назва_компанії_постачальника

class Матеріали(models.Model):
    код_матеріалу = models.AutoField(primary_key=True)
    назва_матеріалу = models.CharField(max_length=255)
    ціна = models.DecimalField(max_digits=10, decimal_places=2)

class Поставки(models.Model):
    номер_поставки = models.AutoField(primary_key=True)
    дата_поставки = models.DateField()
    код_постачальника = models.ForeignKey(Постачальники, on_delete=models.CASCADE)
    код_матеріалу = models.ForeignKey(Матеріали, on_delete=models.CASCADE)
    кількість_днів = models.PositiveIntegerField()
    кількість_матеріалів = models.PositiveIntegerField()
