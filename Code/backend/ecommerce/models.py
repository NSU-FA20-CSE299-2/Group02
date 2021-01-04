from django.db import models
from account.models import User, Address
import uuid
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name



class Item(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0)
    primary_category = models.ForeignKey(Category, related_name='primary_products', blank=True, null=True, on_delete=models.CASCADE)
    secondary_categories = models.ManyToManyField(Category, blank=True)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='product_images')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)

    def get_price(self):
        return "{:.2f}".format(self.price / 100)

    @property
    def in_stock(self):
        return self.stock > 0

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(
        "Order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_raw_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_item_price(self):
        price = self.get_raw_total_item_price()
        return "{:.2f}".format(price / 100)


class Order(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)

    billing_address = models.ForeignKey(
        Address, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.id}"

    def get_raw_subtotal(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_raw_total_item_price()
        return total

    def get_subtotal(self):
        subtotal = self.get_raw_subtotal()
        return "{:.2f}".format(subtotal / 100)

    def get_raw_total(self):
        subtotal = self.get_raw_subtotal()
        # total = subtotal - discounts + tax + delivery
        return subtotal

    def get_total(self):
        total = self.get_raw_total()
        return "{:.2f}".format(total / 100)

class Payment(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=(
        ('Online', 'Online'),
        ('Cash', 'Cash')
    ))
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"PAYMENT-{self.order}-{self.id}"

def pre_save_item_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(pre_save_item_receiver, sender=Item)