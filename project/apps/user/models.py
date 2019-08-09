from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models


class User(AbstractUser):
    phone = models.CharField(_('phone'), max_length=10, blank=True)
    # USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('date_joined',)

    def __str__(self):
        return self.get_full_name()