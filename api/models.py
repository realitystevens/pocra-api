import os
import random
from decouple import config
from django.db import models
from django.utils.timezone import datetime
from cloudinary.models import CloudinaryField



def idHash():
    letters = "acemnosuvwxz"
    digits = "45678"

    while True:
        output = []
        input = random.choices(letters + digits, k=6)

        for i in range(len(input)-1):
            if input[i].isdigit() and input[i+1].isdigit():
                input[i+1] = random.choice(letters)
            elif input[i].isalpha() and input[i+1].isalpha():
                input[i+1] = random.choice(digits)
            elif input[0].isdigit():
                input[0] = random.choice(letters)
            else:
                continue

            if input[-1].isdigit():
                input[-1] = random.choice(letters)
            else:
                continue

        output = "".join(input)

        return output
    



class Product(models.Model):
    id = models.CharField(max_length=6, default=idHash, primary_key=True, unique=True, blank=False)
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='', blank=True)
    if config('ENVIRONMENT') == 'PRODUCTION':
        image = models.CloudinaryField('image')
    else:
        image = models.ImageField(upload_to='assets/products', blank=True, default='')
    url = models.URLField(default='', blank=True)
    price = models.CharField(max_length=20, default='', blank=True)
    is_published = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    published_at = models.DateTimeField(default=datetime.now if is_published else None, editable=True, blank=True)


    def __str__(self):
        return self.id
