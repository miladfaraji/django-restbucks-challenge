from django.utils.translation import gettext as _

from rest_framework import generics, status, exceptions, mixins
from rest_framework.response import Response

from project.apps.order.consts import ORDER_STATUS
from project.apps.order.models import Order, OrderProductFeature
from project.apps.order.serializers import OrderSerializer, OrderCreateSerializer, CancelOrderSerializer
from project.apps.product.models import ProductFeature


class OrderListView(generics.ListAPIView, generics.CreateAPIView):
    """
    products List view
    """
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        product_features_id_list = [item['product_feature_id'] for item in serializer.validated_data['order_items']]
        product_features = ProductFeature.objects.filter(id__in=product_features_id_list)
        order_items = []
        for product_feature in product_features:
            for order_item in serializer.validated_data['order_items']:
                if order_item['product_feature_id'] == product_feature.id:
                    order_items.append(OrderProductFeature(product_feature=product_feature,
                                                           number=order_item['number']))
        return Order.create(user=self.request.user,
                            order_items=order_items)

    def create(self, request, *args, **kwargs):
        create_serializer = OrderCreateSerializer(data=request.data, context=self.get_content_negotiator())
        create_serializer.is_valid(raise_exception=True)
        order = self.perform_create(create_serializer)
        headers = self.get_success_headers(create_serializer.data)
        serializer = self.get_serializer(instance=order)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderView(generics.RetrieveAPIView, generics.UpdateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.request.user.orders.filter()

    def perform_update(self, serializer):
        order = self.get_object()
        if not order.can_be_updated:
            raise exceptions.ValidationError(_('You can not update this order'))

        product_features_id_list = [item['product_feature_id'] for item in serializer.validated_data['order_items']]
        product_features = ProductFeature.objects.filter(id__in=product_features_id_list)
        order_items = []
        for product_feature in product_features:
            for order_item in serializer.validated_data['order_items']:
                if order_item['product_feature_id'] == product_feature.id:
                    order_items.append(OrderProductFeature(product_feature=product_feature,
                                                           number=order_item['number']))
        return order.update(order_items=order_items)

    def put(self, request, *args, **kwargs):
        create_serializer = OrderCreateSerializer(data=request.data, context=self.get_content_negotiator())
        create_serializer.is_valid(raise_exception=True)
        order = self.perform_update(create_serializer)
        serializer = self.get_serializer(instance=order)
        return Response(serializer.data)



class CancelOrderView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = CancelOrderSerializer

    def get_queryset(self):
        return self.request.user.orders.filter()

    def post(self, request, *args, **kwargs):
        order = self.get_object()
        if not order.can_be_updated:
            raise exceptions.ValidationError(_('You can not cancel this order'))
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(status=ORDER_STATUS.cancel)





