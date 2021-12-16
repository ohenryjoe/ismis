from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
)
from django.db.models import ForeignKey

from hrms.models import Employees
from . import utils


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128, null=True)
    employee_id = ForeignKey(Employees, blank=True, null=True, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=128, null=True)
    is_active = models.BooleanField(default=True)  # default=False when you are going to implement Activation Mail
    is_admin = models.BooleanField(default=False)

    objects = utils.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def has_perms(self, perm, ob=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def natural_key(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
