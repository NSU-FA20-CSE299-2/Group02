from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

class User(AbstractUser):
    username = models.CharField(max_length=128, unique=True, primary_key=True, name='username',
        help_text='Required. 128 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.',
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid'),
        ],
        error_messages={
            'unique': "A user with that username already exists.",
        })
    mobileNo = models.CharField(max_length=16)

    def __str__(self):
        return self.username

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apt = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    street_opt = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    zip_code = models.CharField(max_length=20)
    mobile = models.CharField(max_length=16)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True)

    def __str__(self):
        return f"{self.street}, {self.street_opt}, {self.city}, {self.zip_code}"

    class Meta:
        verbose_name_plural = 'Addresses'