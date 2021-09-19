from django.db import models
from utility.models import BaseModel, UserProfile
from utility.models import PredfinedPointsRule, TaskUnitsPointsBaseModel
from hr.models import Employee, Employee_Achievement
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from crm.models import Customer
from hr.models import Employee
from django.contrib.auth.models import Group
from inventory.models import Item
from django_jalali.db import models as jmodels


class Material(models.Model):
    class Meta:
        verbose_name = _('ماده خام')
        verbose_name_plural = _('مواد خام')

    material_no = models.CharField(max_length=255, verbose_name=_('شماره ماده خام '), blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name=_('توضیحات '), blank=True, null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    part_no = models.CharField(max_length=255, verbose_name=_('شماره قطعه '), blank=True, null=True)
    work_shop = models.CharField(max_length=255, verbose_name=_('کارگاه '), blank=True, null=True)

    def __str__(self):
        return str(self.material_no) + " :شماره ماده خام"


class Cutting(models.Model):
    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)

    class Meta:
        verbose_name = _('دستگاه برش')
        verbose_name_plural = _('دستگاه های برش ')
        ordering = ('-finish_planning',)

    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class TN50(models.Model):
    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)

    class Meta:
        verbose_name = _('دستگاه تراش (TN50)')
        verbose_name_plural = _('دستگاه های تراش (TN50)')
        ordering = ('-finish_planning',)

    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class TN71(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _('دستگاه تراش (TN71)')
        verbose_name_plural = _('دستگاه های تراش (TN71)')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class TPK90(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _('دستگاه تراش (TPK90)')
        verbose_name_plural = _('دستگاه های تراش (TPK90)')
        ordering = ('-finish_planning',)

    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class s100_rosi(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _('فرز روسی (s100)')
        verbose_name_plural = _('فرز های روسی (s100)')
        ordering = ('-finish_planning',)

    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class TP120(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _('دستگاه تراش (TP120)')
        verbose_name_plural = _('دستگاه های تراش (TP120)')
        ordering = ('-finish_planning',)

    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class UniversalFerez(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' دستگاه فرز یونیورسال')
        verbose_name_plural = _('دستگاه های فرز یونیورسال')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class VerticalFerez(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' دستگاه فرز عمودی')
        verbose_name_plural = _('دستگاه های فرز عمودی')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class Kharzani(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' دستگاه خارزنی')
        verbose_name_plural = _('دستگاه های خارزنی')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class Drilling(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' دستگاه دریل')
        verbose_name_plural = _('دستگاه های دریل')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class LathingCnc(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' دستگاه تراش CNC')
        verbose_name_plural = _('دستگاه های تراش CNC')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class Carousel(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' دستگاه کاروسل')
        verbose_name_plural = _('دستگاه های کاروسل')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class StaticBalancing(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' دستگاه بالانس استاتیکی')
        verbose_name_plural = _('دستگاه های بالانس استاتیکی')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class PreAssembling(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' پیش مونتاژ')
        verbose_name_plural = _('پیش مونتاژ ها')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class Welding(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' جوشکاری')
        verbose_name_plural = _('جوشکاری ها')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class Casting(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' ریخته گری')
        verbose_name_plural = _('ریخته گری ها')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class Assembling(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' مونتاژ')
        verbose_name_plural = _('مونتاژ ها')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class Painting(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' رنگرزی')
        verbose_name_plural = _('رنگرزی ها')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


class PackingDelivery(models.Model):

    part_code = models.CharField(max_length=255, verbose_name=_('کد قطعه '), blank=False, default=None)
    start_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع برنامه ریزی شده '), null=True)
    start_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان شروع واقعی '), null=True)
    finish_planning = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان برنامه ریزی شده '), null=True)
    finish_actual = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان پایان واقعی '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    measurment = models.CharField(max_length=255, verbose_name=_('اندازه گیری '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '), blank=True, null=True)
    operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    unit_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی واحد '), blank=True, null=True)
    operator_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی اپراتور '), blank=True,
                                     null=True)
    tool_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ابزار '), blank=True, null=True)
    energy_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی انرژی '), blank=True, null=True)
    transportation_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی حمل و نقل '), blank=True,
                                           null=True)
    hse_cost = models.CharField(default=0, max_length=255, verbose_name=_('هزینه ی ایمنی کار '), blank=True, null=True)
    total_cost = models.CharField(default=0, max_length=255, verbose_name=_('جمه هزینه '), blank=True, null=True)
    class Meta:
        verbose_name = _(' بسته بندی و تحویل')
        verbose_name_plural = _('بسته بندی و تحویل ها')
        ordering = ('-finish_planning',)
    def __str__(self):
        return self.start_planning.strftime("%Y/%m/%d %H:%M:%S") + " - " + self.finish_planning.strftime(
            "%Y/%m/%d %H:%M:%S")


# Create your models here.
class Project(TaskUnitsPointsBaseModel):
    class Meta:
        verbose_name = _('پروژه')
        verbose_name_plural = _('پروژه ها')
    name = models.CharField(max_length=255, verbose_name=_('نام '), blank=True, null=True)
    description = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)
    project_cost = models.DecimalField(default="0.00", verbose_name=_('هزینه ی پروژه '), max_digits=12,
                                       decimal_places=2)
    estimated_cost = models.DecimalField(default="0.00", verbose_name=_('هزینه ی تخمینی '), max_digits=12,
                                         decimal_places=2)
    actual_cost = models.DecimalField(default="0.00", verbose_name=_('هزینه ی واقعی '), max_digits=12, decimal_places=2)
    start_date = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ شروع '), null=True)
    end_date = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ پایان '), null=True)
    status = models.CharField(max_length=32, verbose_name=_('وضعیت '),
                              choices=(('منتظر پاسخ', 'منتظر پاسخ'), ('کامل شده', 'کامل شده')), blank=True)

    def __str__(self):
        return str(self.name)


class ProjectManager(models.Model):
    class Meta:
        verbose_name = _('مدیر پروژه')
        verbose_name_plural = _('مدیر های پروژه')

    project = models.ForeignKey(Project, verbose_name=_('پروژه '), blank=True, null=True, related_name='ProjectManage',
                                on_delete=models.CASCADE)
    project_manager = models.ForeignKey(Employee, verbose_name=_('مدیر پروژه '), blank=True, null=True,
                                        on_delete=models.CASCADE)
    start_date = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ شروع '), null=True)
    comments = models.TextField(blank=True, verbose_name=_('نظرات '), null=True)
    status = models.CharField(max_length=32, verbose_name=_('وضعیت '),
                              choices=(('فعال', 'فعال'), ('غیرفعال', 'غیرفعال')), blank=True)


class Task(BaseModel):
    class Meta:
        verbose_name = _('عملیات')
        verbose_name_plural = _('عملیات ها')

    project = models.ForeignKey(Project, verbose_name=_('پروژه '), blank=True, null=True, related_name='ProjectTask',
                                on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, verbose_name=_('محول شده به '), blank=True, null=True,
                                    on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)
    total_units_task = models.DecimalField(default="0.00", verbose_name=_('مجموع عملیات های واحد '), max_digits=12,
                                           decimal_places=2)
    estimated_time_duration = models.DecimalField(verbose_name="زمان تخمینی به ساعت", default="0.00",
                                                  max_digits=12, decimal_places=2)
    start_date = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ شروع '), null=True)
    start_time = models.TimeField(blank=True, verbose_name=_('زمان شروع '), null=True)
    end_date = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ پایان '), null=True)
    end_time = models.TimeField(blank=True, verbose_name=_('زمان پایان '), null=True)


class TaskPerformed(models.Model):
    class Meta:
        verbose_name = _('عملیات انجام شده')
        verbose_name_plural = _('عملیات های انجام شده')

    task = models.ForeignKey(Task, verbose_name=_('عملیات '), blank=True, null=True, on_delete=models.CASCADE)
    no_of_units_completed = models.DecimalField(default="0.00", verbose_name=_('تعداد واحد های کامل شده '),
                                                max_digits=12, decimal_places=2)
    percent_completion = models.DecimalField(default="0.00", verbose_name=_('درصد پیشرفت '), max_digits=12,
                                             decimal_places=2)
    total_task_time = models.DecimalField(verbose_name="مجموع زمان عملیات به ساعت", default="0.00", max_digits=12,
                                          decimal_places=2)
    comments = models.TextField(blank=True, verbose_name=_('نظرات '), null=True)
    start_date = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ شروع '), null=True)
    start_time = models.TimeField(blank=True, verbose_name=_('زمان شروع '), null=True)
    end_date = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ پایان '), null=True)
    end_time = models.TimeField(blank=True, verbose_name=_('زمان پایان '), null=True)


class TaskPerformedReport(models.Model):
    class Meta:
        verbose_name = _('گزارش عملیات انجام شده')
        verbose_name_plural = _('گزارش عملیات های انجام شده')

    taskperformed = models.ForeignKey(TaskPerformed, verbose_name=_('عملیات انجام شده '), blank=True, null=True,
                                      on_delete=models.CASCADE)
    project_manager = models.ForeignKey(UserProfile, verbose_name=_('مدیر پروزه '), blank=True, null=True,
                                        on_delete=models.CASCADE)
    employee_achievement = models.ForeignKey(Employee_Achievement, verbose_name=_('موفقیت کارمند '), blank=True,
                                             null=True, on_delete=models.CASCADE)
    comments = models.TextField(blank=True, verbose_name=_('نظرات '), null=True)
    status = models.CharField(max_length=32, verbose_name=_('وضعیت '),
                              choices=(('منتظر پاسخ', 'منتظر پاسخ'), ('کامل شده', 'کامل شده')), blank=True)


class OverTime(TaskUnitsPointsBaseModel):
    class Meta:
        verbose_name = _('اضافه کار')
        verbose_name_plural = _('اضافه کار ها')

    employee = models.ForeignKey(Employee, verbose_name=_('کارمند '), blank=True, null=True, related_name="OverTime",
                                 on_delete=models.CASCADE)
    overtime_manager = models.ForeignKey(Employee, verbose_name=_('مدیر اضافه کاری '), blank=True, null=True,
                                         related_name="OverTimeManager",
                                         on_delete=models.CASCADE)
    task = models.ForeignKey(Task, verbose_name=_('عملیات '), blank=True, null=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255, verbose_name=_('موضوع '), blank=True, null=True)
    description = models.TextField(blank=True, verbose_name=_('توضیحات '), null=True)
    date_from = jmodels.jDateTimeField(blank=True, verbose_name=_('از تاریخ '), null=True)
    time_from = models.TimeField(blank=True, verbose_name=_('از زمان '), null=True)
    date_to = jmodels.jDateTimeField(blank=True, verbose_name=_('تا تاریخ '), null=True)
    time_to = models.TimeField(blank=True, verbose_name=_('تا زمان '), null=True)
    total_in_hrs = models.CharField(max_length=255, verbose_name=_('مجموع به ساعت '), blank=True, null=True)
    rate_per_hour = models.DecimalField(default="0.00", verbose_name=_('میانگین نسبت به ساعت '), max_digits=12,
                                        decimal_places=2)
    total_cost = models.DecimalField(default="0.00", verbose_name=_('مجموع هزینه '), max_digits=12, decimal_places=2)
    comments = models.TextField(blank=True, verbose_name=_('نظرات '), null=True)
    status = models.CharField(max_length=32, verbose_name=_('وضعیت '),
                              choices=(('موافقت‌', 'موافقت‌'), ('رد كردن‌', 'رد كردن‌')), blank=True)


class Outsourcing(models.Model):
    class Meta:
        verbose_name = _(' برونسپاری')
        verbose_name_plural = _('برونسپاری ها')

    doc_code = models.CharField(max_length=255, verbose_name=_('کد مدرک '), blank=True,
                                null=True)
    project_name = models.CharField(max_length=255, verbose_name=_('نام پروژه '), blank=True,
                                    null=True)
    project_code = models.CharField(max_length=255, verbose_name=_('کد پروژه '), blank=True,
                                    null=True)
    date = jmodels.jDateTimeField(verbose_name=_('تاریخ '), blank=True, null=True)
    part_name = models.CharField(max_length=255, verbose_name=_('نام قطعه '), blank=True,
                                 null=True)
    sps_part = models.CharField(max_length=255, verbose_name=_('کد قطعه/فایل '), blank=True,
                                null=True)
    description = models.CharField(max_length=255, verbose_name=_('نام دستگاه '), blank=True,
                                   null=True)
    sp_code = models.CharField(max_length=255, verbose_name=_('کد پروژه فرعی '), blank=True,
                               null=True)
    qty = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True,
                           null=True)
    operation_desc = models.CharField(max_length=255, verbose_name=_('شرح عملیات '), blank=True,
                                      null=True)
    comments = models.CharField(max_length=255, verbose_name=_('ملاحظلات '), blank=True,
                                null=True)

    qc_operator_name = models.ForeignKey(Employee, verbose_name=_('نام اپراتور برنامه ریزی '), blank=True, null=True,
                                         on_delete=models.CASCADE)
    sc_approv_date = jmodels.jDateTimeField(verbose_name=_('تاریخ تایید برنامه ریزی '), blank=True, null=True)
    qc_approv = models.BooleanField(default=False, verbose_name=_('تایید کنترل کیفیت '))
    outsourcing_approv = models.BooleanField(default=False, verbose_name=_('تایید برونسپاری '))
    inv_approv = models.BooleanField(default=False, verbose_name=_('تایید انبار '))
    def __str__(self):
        return self.date.strftime("%Y/%m/%d %H:%M:%S")

class Casting_Model(models.Model):
    class Meta:
        verbose_name = _(' مدل ریخته گری')
        verbose_name_plural = _('مدل های ریخته گری')

    doc_code = models.CharField(max_length=255, verbose_name=_('کد مدرک '), blank=True,
                                null=True)
    review_num = models.CharField(max_length=255, verbose_name=_('شماره بازنگری '), blank=True,
                                  null=True)
    model_name = models.CharField(max_length=255, verbose_name=_('نام مدل '), blank=True,
                                  null=True)
    model_code = models.CharField(max_length=255, verbose_name=_('کد مدل '), blank=True,
                                  null=True)
    build_date = jmodels.jDateTimeField(verbose_name=_('تاریخ ساخت '), blank=True,
                                        null=True)
    builder = models.CharField(max_length=255, verbose_name=_('سازنده '), blank=True,
                               null=True)
    material = models.CharField(max_length=255, verbose_name=_('جنس ریخته '), blank=True,
                                null=True)
    model_mat = models.CharField(max_length=255, verbose_name=_('جنس مدل '), blank=True,
                                 null=True)
    sketch_num = models.CharField(max_length=255, verbose_name=_('شماره نقشه '), blank=True,
                                  null=True)
    usage = models.CharField(max_length=255, verbose_name=_('محل استفاده '), blank=True,
                             null=True)
    spec = models.CharField(max_length=255, verbose_name=_('دوره کنترل '), blank=True,
                            null=True)
    mixed_model = models.CharField(max_length=255, verbose_name=_('تعداد قطعات ترکیبی '), blank=True,
                                   null=True)
    core = models.CharField(max_length=255, verbose_name=_('تعداد قطعات ماهیچه '), blank=True,
                            null=True)
    cap = models.CharField(max_length=255, verbose_name=_('تعداد قطعات درپوش '), blank=True,
                           null=True)
    bed = models.CharField(max_length=255, verbose_name=_('تعداد قطعات بستر '), blank=True,
                           null=True)
    first_approv_model = models.BooleanField(default=False, verbose_name=_('تایید اولیه مدل '))
    first_approv_model_comments = models.CharField(max_length=255, verbose_name=_('توضیحات تایید اولیه مدل '),
                                                   blank=True,
                                                   null=True)
    first_approv_cast = models.BooleanField(default=False, verbose_name=_('تایید اولیه ریخته نمونه '))
    first_approv_cast_comments = models.CharField(max_length=255, verbose_name=_('توضیحات تایید اولیه ریخته نمونه '),
                                                  blank=True,
                                                  null=True)
    model_approver_name = models.CharField(max_length=255, verbose_name=_('نام تایید کننده مدل '), blank=True,
                                           null=True)
    cast_approver_name = models.CharField(max_length=255, verbose_name=_('نام تایید کننده ریخته نمونه '), blank=True,
                                          null=True)
    visual_quality = models.BooleanField(default=False, verbose_name=_('کیفیت ظاهری ریخته '))
    visual_quality_comments = models.CharField(max_length=255, verbose_name=_('توضیحات کیفیت ظاهری '), blank=True,
                                               null=True)

    dimensions_quality = models.BooleanField(default=False, verbose_name=_('کیفیت ابعادی ریخته '))
    dimensions_quality_comments = models.CharField(max_length=255, verbose_name=_('توضیحات کیفیت ابعادی '), blank=True,
                                                   null=True)

    machining_quality = models.BooleanField(default=False, verbose_name=_('کیفیت ماشین کاری ریخته '))
    machining_quality_comments = models.CharField(max_length=255, verbose_name=_('توضیحات کیفیت ماشین کاری '),
                                                  blank=True,
                                                  null=True)
    qc_approver_name = models.CharField(max_length=255, verbose_name=_('تایید کننده ی کنترل نمونه اولیه '), blank=True,
                                        null=True)

    final_approv = models.BooleanField(default=False, verbose_name=_('تایید نهایی '))
    machining_quality_comments = models.CharField(max_length=255, verbose_name=_('توضیحات تایید نهایی '), blank=True,
                                                  null=True)
    final_approver_name = models.CharField(max_length=255, verbose_name=_('تایید کننده ی کنترل نهایی '), blank=True,
                                           null=True)

    def __str__(self):
        return str(self.model_code)


class Agenda(models.Model):
    class Meta:
        verbose_name = _('دستور کار')
        verbose_name_plural = _('دستور کارها')

    customer_name = models.ForeignKey(Customer, verbose_name=_('نام مشتری '), blank=True, null=True,
                                      on_delete=models.CASCADE, related_name='DisciplinaryAction9')
    agenda_number = models.CharField(max_length=255, verbose_name=_('شماره دستور کار '), blank=True, null=True)
    # project_code = models.CharField(max_length=255, verbose_name=_('کد پروژه '), blank=True, null=True)
    status = models.CharField(max_length=32, verbose_name=_('وضعیت '),
                              choices=(('در جریان', 'در جریان'), ('خاتمه یافته‌', 'خاتمه یافته‌'), ('راکد', 'راکد'),),
                              blank=True, null=True)
    quiddity = models.CharField(max_length=32, verbose_name=_('ماهیت '),
                                choices=(('A', 'A'), ('B', 'B'), ('C', 'C'),),
                                blank=True, null=True)
    secondary_code = models.CharField(max_length=255, verbose_name=_('کد فرعی '), blank=True, null=True)
    # agenda_rowid = models.CharField(max_length=255, verbose_name=_('ردیف دستور کار '), blank=True, null=True)
    agenda_detail = models.TextField(blank=True, verbose_name=_('شرح دستور کار '), null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True, null=True)
    agenda_date = jmodels.jDateTimeField(blank=True, verbose_name='تاریخ صدور دستور کار', null=True)
    date_required = jmodels.jDateTimeField(blank=True, verbose_name='تاریخ نیاز', null=True)
    comments = models.CharField(max_length=255, verbose_name=_('توضیحات '), blank=True, null=True)
    production_site = models.CharField(max_length=255, verbose_name=_('سایت تولید '), blank=True, null=True)
    project_control_responsible = models.ForeignKey(Employee, verbose_name=_('مسئول کنترل پروژه '), blank=True,
                                                    null=True,
                                                    on_delete=models.CASCADE, related_name='DisciplinaryAction7')
    schedule_control_responsible = models.ForeignKey(Group, verbose_name=_('مسئول برنامه ریزی '), blank=True, null=True,
                                                     on_delete=models.CASCADE, related_name='DisciplinaryAction8')
    agenda_modification_date = jmodels.jDateTimeField(verbose_name=_('تاریخ اصلاح دستور کار '), blank=True,
                                                      null=True)
    modification_details = models.CharField(max_length=255, verbose_name=_('شرح اصلاحیه در صورت وجود '), blank=True,
                                            null=True)
    considerations = models.CharField(max_length=255, verbose_name=_('ملاحظات '), blank=True, null=True)

    design_team_code = models.ForeignKey(Group, max_length=32, verbose_name=_('کد تیم طراحی '), blank=True, null=True,
                                         on_delete=models.CASCADE, related_name='DisciplinaryAction5')
    scheduling_send_date = jmodels.jDateTimeField(blank=True, verbose_name='تاریخ ارسال به برنامه ریزی', null=True)
    project_engineering_person_code = models.ForeignKey(Employee, verbose_name='کد نفر مهندسی پروژه ',
                                                        blank=True, null=True,
                                                        on_delete=models.CASCADE, related_name='DisciplinaryAction6')
    design_document_predicted_time = jmodels.jDateTimeField(
        verbose_name=_('زمان پیش بینی شده تحویل مدارک طراحی '),
        blank=True, null=True)
    design_document_actual_time = jmodels.jDateTimeField(
        verbose_name=_('زمان واقعی تحویل مدارک طراحی '), blank=True,
        null=True)
    project_eng_document_predicted_time = jmodels.jDateTimeField(
        verbose_name=_(
            'زمان پیش بینی شده تحویل مدارک مهندسی پروژه '),
        blank=True, null=True)
    project_eng_document_actual_time = jmodels.jDateTimeField(
        verbose_name=_('زمان واقعی تحویل مدارک مهندسی پروژه '),
        blank=True, null=True)
    design_comments = models.CharField(max_length=255, verbose_name=_('توضیحات طراحی '), blank=True, null=True)
    project_eng_comments = models.CharField(max_length=255, verbose_name=_('توضیحات مهندسی پروژه '), blank=True,
                                            null=True)

    def __str__(self):
        return str(self.agenda_number)


class MTO_Headers(models.Model):
    class Meta:
        verbose_name = _('MTO')
        verbose_name_plural = _('ها MTO ')

    client = models.ForeignKey(Customer, verbose_name=_('خریدار/client '), blank=True, null=True,
                               related_name='DisciplinaryAction999', on_delete=models.CASCADE)

    form_code = models.CharField(max_length=255, verbose_name=_('کد فرم/ویراش '), blank=True,
                                 null=True)
    sp_code = models.CharField(max_length=255, verbose_name=_('کد پروژه فرعی '), blank=True,
                               null=True)
    machine_name = models.CharField(max_length=255, verbose_name=_('نام دستگاه '), blank=True,
                                    null=True)
    collection = models.CharField(max_length=255, verbose_name=_('نام مجموعه '), blank=True,
                                  null=True)
    agenda_number = models.ForeignKey(Agenda, verbose_name=_('شماره دستور کار '), blank=True,
                                      null=True, on_delete=models.CASCADE)

    # project_code = models.CharField(max_length=255, verbose_name=_('کد پروژه '), blank=True, null=True)
    # agenda_number_seperated = models.CharField(max_length=255, verbose_name=_('شماره دستور کار جدا '), blank=True, null=True)
    # agenda_rowid = models.CharField(max_length=255, verbose_name=_('ردیف دستور کار  '), blank=True, null=True)

    date = jmodels.jDateTimeField(blank=True, verbose_name=_('تاریخ تهیه '), null=True)

    doc_no = models.CharField(max_length=255, verbose_name=_('شماره مدرک '), blank=True,
                              null=True)
    producer = models.CharField(max_length=255, verbose_name=_('تهیه کننده '), blank=True,
                                null=True)
    verified_by = models.CharField(max_length=255, verbose_name=_('تایید کننده '), blank=True,
                                   null=True)
    machine_qdy = models.CharField(max_length=255, verbose_name=_('تعداد دستگاه '), blank=True,
                                   null=True)
    cut = models.CharField(max_length=255, verbose_name=_('اقلام برشی '), blank=True,
                           null=True)
    cast = models.CharField(max_length=255, verbose_name=_('اقلام ریخته '), blank=True,
                            null=True)
    std = models.CharField(max_length=255, verbose_name=_('اقلام استاندارد '), blank=True,
                           null=True)
    agenda_description = models.CharField(max_length=255, verbose_name=_('شرح دستور کار '), blank=True,
                                          null=True)
    serial_no = models.CharField(max_length=255, verbose_name=_('شماره سریال '), blank=True,
                                 null=True)

    def __str__(self):
        return str(self.agenda_number.agenda_number)


class PP(models.Model):
    class Meta:
        verbose_name = _('برنامه ریزی تولید')
        verbose_name_plural = _('برنامه ریزی تولید')

    mto_headers = models.ForeignKey(MTO_Headers, verbose_name=_('سربرگ '), blank=True, null=True,
                                    on_delete=models.CASCADE)
    sps_part = models.CharField(max_length=255, verbose_name=_('کد قطعه/فایل '), blank=True,
                                null=True)
    cutting = models.ManyToManyField(Cutting, verbose_name=_('برش '), default='', blank=True, null=True)
    tn50 = models.ManyToManyField(TN50, verbose_name=_('تراش (TN50) '), default='', blank=True, null=True)
    tn71 = models.ManyToManyField(TN71, verbose_name=_('تراش (TN71) '), default='', blank=True, null=True)
    tpk90 = models.ManyToManyField(TPK90, verbose_name=_('تراش (TPK90) '), default='', blank=True, null=True)
    s100_rosi = models.ManyToManyField(s100_rosi, verbose_name=_('فرز (s100) '), default='', blank=True, null=True)
    tp120 = models.ManyToManyField(TP120, verbose_name=_('تراش (TP120) '), default='', blank=True, null=True)
    universal_ferez = models.ManyToManyField(UniversalFerez, verbose_name=_('فرز یونیورسال '), default='', blank=True,
                                             null=True)
    vertical_ferez = models.ManyToManyField(VerticalFerez, verbose_name=_('فرز عمودی '), default='', blank=True,
                                            null=True)
    kharzani = models.ManyToManyField(Kharzani, verbose_name=_('خارزنی '), default='', blank=True, null=True)
    drilling = models.ManyToManyField(Drilling, verbose_name=_('دریل کاری '), default='', blank=True, null=True)
    lath_cnc = models.ManyToManyField(LathingCnc, verbose_name=_('تراش CNC '), default='', blank=True, null=True)
    carousel = models.ManyToManyField(Carousel, verbose_name=_('کاروسل '), default='', blank=True, null=True)
    static_balancing = models.ManyToManyField(StaticBalancing, verbose_name=_('بالانس استاتیکی '), default='',
                                              blank=True, null=True)
    pre_assembling = models.ManyToManyField(PreAssembling, verbose_name=_('پیش مونتاژ '), default='', blank=True,
                                            null=True)
    welding = models.ManyToManyField(Welding, verbose_name=_('جوشکاری '), default='', blank=True, null=True)
    assembly = models.ManyToManyField(Assembling, verbose_name=_('مونتاژ '), default='', blank=True, null=True)
    painting = models.ManyToManyField(Painting, verbose_name=_('رنگرزی '), default='', blank=True, null=True)
    packing_delivery = models.ManyToManyField(PackingDelivery, default='', blank=True,
                                              verbose_name=_('بسته بندی و تحویل '), null=True)
    outsourcing = models.ManyToManyField(Outsourcing, verbose_name=_('برونسپاری '), default='', blank=True, null=True)
    casting_model = models.ManyToManyField(Casting_Model, verbose_name=_('نیاز به مدل ریخته '), default='', blank=True,
                                           null=True)
    casting = models.ManyToManyField(Casting, verbose_name=_('ریخته گری '), default='', blank=True, null=True)

    def __str__(self):
        return self.sps_part


class MTO_Content(models.Model):
    class Meta:
        verbose_name = _('محتوای ام تی او')
        verbose_name_plural = _('محتوای ام تی او ها')

    mto_headers = models.ForeignKey(MTO_Headers, verbose_name=_('سربرگ '), blank=True, null=True,
                                    on_delete=models.CASCADE)
    part_name = models.CharField(max_length=255, verbose_name=_('نام قطعه '), blank=True,
                                 null=True)
    sps_part = models.CharField(max_length=255, verbose_name=_('کد قطعه/فایل '), blank=True,
                                null=True)
    ver = models.CharField(max_length=255, verbose_name=_('ویرایش '), blank=True,
                           null=True)
    material_type = models.CharField(max_length=32, verbose_name=_('نوع مواد '),
                                     choices=(('STD', 'STD'), ('CUT', 'CUT'), ('CAST', 'CAST')),
                                     blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name=_('شرح قطعه '), blank=True,
                                   null=True)
    material = models.CharField(max_length=255, verbose_name=_('جنس '), blank=True,
                                null=True)
    quantity = models.CharField(max_length=255, verbose_name=_('تعداد '), blank=True,
                                null=True)
    raw_material_dimension = models.CharField(max_length=255, verbose_name=_('ابعاد مواد خام '), blank=True,
                                              null=True)
    mass = models.CharField(max_length=255, verbose_name=_('وزن تقریبی '), blank=True,
                            null=True)
    remark = models.CharField(max_length=255, verbose_name=_('ملاحظات '), blank=True,
                              null=True)
    pdf = models.FileField(upload_to='pdf', blank=True, null=True)
    delivery_date = jmodels.jDateTimeField(blank=True, verbose_name=_('زمان تحویل به تولید '), null=True)
    available_sps = models.BooleanField(default=False, verbose_name=_('موجود در انبار '), null=True)
    builtin_buy = models.BooleanField(default=False, verbose_name=_('خرید اقلام ساختنی '), null=True)
    standard_buy = models.BooleanField(default=False, verbose_name=_('خرید استاندارد '), null=True)

    material_cost = models.CharField(max_length=255, verbose_name=_('بهای تمام شده مواد خام '), blank=True,
                                     null=True, default='0')
    pp = models.OneToOneField(PP, verbose_name=_('برنامه ریزی '), blank=True, null=True,
                              on_delete=models.CASCADE)
