from django.db import models

# Create your models here.
class mobiles(models.Model):
    Mobileid=models.IntegerField()
    Mobilebrand=models.CharField(max_length=100)
    Mobilemodel=models.CharField(max_length=100)
    Mobilecolor=models.CharField(max_length=100)
    Specifications=models.TextField()
    Mobileprice=models.IntegerField()
    Photo=models.ImageField(upload_to="images")

class Meta:
    db_table="mobiles"