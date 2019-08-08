from django.db import models
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import ArrayField


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('created at'),
                                      auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(_('name'), max_length=200)
    features = models.ManyToManyField('Feature',
                                      through='ProductFeature')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Feature(BaseModel):
    name = models.CharField(_('name'), max_length=200)
    values = ArrayField(verbose_name=_('values'),
                        base_field=models.CharField(max_length=200))

    def __str__(self):
        return self.name


class ProductFeature(BaseModel):
    product = models.ForeignKey('Product')
    feature = models.ForeignKey('Feature')
    value = models.CharField(_('value'), max_length=200)
    price = models.IntegerField(_('price'), default=1000)

    class Meta:
        ordering = ['product', 'price']

    def __str__(self):
        return ','.join((str(self.product), str(self.feature), str(self.price)))