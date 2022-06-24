from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField('id', primary_key = True)
    email = models.CharField('email користувача',max_length=100)
    name = models.CharField('имя користувача', max_length=30)
    password = models.CharField('Пароль користувача',max_length=30)

    class Meta:
        verbose_name = 'Users'

class Wallet(models.Model):
    user = models.OneToOneField(Users, on_delete = models.CASCADE, primary_key = True)
    wallet = models.CharField('Гаманець користувача', max_length=150)
    Tron = models.FloatField('Кількість Tron на гаманці', default='0')
    Avira = models.FloatField('Кількість Avira на гаманці', default='0')
    USDT = models.FloatField('Кількість USDT на гаманці', default='0')

class History(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    wallet = models.CharField('Гаманець користувача', max_length=150)
    DateTime = models.DateTimeField('Дата та час транзакції')
    count = models.CharField('Кількість токенів', max_length=50)

class Transaction(models.Model):
    id = models.AutoField('id', primary_key = True)
    wallet_from = models.CharField('З гаманеця користувача', max_length=150)
    wallet_in = models.CharField('В гаманець користувача', max_length=150)
    DateTime = models.DateTimeField('Дата та час транзакції')
    count = models.CharField('Кількість токенів', max_length=50)

class Transaction_turn(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    wallet_from = models.CharField('З гаманеця користувача', max_length=150)
    wallet_in = models.CharField('В гаманець користувача', max_length=150)
    count = models.CharField('Кількість токенів', max_length=50)