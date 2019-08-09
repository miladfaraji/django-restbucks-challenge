from django.contrib import admin

from .models import Order, OrderProductFeature


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'price', 'created_at')
    list_filter = ('status', )


class OrderProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_feature', 'number', 'created_at')

    # def get_product(self):
    #     return self.pro


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProductFeature, OrderProductFeatureAdmin)

