# Django
from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    """ Deprtments Catalog. """
    fDepartmet = models.ForeignKey('self', null=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return description."""
        return self.description


class Userinfo(models.Model):
    """Profile model.
    Proxy model that extends the base data with other
    information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username


class Menu(models.Model):
    """ Menu Catalog. """
    fMenu = models.ForeignKey('self', null=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=30)
    icon = models.TextField(max_length=60)
    url = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return description."""
        return self.description





