from django.db import models, transaction
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import ArrayField

from project.apps.order.consts import ORDER_STATUS
from project.utils.model import BaseModel


class Order(BaseModel):
    user = models.ForeignKey('user.User', related_name='orders')
    product_features = models.ManyToManyField('product.ProductFeature', through='OrderProductFeature')
    updated_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    status = models.CharField(choices=ORDER_STATUS,
                              max_length=20, default=ORDER_STATUS.wait)

    class Meta:
        ordering = ['created_at', 'user']

    @classmethod
    def create(cls, user, order_items):
        """

        :param user:
        :param order_items: list of OrderProductFeature
        :return:
        """
        order = cls.objects.create(user=user)
        price = 0
        for order_item in order_items:
            order_item.order = order
            price += order_item.product_feature.get_price_by_number(order_item.number)

        OrderProductFeature.objects.bulk_create(order_items)
        order.price = price
        order.save()
        return order

    def update(self, order_items):
        """
        :param order_items: list of OrderProductFeature
        :return:
        """
        with transaction.atomic():
            OrderProductFeature.objects.filter(order=self).delete()
            price = 0
            for order_item in order_items:
                order_item.order = self
                price += order_item.product_feature.get_price_by_number(order_item.number)

            OrderProductFeature.objects.bulk_create(order_items)
            self.price = price
            self.save()
            return self

    @property
    def order_items(self):
        return OrderProductFeature.objects.filter(order=self)

    @property
    def can_be_updated(self) -> bool:
        """
        user can update order?
        :return:
        """
        return self.status == ORDER_STATUS.wait


class OrderProductFeature(BaseModel):
    order = models.ForeignKey('Order')
    product_feature = models.ForeignKey('product.ProductFeature')
    number = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']




