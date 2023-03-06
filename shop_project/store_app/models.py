from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='BannerImage')
    http_link = models.URLField(max_length = 300, blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 150)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child')
    image = models.ImageField(upload_to='CategoryImage')

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='BrandImage')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ProductImage')
    price  = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    description  = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity  = models.IntegerField()

    def __str__(self):
        return self.name
    

class CartProduct(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name
    
    def get_subtotal(self):
        if self.product.discount_price:
            return self.product.discount_price * self.quantity
        else:
            return self.product.price * self.quantity
        
class Order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_products = models.ManyToManyField(CartProduct)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()
    total_order_amount  = models.IntegerField(default=500)
    # PaymentOption = (
    #     ('Cash On Delivery','Cash On Delivery'),
    #     ('SSL Commerz','SSL Commerz'),
    # )
    payment_option = models.CharField(max_length=100,blank=True , null=True)
    

    
    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for i in self.cart_products.all():
            total += i.get_subtotal()
        return total

    def total(self):
        return self.get_total() + 100

class WishList(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

