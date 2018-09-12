from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields here

    class Meta():
        permissions = (
            ('G1', 'Pode ver x'),
            ('G2', 'Pode ver y'),
            ('G3', 'Pode ver z')
        )

    def __str__(self):
        return self.email