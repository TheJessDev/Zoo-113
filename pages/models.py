from django.db import models
from django.contrib.auth import get_user_model


class Pages(models.Model):
    dept = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    name = models.ForeignKey(
        get_user_model(),
        on_delete=CASCADE
    )

    
