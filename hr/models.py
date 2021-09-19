from django.db import models
from django.contrib.auth.models import User
from utility.models import UserProfile, UserProfileBaseModel
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels


# Create your models here.

class Employee(UserProfileBaseModel):
    class Meta:
        verbose_name = _('کارمند')
        verbose_name_plural = _('کارمندان')
    user = models.OneToOneField(User, verbose_name=_('کاربر '), related_name="Employee", blank=True, null=True, on_delete=models.CASCADE)
    personal_id = models.CharField(max_length=255, verbose_name=_('کد پرسنلی '), blank=True, null=True)
    fathers_name = models.CharField(max_length=255, verbose_name=_('نام پدر '), blank=True, null=True)
    mothers_name = models.CharField(max_length=255, verbose_name=_('نام مادر '), blank=True, null=True)
    home_district = models.CharField(max_length=255, verbose_name=_('منطقه ی منزل '), blank=True, null=True)
    # is_freedomfighter= models.CharField(max_length=32, choices=(('yes','yes'),('no','no')), blank=True)
    spouse_occupation = models.CharField(max_length=255, verbose_name=_('وضعیت تاهل '), blank=True, null=True)
    spouse_district = models.CharField(max_length=255, verbose_name=_('منطقه ی منزل همسر '), blank=True, null=True)
    religion = models.CharField(max_length=255, verbose_name=_('دین '), blank=True, null=True)
    date_joining =jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ پیوستن '), null=True)
    entry_designation = models.CharField(max_length=255, verbose_name=_('نقش هنگام ورود '), blank=True, null=True)
    entry_scale = models.CharField(max_length=255, verbose_name=_('مقیاس ورود '), blank=True, null=True)
    picture = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name=_('ورود '), blank=True, null=True)
    archive_status = models.CharField(max_length=32, verbose_name=_('وضعیت بایگانی '), choices=(('yes', 'yes'), ('no', 'no')), blank=True)
    status = models.CharField(max_length=32, verbose_name=_('وضعیت '), choices=(('active', 'active'), ('inactive', 'inactive')), blank=True)

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name

    def __str__(self):
        return self.user.username


class Children(models.Model):
    class Meta:
        verbose_name = _('فرزند')
        verbose_name_plural = _('فرزندان')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='Children', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_('نام '), blank=True, null=True)
    sex = models.CharField(max_length=32, verbose_name=_('جنسیت '), choices=(('مرد', 'مرد'), ('زن', 'زن'), ('دیگر', 'دیگر')),
                           blank=True)
    dob = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ تولد '), null=True)


class DisciplinaryAction(models.Model):
    class Meta:
        verbose_name = _('سو پیشینه')
        verbose_name_plural = _('سو پیشینه ها')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='DisciplinaryAction',
                                 on_delete=models.CASCADE)
    nature_offence = models.CharField(max_length=255, verbose_name=_('سو پیشینه '), blank=True, null=True)
    punishment = models.CharField(max_length=255, verbose_name=_('مجازات '), blank=True, null=True)
    date =jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ '), null=True)


class District(models.Model):
    class Meta:
        verbose_name = _('ناحیه')
        verbose_name_plural = _('ناحیه ها')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='District', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_('نام '), blank=True, null=True)
    status = models.CharField(max_length=32, verbose_name=_('وضعیت '), choices=(('active', 'active'), ('inactive', 'inactive')), blank=True)


class Education(models.Model):
    class Meta:
        verbose_name = _('تحصیلات')
        verbose_name_plural = _('تحصیلات ها')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='Education', on_delete=models.CASCADE)
    name_institution = models.CharField(max_length=255, verbose_name=_('نام موسسه '), blank=True, null=True)
    principals_subject = models.CharField(max_length=255, verbose_name=_('موضوعات اصلی '), blank=True, null=True)
    degree = models.CharField(max_length=255, verbose_name=_('درجه '), blank=True, null=True)
    year = models.CharField(max_length=255, verbose_name=_('سال '), blank=True, null=True)
    division = models.CharField(max_length=255, verbose_name=_('گرایش '), blank=True, null=True)


class Training(models.Model):
    class Meta:
        verbose_name = _('گواهی نامه')
        verbose_name_plural = _('گواهی نامه ها')
    employee = models.ForeignKey(Employee, blank=True, verbose_name=_('کارمند '), null=True, related_name='Training', on_delete=models.CASCADE)
    title_trainin = models.CharField(max_length=255, verbose_name=_('عنوان آموزش '), blank=True, null=True)
    institution = models.CharField(max_length=255, verbose_name=_('موسسه '), blank=True, null=True)
    date_from =jmodels.jDateTimeField(blank=True, verbose_name=_('از تازیخ '), null=True)
    date_to =jmodels.jDateTimeField(blank=True, verbose_name=_('تا تاریخ '), null=True)
    trining_type = models.CharField(max_length=32, verbose_name=_('نوع آموزش '), choices=(('داخلی', 'داخلی'), ('خارجی', 'خارجی')), blank=True)


class Languages(models.Model):
    class Meta:
        verbose_name = _('زبان')
        verbose_name_plural = _('زبان ها')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='Languages', on_delete=models.CASCADE)
    languages = models.CharField(max_length=255, verbose_name=_('زبان '), blank=True, null=True)
    read = models.CharField(max_length=255, verbose_name=_('خواندن '), blank=True, null=True)
    write = models.CharField(max_length=255, verbose_name=_('نوشتن '), blank=True, null=True)
    speak = models.CharField(max_length=255, verbose_name=_('مکالمه '), blank=True, null=True)


class Address(models.Model):
    class Meta:
        verbose_name = _('آدرس')
        verbose_name_plural = _('آدرس ها')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='Address', on_delete=models.CASCADE)
    road_village = models.CharField(max_length=255, verbose_name=_('خیابان '), blank=True, null=True)
    postoffice = models.CharField(max_length=255, verbose_name=_('اداره پست '), blank=True, null=True)
    post_code = models.CharField(max_length=255, verbose_name=_('کد پستی '), blank=True, null=True)
    flat_no = models.CharField(max_length=255, verbose_name=_('آپارتمان '), blank=True, null=True)
    police_station_thana = models.CharField(max_length=255, verbose_name=_('اداره ی پلیس '), blank=True, null=True)
    district = models.CharField(max_length=255, verbose_name=_('ناحیه '), blank=True, null=True)
    date_from =jmodels.jDateTimeField(blank=True, verbose_name=_('از تاریخ '), null=True)
    address_type = models.CharField(max_length=32, verbose_name=_('نوع آدرس '), choices=(('موقتی', 'موقتی'), ('دایمی', 'دایمی')),
                                    blank=True)


class Promotions(models.Model):
    class Meta:
        verbose_name = _('ارتقا')
        verbose_name_plural = _('ارتقا ها')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='Promotions', on_delete=models.CASCADE)
    date_promotion =jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ ارتقا '), null=True)
    designation = models.CharField(max_length=255, verbose_name=_('نقش '), blank=True, null=True)
    pay_scale = models.CharField(max_length=255, verbose_name=_('اشل حقوقی '), blank=True, null=True)
    nature_promotion = models.CharField(max_length=255, verbose_name=_('نوع ارتقا '), blank=True, null=True)


class Rest_of_recreation(models.Model):
    class Meta:
        verbose_name = _('کارمند')
        verbose_name_plural = _('کارمندان')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='Rest_of_recreation',
                                 on_delete=models.CASCADE)
    date_from =jmodels.jDateTimeField(blank=True, verbose_name=_('از تاریخ '), null=True)
    coming_date =jmodels.jDateTimeField(blank=True, verbose_name=_('تا تاریخ '), null=True)


class Retirement_year(models.Model):
    class Meta:
        verbose_name = _('تاریخ بازنشستگی')
        verbose_name_plural = _('تاریخ های بازنشستگی')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='Retirement_year',
                                 on_delete=models.CASCADE)
    year =jmodels.jDateTimeField(blank=True, verbose_name=_('سال '), null=True)
    date =jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ '), null=True)


class ServiceHistory(models.Model):
    class Meta:
        verbose_name = _('تاریخچه ی خدمت')
        verbose_name_plural = _('تاریخچه های خدمت')
    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name='ServiceHistory',
                                 on_delete=models.CASCADE)
    designation = models.CharField(max_length=255, verbose_name=_('نقش '), blank=True, null=True)
    office_name = models.CharField(max_length=255, verbose_name=_('ساعت اداری '), blank=True, null=True)
    section = models.CharField(max_length=255, verbose_name=_('بخش '), blank=True, null=True)
    date_from =jmodels.jDateTimeField(blank=True, verbose_name=_('از تاریخ '), null=True)


class Employee_Achievement(models.Model):
    class Meta:
        verbose_name = _('موفقیت کارمند')
        verbose_name_plural = _('موفقیت های کارمند')
    points_to = models.ForeignKey(Employee, verbose_name=_('امتیاز داده می شود به '), blank=True, null=True, related_name='EmployeeAchievement',
                                  on_delete=models.CASCADE)
    points_by = models.ForeignKey(Employee, verbose_name=_('امتیاز داده می شود با '), blank=True, null=True, related_name='ManagerAchievement',
                                  on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)
    no_of_units_completed = models.DecimalField(default="0.00", verbose_name=_('شماره واحد هایی که کامل کرده '), max_digits=12, decimal_places=2)
    points_on_unit_task = models.DecimalField(default="0.00", verbose_name=_('امتیاز واحد عملیات '), max_digits=12, decimal_places=2)
    total_units_points = models.DecimalField(default="0.00", verbose_name=_('جمع امتیازات '), max_digits=12, decimal_places=2)
    date_achivement =jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ موفقیت '), null=True)
