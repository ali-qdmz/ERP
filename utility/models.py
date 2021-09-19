from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from utility.country_codes import COUNTRY_CHOICES
from django_jalali.db import models as jmodels


# Create your models here.
class BaseModel(models.Model):
    class Meta:
        verbose_name = _('مدل اصلی')
        verbose_name_plural = _('مدل های اصلی')
    created_on = jmodels.jDateTimeField(auto_now_add=True, verbose_name=_('ایجاد شده در تاریخ '), null=True, blank=True)
    modified_on = jmodels.jDateTimeField(auto_now=True, verbose_name=_('تغییر داده شده در تاریخ '))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('ایجاد شده توسط '), related_name='%(class)s_createdby', null=True, blank=True,
                                   on_delete=models.CASCADE)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('تغییر داده شده توسط '), related_name='%(class)s_modifiedby', null=True,
                                    blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class AddressBaseModel(models.Model):
    class Meta:
        verbose_name = _('مدل اصلی آدرس')
        verbose_name_plural = _('مدل های اصلی آدرس')
    address1 = models.CharField(max_length=255, verbose_name=_('آدرس 1 '), blank=True, null=True)
    address2 = models.CharField(max_length=255, verbose_name=_('آدرس 2 '), blank=True, null=True)
    country = models.CharField(max_length=32, verbose_name=_('کشور '), choices=COUNTRY_CHOICES, blank=True)
    state = models.CharField(max_length=255, verbose_name=_('استان '), blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name=_('شهر '), blank=True, null=True)
    zip_code = models.CharField(max_length=255, verbose_name=_('کد پستی '), blank=True, null=True)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    class Meta:
        verbose_name = _('پروفایل کاربری')
        verbose_name_plural = _('پروفایل های کاربری')
    user = models.OneToOneField(User, related_name="profile", verbose_name=_('کاربر '), on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name=_('نام '), blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name=_('نام خانوادگی '), blank=True, null=True)
    gender = models.CharField(max_length=32, verbose_name=_('جنسیت '), choices=(('مرد', 'مرد'), ('زن', 'زن'), ('دیگر', 'دیگر')),
                              blank=True)
    date_of_birth = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ تولد '), null=True)
    nationalid = models.CharField(max_length=255, verbose_name=_('کد ملی '), blank=True, null=True)
    blood_group = models.CharField(max_length=255, verbose_name=_('گروه خونی '), blank=True, null=True)
    marital_status = models.CharField(max_length=255, verbose_name=_('وضعیت نظام وظیفه '), blank=True, null=True)
    name_spouse = models.CharField(max_length=255, verbose_name=_('نام همسر '), blank=True, null=True)
    email = models.CharField(max_length=255, verbose_name=_('ایمیل '), blank=True, null=True)
    cell_phone = models.CharField(max_length=255, verbose_name=_('شماره تلفن همراه '), blank=True, null=True)
    land_phone = models.CharField(max_length=255, verbose_name=_('شماره تلفن ثابت '), blank=True, null=True)
    country = models.CharField(max_length=32, verbose_name=_('کشور '), choices=COUNTRY_CHOICES, blank=True)
    state = models.CharField(max_length=255, verbose_name=_('استان '), blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name=_('شهر '), blank=True, null=True)
    zip_code = models.CharField(max_length=255, verbose_name=_('کدپستی '), blank=True, null=True)
    permanent_address = models.TextField(blank=True, verbose_name=_('آدرس دایمی '), null=True)
    about = models.TextField(blank=True, verbose_name=_('درباره '), null=True)
    contact_details = models.TextField(blank=True, verbose_name=_('جزییات اطلاعات تماس '), null=True)
    latitude = models.CharField(max_length=512, verbose_name=_('عرض جغرافیایی '), blank=True, null=True)
    longitude = models.CharField(max_length=512, verbose_name=_('طول جغرافیایی '), blank=True, null=True)

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name

    def __str__(self):
        return self.user.username


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class UserProfileBaseModel(models.Model):
    class Meta:
        verbose_name = _('مدل اصلی پروفایل کاربری')
        verbose_name_plural = _('مدل های اصلی پروفایل کاربری')
    first_name = models.CharField(max_length=255, verbose_name=_('نام '), blank=True, null=True)
    last_name = models.CharField(max_length=255, verbose_name=_('نام خانوادگی '), blank=True, null=True)
    gender = models.CharField(max_length=32, verbose_name=_('جنسیت '), choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')),
                              blank=True)
    date_of_birth = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ تولد '), null=True)
    nationalid = models.CharField(max_length=255, verbose_name=_('کئ ملی '), blank=True, null=True)
    blood_group = models.CharField(max_length=255, verbose_name=_('گروه خونی '), blank=True, null=True)
    marital_status = models.CharField(max_length=255, verbose_name=_('وضعیت نظام وظیفه '), blank=True, null=True)
    name_spouse = models.CharField(max_length=255, verbose_name=_('نام همسر '), blank=True, null=True)
    email = models.CharField(max_length=255, verbose_name=_('ایمیل '), blank=True, null=True)
    cell_phone = models.CharField(max_length=255, verbose_name=_('شماره تماس همراه '), blank=True, null=True)
    land_phone = models.CharField(max_length=255, verbose_name=_('شماره تماس ثابت '), blank=True, null=True)
    country = models.CharField(max_length=32, verbose_name=_('کشور '), choices=COUNTRY_CHOICES, blank=True)
    state = models.CharField(max_length=255, verbose_name=_('استان '), blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name=_('شهر '), blank=True, null=True)
    zip_code = models.CharField(max_length=255, verbose_name=_('کدپستی '), blank=True, null=True)
    permanent_address = models.TextField(blank=True, verbose_name=_('نام '), null=True)
    about = models.TextField(blank=True, verbose_name=_('درباره '), null=True)
    contact_details = models.TextField(blank=True, verbose_name=_('جزییات اطلاعات تماس '), null=True)
    latitude = models.CharField(max_length=512, verbose_name=_('عرض جغرافیایی '), blank=True, null=True)
    longitude = models.CharField(max_length=512, verbose_name=_('طول جغرافیایی '), blank=True, null=True)

    class Meta:
        abstract = True


class Company(models.Model):
    class Meta:
        verbose_name = _('کمپانی')
        verbose_name_plural = _('کمپانی ها')
    name = models.CharField(max_length=255, verbose_name=_('نام '), blank=True, null=True)
    description = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)
    email = models.CharField(max_length=255, verbose_name=_('ایمیل '), blank=True, null=True)
    cell_phone = models.CharField(max_length=255, verbose_name=_('شماره تلفن همراه '), blank=True, null=True)
    land_phone = models.CharField(max_length=255, verbose_name=_('شماره تلن ثابت '), blank=True, null=True)
    country = models.CharField(max_length=32, verbose_name=_('کشور '), choices=COUNTRY_CHOICES, blank=True)
    state = models.CharField(max_length=255, verbose_name=_('استان '), blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name=_('شهر '), blank=True, null=True)
    zip_code = models.CharField(max_length=255, verbose_name=_('کدپستی '), blank=True, null=True)
    about = models.TextField(blank=True, verbose_name=_('درباره '), null=True)
    contact_details = models.TextField(blank=True, verbose_name=_('اطلاعات تماس '), null=True)
    latitude = models.CharField(max_length=512, verbose_name=_('عرض جغرافیایی '), blank=True, null=True)
    longitude = models.CharField(max_length=512, verbose_name=_('طول جغرافیایی '), blank=True, null=True)
    year_established = jmodels.jDateTimeField(blank=True, verbose_name=_('سال تاسیس '), null=True)
    total_employees = models.CharField(max_length=255, verbose_name=_('تعداد کارمندان '), blank=True, null=True)
    business_type = models.CharField(max_length=255, verbose_name=_('نوع کسب و کار '), blank=True, null=True)
    main_products = models.CharField(max_length=255, verbose_name=_('تولیدات اصلی '), blank=True, null=True)
    total_annual_revenue = models.CharField(max_length=255, verbose_name=_('مجموع عایدی سالانه '), blank=True, null=True)
    url = models.CharField(max_length=255, verbose_name=_('لینک '), blank=True, null=True)
    social_link = models.CharField(max_length=255, verbose_name=_('شبکه ی اجتماعی '), blank=True, null=True)


class CompanyBranch(models.Model):
    class Meta:
        verbose_name = _('شاخه ی کمپانی')
        verbose_name_plural = _('شاخ های کمپانی')
    company = models.ForeignKey(Company, verbose_name=_('کمپانی '), blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_('نام '), blank=True, null=True)
    description = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)
    email = models.CharField(max_length=255, verbose_name=_('ایمیل '), blank=True, null=True)
    cell_phone = models.CharField(max_length=255, verbose_name=_('شماره تلفن همراه '), blank=True, null=True)
    land_phone = models.CharField(max_length=255, verbose_name=_('شمره تلفن ثابت '), blank=True, null=True)
    country = models.CharField(max_length=32, verbose_name=_('کشور '), choices=COUNTRY_CHOICES, blank=True)
    state = models.CharField(max_length=255, verbose_name=_('استان '), blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name=_('شهر '), blank=True, null=True)
    zip_code = models.CharField(max_length=255, verbose_name=_('کدپستی '), blank=True, null=True)
    about = models.TextField(blank=True, verbose_name=_('درباره '), null=True)
    contact_details = models.TextField(blank=True, verbose_name=_('جزییات اطلاعات تماس '), null=True)
    latitude = models.CharField(max_length=512, verbose_name=_('عرض جغرافیایی '), blank=True, null=True)
    longitude = models.CharField(max_length=512, verbose_name=_('طول جغرافیایی '), blank=True, null=True)
    year_established = jmodels.jDateTimeField(blank=True, verbose_name=_('سال تاسیس '), null=True)
    total_employees = models.CharField(max_length=255, verbose_name=_('تعداد کارمندان '), blank=True, null=True)
    business_type = models.CharField(max_length=255, verbose_name=_('نوع تجارت '), blank=True, null=True)
    main_products = models.CharField(max_length=255, verbose_name=_('محصولات اصلی '), blank=True, null=True)
    total_annual_revenue = models.CharField(max_length=255, verbose_name=_('سود خالص سالانه '), blank=True, null=True)
    url = models.CharField(max_length=255, verbose_name=_('لینک '), blank=True, null=True)
    social_link = models.CharField(max_length=255, verbose_name=_('لینک شبکه ی اجتماعی '), blank=True, null=True)


class PredfinedPointsRule(BaseModel):
    class Meta:
        verbose_name = _('قوانین امتیاز')
        verbose_name_plural = _('قوانین امتیازات')
    units_points = models.DecimalField(default="0.00", verbose_name=_('امتیاز واحد '), max_digits=12, decimal_places=2)
    task_description = models.TextField(blank=True, verbose_name=_('توضیحات عملیات '), null=True)
    comments = models.TextField(blank=True, verbose_name=_('نظرات '), null=True)


class TaskUnitsPointsBaseModel(models.Model):
    class Meta:
        verbose_name = _('امتیاز واحد عملیات')
        verbose_name_plural = _('امتیازات واحد عملیات')
    total_units_task = models.DecimalField(default="0.00", verbose_name=_('مجموع عملیات های واحد '), max_digits=12, decimal_places=2)
    unit_task_description = models.TextField(blank=True, verbose_name=_('توضیح عملیات واحد '), null=True)
    points_on_unit_task = models.DecimalField(default="0.00", verbose_name=_('امتیاز عملیات واحد '), max_digits=12, decimal_places=2)


class Unit(models.Model):
    class Meta:
        verbose_name = _('واحد')
        verbose_name_plural = _('واحد ها')
    name = models.CharField(max_length=255, verbose_name=_('نام '), blank=True, null=True)
    description = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)

    def __str__(self):
        return self.name


class BusinessType(models.Model):
    class Meta:
        verbose_name = _('نوع کسب و کار ')
        verbose_name_plural = _('نوع کسب و کار')
    name = models.CharField(max_length=255, verbose_name=_('نام '), blank=True, null=True)
    description = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)

    def __str__(self):
        return self.name


class Tax(models.Model):
    class Meta:
        verbose_name = _('مالیات')
        verbose_name_plural = _('مالیات ها')
    business_type = models.ForeignKey(BusinessType, verbose_name=_('نوع تجارت '), blank=True, null=True, related_name='TaxBusinessType',
                                      on_delete=models.CASCADE)
    tax = models.FloatField(verbose_name=_('مالیات '), blank=True, null=True)

    def __unicode__(self):
        return self.name


class Vat(models.Model):
    class Meta:
        verbose_name = _('مالیات بر ارزش افزوده')
        verbose_name_plural = _('مالیات ها بر ارزش افزوده')
    business_type = models.ForeignKey(BusinessType, verbose_name=_('نوع تجارت '), blank=True, null=True, related_name='VatBusinessType',
                                      on_delete=models.CASCADE)
    vat = models.FloatField(verbose_name="درصد مالیات بر ارزش افزوده", blank=True, null=True)

    def __unicode__(self):
        return str(self.vat)


class ScheduleBaseModel(models.Model):
    class Meta:
        verbose_name = _('مدل اصلی برنامه ریزی')
        verbose_name_plural = _('مدل های اصلی برنامه ریزی')
    subject = models.CharField(max_length=255, verbose_name=_('موضوع '), blank=True, null=True)
    description = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)
    date_from = jmodels.jDateTimeField(blank=True, verbose_name=_('از تاریخ '), null=True)
    time_from = models.TimeField(blank=True, verbose_name=_('از زمان '), null=True)
    date_to = jmodels.jDateTimeField(blank=True, verbose_name=_('تا تاریخ '), null=True)
    time_to = models.TimeField(blank=True, verbose_name=_('تا زمان '), null=True)
