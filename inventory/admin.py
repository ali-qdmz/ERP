from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from inventory.models import WareHouse, WareHouseManager, Category, Item, SaleProducts, BuyProducts, Sale, Buy

from django.contrib import admin


# from adminfilters.models import Breed, Pet

# class BreedListFilter(admin.SimpleListFilter):
#     """
#     This filter is an example of how to combine two different Filters to work together.
#     """
#     # Human-readable title which will be displayed in the right admin sidebar just above the filter
#     # options.
#     title = 'انبار'
#
#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'warehouse'
#
#     # Custom attributes
#     related_filter_parameter = 'breed__species__id__exact'
#
#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         list_of_questions = []
#         queryset = Item.objects.order_by('id')
#         if self.related_filter_parameter in request.GET:
#             queryset = queryset.filter(id=request.GET[self.related_filter_parameter])
#         for breed in queryset:
#             list_of_questions.append(
#                 (str(breed.id), breed.warehouse)
#             )
#         return sorted(list_of_questions, key=lambda tp: tp[1])
#
#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value to decide how to filter the queryset.
#         if self.value():
#             return queryset.filter(id=self.value())
#         return queryset
#

@admin.register(Item)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'item_unit', 'orginal_price', 'category')
    list_filter = ('category','item_unit','warehouse','brand','model')


# Register your models here.
class WareHouseManagerInline(admin.TabularInline):
    model = WareHouseManager
    extra = 1


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class WareHouseAdmin(admin.ModelAdmin):
    model = WareHouse
    inlines = [WareHouseManagerInline]


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class ItemAdmin(admin.ModelAdmin):
    model = Item


class SaleProductsInline(admin.TabularInline):
    model = SaleProducts
    extra = 1


class SaleAdmin(admin.ModelAdmin):
    model = Sale
    inlines = [SaleProductsInline]


class BuyProductsInline(admin.TabularInline):
    model = BuyProducts
    extra = 1


class BuyAdmin(admin.ModelAdmin):
    model = Buy
    inlines = [BuyProductsInline]


class SaleProductsAdmin(admin.ModelAdmin):
    model = SaleProducts


class BuyProductsAdmin(admin.ModelAdmin):
    model = BuyProducts


admin.site.register(WareHouse, WareHouseAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Item, ItemAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Buy, BuyAdmin)
# admin.site.register(SaleProducts, SaleProductsAdmin)
# admin.site.register(BuyProducts, BuyProductsAdmin)
