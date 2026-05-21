from django.contrib import admin
from .models import (Banner, Ingredient, Category, Product,
                     WhyPoint, Customer, FlashSaleItem, NavLink,
                     ProductShade, OfferBanner, BuyOneGetOne, ExclusiveKit)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'button_text', 'button_position', 'is_active', 'order']
    list_editable = ['button_position', 'is_active', 'order']

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'order']
    list_editable = ['order']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating', 'badge', 'is_active']
    list_editable = ['price', 'is_active']
    list_filter = ['badge', 'is_active', 'category']
    search_fields = ['name', 'description']

@admin.register(WhyPoint)
class WhyPointAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'stars', 'is_active']
    list_editable = ['is_active']

@admin.register(FlashSaleItem)
class FlashSaleItemAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'discount', 'original_price', 'sale_price', 'is_active']
    list_editable = ['is_active']

@admin.register(NavLink)
class NavLinkAdmin(admin.ModelAdmin):
    list_display = ['label', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']

@admin.register(OfferBanner)
class OfferBannerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_active', 'order']
    list_editable = ['is_active', 'order']

@admin.register(BuyOneGetOne)
class BuyOneGetOneAdmin(admin.ModelAdmin):
    list_display = ['name', 'offer_price', 'original_price', 'is_active']
    list_editable = ['is_active']

@admin.register(ExclusiveKit)
class ExclusiveKitAdmin(admin.ModelAdmin):
    list_display = ['name', 'offer_price', 'original_price', 'save_percent', 'is_active']
    list_editable = ['is_active']