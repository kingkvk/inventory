from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_quantity=models.IntegerField()

    def __str__(self):
        return self.product_name

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class OrderDetails(models.Model):
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)