from django.contrib import admin

from .models import Product, Feature, ProductFeature


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'feature', 'value', 'price')


admin.site.register(Product, ProductAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(ProductFeature, ProductFeatureAdmin)
