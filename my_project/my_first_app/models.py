from django.db import models

class Аpartments(models.Model):
    name=models.CharField("Название",max_length=50)
    price=models.IntegerField("Цена")
    adress=models.TextField("Адрес",max_length=40)
    guests=models.IntegerField("Количество гостей")
    beds=models.IntegerField("Количество спальныx мест")