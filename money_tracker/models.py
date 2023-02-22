from django.db import models

class TransactionRecord(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

TYPE_CHOICES = [
    ('Pengeluaran', 'Pengeluaran'),
    ('Pemasukan', 'Pemasukan')
]

class TransactionRecord(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


