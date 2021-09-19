from django.db import models
from hr.models import Employee
from utility.models import Unit, BaseModel
from crm.models import Supplier, Customer, ShippingAddress, BillingAddress
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels

class WareHouse(BaseModel):
    class Meta:
        verbose_name = _('انبار کالا')
        verbose_name_plural = _('انبار های کالا')

    code = models.CharField(verbose_name="کد :", max_length=255, blank=True, null=True)
    name = models.CharField(verbose_name="نام :", max_length=255, blank=True, null=True)
    location = models.CharField(verbose_name="موقعیت :", max_length=255, blank=True, null=True)
    date_start =jmodels.jDateTimeField(verbose_name="تاریخ شروع :", blank=True, null=True)
    date_end =jmodels.jDateTimeField(verbose_name="تاریخ پایان :", blank=True, null=True)
    status = models.CharField(verbose_name="وضعیت :", max_length=32,
                              choices=(('active', 'active'), ('inactive', 'inactive')), blank=True)

    def __str__(self):
        return self.name


class WareHouseManager(models.Model):
    class Meta:
        verbose_name = _('مدیریت انبار کالا')
        verbose_name_plural = _('مدیریت انبار کالا')

    warehouse = models.ForeignKey(WareHouse, verbose_name="انبار :", blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(Employee, verbose_name="مدیر :", blank=True, null=True, on_delete=models.CASCADE)
    appointed_date =jmodels.jDateTimeField(verbose_name="تاریخ قرارداد :", blank=True, null=True)
    date_end =jmodels.jDateTimeField(verbose_name="تاریخ پایان :", blank=True, null=True)
    status = models.CharField(verbose_name="وضعیت :", max_length=32,
                              choices=(('active', 'active'), ('inactive', 'inactive')), blank=True)


class Category(models.Model):
    class Meta:
        verbose_name = _('طبقه بندی')
        verbose_name_plural = _('طبقه بندی ها')

    parent_category = models.ForeignKey('self', verbose_name="دسته بندی سازمانی", blank=True, null=True, default=None,
                                        related_name='category_item', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="نام :", max_length=255, blank=True, null=True)
    description = models.TextField(verbose_name="توضیحات :", blank=True, null=True)
    slug = models.CharField(verbose_name="کد شماره صفحه :", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    class Meta:
        verbose_name = _('کالا')
        verbose_name_plural = _('کالاها')

    warehouse = models.ForeignKey(WareHouse, verbose_name="انبار :", blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="دسته بندی :", blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="نام :", blank=True, null=True)
    brand = models.CharField(max_length=255, verbose_name="برند :", blank=True, null=True)
    model = models.CharField(max_length=255, verbose_name="مدل :", blank=True, null=True)
    item_unit = models.ForeignKey(Unit, blank=True, verbose_name="واحد مربوط :", null=True, on_delete=models.CASCADE)
    item_quantity = models.DecimalField(default="0.00", max_digits=12, verbose_name="مقدار موجود :", decimal_places=2)
    orginal_price = models.DecimalField(default="0.00", verbose_name="قیمت اصلی :", max_digits=12, decimal_places=2)
    sale_price = models.DecimalField(default="0.00", verbose_name="قیمت فروش :", max_digits=12, decimal_places=2)
    date_added =jmodels.jDateTimeField(blank=True, verbose_name="تاریخ اضافه شدن :", null=True)
    slug = models.CharField(max_length=255, verbose_name="کد شماره صفحه :", blank=True, null=True)

    def __str__(self):
        return self.name


class Sale(BaseModel):
    customer = models.ForeignKey(Customer, verbose_name="مشتری :", blank=True, null=True, on_delete=models.CASCADE)
    seller = models.ForeignKey(Employee, verbose_name="فروشنده :", blank=True, null=True, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, verbose_name="آدرس ترابری :", blank=True, null=True,
                                         on_delete=models.CASCADE)
    billing_address = models.ForeignKey(BillingAddress, verbose_name="آدرس تنظیم صورت حساب :", blank=True, null=True,
                                        on_delete=models.CASCADE)
    status = models.CharField(max_length=32, verbose_name="وضعیت :", choices=(
        ('order_submitted', 'order_submitted'), ('shipping', 'shipping'), ('completed', 'completed'), ('back', 'back'),
        ('order_cancel', 'order_cancel')), blank=True)

    class Meta:
        verbose_name = _('فروش')
        verbose_name_plural = _('فروش ها')


class SaleProducts(models.Model):
    class Meta:
        verbose_name = _('فروش')
        verbose_name_plural = _('فروش ها')

    sale = models.ForeignKey(Sale, verbose_name="فروش :", blank=True, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name="نوع جنس :", blank=True, null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, verbose_name="واحد :", blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.DecimalField(default="0.00", verbose_name="مقدار :", max_digits=12, decimal_places=2)
    discount = models.DecimalField(default="0.00", verbose_name="تخفیف :", max_digits=12, decimal_places=2)
    tax = models.DecimalField(default="0.00", verbose_name="مالیات :", max_digits=12, decimal_places=2)
    date_added =jmodels.jDateTimeField(blank=True, verbose_name="تاریخ اضافه شدن :", null=True)
    slug = models.CharField(max_length=255, verbose_name="کد شماره صفحه :", blank=True, null=True)


class Buy(models.Model):
    class Meta:
        verbose_name = _('خرید')
        verbose_name_plural = _('خرید ها')

    customer = models.ForeignKey(Employee, verbose_name="مشتری :", blank=True, null=True, on_delete=models.CASCADE)
    seller = models.ForeignKey(Customer, verbose_name="فروشنده :", blank=True, null=True, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, verbose_name="آدرس ترابری :", blank=True, null=True,
                                         on_delete=models.CASCADE)
    billing_address = models.ForeignKey(BillingAddress, verbose_name="آدرس تنظیم صورت حساب :", blank=True, null=True,
                                        on_delete=models.CASCADE)
    status = models.CharField(max_length=32, verbose_name="وضعیت :", choices=(
        ('order_submitted', 'order_submitted'), ('shipping', 'shipping'), ('completed', 'completed'), ('back', 'back'),
        ('order_cancel', 'order_cancel')), blank=True)


class BuyProducts(models.Model):
    class Meta:
        verbose_name = _('خرید محصول')
        verbose_name_plural = _('خرید محصول ها')

    buy = models.ForeignKey(Buy, verbose_name="خرید :", blank=True, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name="نوع جنس :", blank=True, null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, verbose_name="واحد :", blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.DecimalField(default="0.00", verbose_name="مقدار :", max_digits=12, decimal_places=2)
    discount = models.DecimalField(default="0.00", verbose_name="تخفیف :", max_digits=12, decimal_places=2)
    tax = models.DecimalField(default="0.00", verbose_name="مالیات :", max_digits=12, decimal_places=2)
    date_added =jmodels.jDateTimeField(blank=True, verbose_name="تاریخ اضافه شدن :", null=True)
    slug = models.CharField(max_length=255, verbose_name="کد شماره صفحه :", blank=True, null=True)
