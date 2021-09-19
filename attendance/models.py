from django.db import models
from utility.models import BaseModel,UserProfile
from hr.models import Employee
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels

# Create your models here.


class Attendance(models.Model):
	class Meta:
		verbose_name = _('حضور غیاب')
		verbose_name_plural = _('حضور غیاب')
	employee           = models.ForeignKey(Employee,verbose_name=_('کارمند '), blank=True, null=True,on_delete=models.CASCADE)
	enterance_date     =jmodels.jDateTimeField( blank=True,verbose_name=_('تاریخ ورود '), null=True)
	enterance_time     = models.TimeField( blank=True,verbose_name=_('زمان ورود '), null=True)
	deperature_date    =jmodels.jDateTimeField( blank=True,verbose_name=_('تاریخ خروج '), null=True)
	deperature_time    = models.TimeField( blank=True,verbose_name=_('زمان خروج '), null=True)
	entry_card_status  = models.CharField(max_length=32,verbose_name=_('وضعیت کارت ورود '), choices=(('accept','accept'),('deny','deny')), blank=True)
	comments           = models.TextField(blank=True,verbose_name=_('نظرات '), null=True)

class in_out_track(models.Model):
	class Meta:
		verbose_name = _('بررسی ورود خروج')
		verbose_name_plural = _('بررسی ورودها و خروج ها')
	atendance          = models.ForeignKey(Attendance, verbose_name=_('حضور '), blank=True, null=True,on_delete=models.CASCADE)
	time_occure        = models.TimeField( blank=True, verbose_name=_('زمان وقوع '), null=True)
	in_out             = models.CharField(max_length=32, verbose_name=_('ورود خروج '), choices=(('in','in'),('out','out')), blank=True)
	entry_card_status  = models.CharField(max_length=32, verbose_name=_('وضعیت کارت ورود '), choices=(('accept','accept'),('deny','deny')), blank=True)
	comments           = models.TextField(blank=True, verbose_name=_('نظرات '), null=True)


class LeaveApplication(models.Model):
	class Meta:
		verbose_name = _('درخواست خاتمه ی همکاری')
		verbose_name_plural = _('درخواست های خاتمه ی همکاری')
	employee           = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name="LeaveApplicant",on_delete=models.CASCADE)
	hr_manager         = models.ForeignKey(Employee, verbose_name=_('مدیر منابع انسانی '), blank=True, null=True,related_name="HRManagerProcess",on_delete=models.CASCADE)
	subject            = models.CharField(max_length=255, verbose_name=_('موضوع '), blank=True, null=True)
	description        = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)
	date_from          =jmodels.jDateTimeField( blank=True, verbose_name=_('از تاریخ '), null=True)
	time_from          = models.TimeField( blank=True, verbose_name=_('از زمان '), null=True)
	end_date           =jmodels.jDateTimeField( blank=True, verbose_name=_('تاریخ خاتمه '), null=True)
	end_time           = models.TimeField( blank=True, verbose_name=_('زمان خاتمه '), null=True)
	total_in_hrs       = models.CharField(max_length=255, verbose_name=_('مجموع زمان همکاری '), blank=True, null=True)
	comments           = models.TextField(blank=True, verbose_name=_('نظرات '), null=True)
	status             = models.CharField(max_length=32, verbose_name=_('وضعیت '), choices=(('approve','approve'),('reject','reject')), blank=True)

class LeaveApplicationDetails(models.Model):
	class Meta:
		verbose_name = _('جزییات درخواست خاتمه ی همکاری')
		verbose_name_plural = _('جزییات درخواست های خاتمه ی همکاری')
	leave_application    = models.ForeignKey(LeaveApplication, verbose_name=_('درخواست خروج از کار '), blank=True, null=True,related_name="LeaveApplicationDetails",on_delete=models.CASCADE)
	comment_by           = models.ForeignKey(Employee, verbose_name=_('نظر داده شده توسط '), blank=True, null=True,related_name="CommentBy",on_delete=models.CASCADE)
	comments             = models.TextField(blank=True, verbose_name=_('نظرات '), null=True)

class Leave(models.Model):
	class Meta:
		verbose_name = _('پایان همکاری')
		verbose_name_plural = _('پایان همکاری ها')
	leave_application   = models.ForeignKey(LeaveApplication, verbose_name=_('درخواست خروج '), blank=True, null=True,related_name="LeaveApplication",on_delete=models.CASCADE)
	leave_type          = models.CharField(max_length=32, verbose_name=_('نحوه ی قطع همکاری '), choices=(('Official','Official'),('Casual','Casual')), blank=True)
	date_from           =jmodels.jDateTimeField( blank=True, verbose_name=_('از تاریخ '), null=True)
	time_from           = models.TimeField( blank=True, verbose_name=_('از زمان '), null=True)
	end_date            =jmodels.jDateTimeField( blank=True, verbose_name=_('تاریخ خاتمه '), null=True)
	end_time            = models.TimeField( blank=True, verbose_name=_('زمان خاتمه '), null=True)
	total_in_hrs        = models.CharField(max_length=255, verbose_name=_('مجموه زمان همکاری '), blank=True, null=True)
	comments            = models.TextField(blank=True, verbose_name=_('نظرات '), null=True)
	status              = models.CharField(max_length=32, verbose_name=_('وضعیت '), choices=(('approve','approve'),('rejected','rejected')), blank=True)


