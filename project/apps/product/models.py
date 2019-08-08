from django.db import models
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import ArrayField


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('created at'))

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(_('name'), max_length=200)

    class Meta:
        ordering = ['name']


class Feature(BaseModel):
    name = models.CharField(_('name'), max_length=200)
    values = ArrayField(verbose_name=_('values'),
                        base_field=models.CharField(max_length=200))


class ProductFeature(BaseModel):
    product = models.ForeignKey('Product')
    feature = models.ForeignKey('Feature')
    price = models.IntegerField(_('price'), default=1000)

    class Meta:
        ordering = ['product', 'price']
