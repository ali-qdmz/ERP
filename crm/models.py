from django.db import models
from django.contrib.auth.models import User
from utility.models import UserProfileBaseModel, BaseModel, BusinessType, AddressBaseModel
from django.utils.translation import gettext_lazy as _
from hr.models import Employee
from django_jalali.db import models as jmodels


# Create your models here.

class ShippingAddress(AddressBaseModel):
    class Meta:
        verbose_name = _('آدرس ترابری')
        verbose_name_plural = _('آدرس های ترابری')
    pass

    def __str__(self):
        return str(self.address1)


class BillingAddress(AddressBaseModel):
    class Meta:
        verbose_name = _('آدرس محل صدور صورت حساب')
        verbose_name_plural = _('آدرس های محل صدور صورت حساب')
    def __str__(self):
        return str(self.address1)

class Lead(UserProfileBaseModel):
    class Meta:
        verbose_name = _('مشتری احتمالی')
        verbose_name_plural = _('مشتری احتمالی')

    date_entry =jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ ورود '), null=True)
    archive_status = models.CharField(max_length=32, verbose_name=_('وضعیت بایگانی '),
                                      choices=(('yes', 'yes'), ('no', 'no')), blank=True)
    status = models.CharField(max_length=32, verbose_name=_('وضعیت '),
                              choices=(('active', 'active'), ('inactive', 'inactive')), blank=True)


class Customer(UserProfileBaseModel):
    class Meta:
        verbose_name = _('مشتری')
        verbose_name_plural = _('مشتری')

    customer_number = models.CharField(max_length=32, verbose_name=_('شماره مشتری '), blank=True)
    ShippingAddress = models.ForeignKey(ShippingAddress, verbose_name=_('آدرس ترابری '),
                                        related_name="CustomerShippingAddress", blank=True, null=True,
                                        on_delete=models.CASCADE)
    BillingAddress = models.ForeignKey(BillingAddress, verbose_name=_('آدرس محل صدور صورت حساب '),
                                       related_name="CustomerBillingAddress", blank=True, null=True,
                                       on_delete=models.CASCADE)
    date_joining =jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ پیوستن '), null=True)
    picture = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name=_('تصویر '), blank=True, null=True)
    archive_status = models.CharField(max_length=32, choices=(('yes', 'yes'), ('no', 'no')),
                                      verbose_name=_('وضعیت بایگانی '), blank=True)
    status = models.CharField(max_length=32, choices=(('active', 'active'), ('inactive', 'inactive')),
                              verbose_name=_('وضعیت '), blank=True)


    def __str__(self):
        return self.customer_number


class Supplier(UserProfileBaseModel):
    class Meta:
        verbose_name = _('کارپرداز')
        verbose_name_plural = _('کارپرداز')

    user = models.OneToOneField(User, verbose_name=_('کاربر '), related_name="Supplier", blank=True, null=True,
                                on_delete=models.CASCADE)
    ShippingAddress = models.ForeignKey(ShippingAddress, verbose_name=_('آدرس ترابری '),
                                        related_name="SupplierShippingAddress", blank=True, null=True,
                                        on_delete=models.CASCADE)
    BillingAddress = models.ForeignKey(BillingAddress, verbose_name=_('آدرس محل صدور صورت حساب '),
                                       related_name="SupplierBillingAddress", blank=True, null=True,
                                       on_delete=models.CASCADE)
    license_number = models.CharField(verbose_name=_("شماره پروانه "), max_length=127)
    business_type = models.ForeignKey(BusinessType, verbose_name=_('نوع بازرگانی '),
                                      related_name="SupplierBusinessType", blank=True, null=True,
                                      on_delete=models.CASCADE)

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name

    def __str__(self):
        return self.user.username
