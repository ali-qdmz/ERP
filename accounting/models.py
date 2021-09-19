from django.db import models
from utility.models import BaseModel, UserProfile
from hr.models import Employee
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels


# Create your models here.
class AccountYear(models.Model):
    class Meta:
        verbose_name = _('حساب سالانه')
        verbose_name_plural = _('حساب های سالانه')
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('نام '))
    start_date =jmodels.jDateTimeField(blank=True, null=True, verbose_name=_('تاریخ شروع '))
    end_date =jmodels.jDateTimeField(blank=True, null=True, verbose_name=_('تاریخ پایان '))
    slug = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('کد مرتبط '))
    def __str__(self):
        return self.name


"""
accont_choice =     Balance Sheet Accounts
        				         Assets
        				                Cash            
        				                Account Receiveable
        				                Equipment
        				                Inventory
        				                Prepaid Expenses
        				         Liablities
        				                Accounts Payable
        				                Accured Expenses
        				                Notes Payable  
        				                Unearned Revenue
        				                Deferred Taxes
        				         Owner's Equity   
        				               Capital
        				               Retained Earnings  
        				      Income Statements Accounts 
          				          Revenue 
          				               Income                 
          				          Expense
          				               Salaries
          				               Selling Expenses
          				               Depreciation
          				               Rent
          				               Interest Expense
"""


class AccountType(models.Model):  # chart of account
    class Meta:
        verbose_name = _('نوع حساب')
        verbose_name_plural = _('انواع حساب')
    parent_type = models.ForeignKey('self', blank=True, null=True, default=None, related_name='prev_item',
                                    on_delete=models.CASCADE,verbose_name=_('نوع حساب سازمانی '))
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('نام '))
    slug = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('کد '))

    def __str__(self):
        return self.name


class Ledger(models.Model):
    class Meta:
        verbose_name = _('دفتر کل')
        verbose_name_plural = _('دفتر کل')
    code = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('کد '))
    account_type = models.ForeignKey(AccountType, blank=True, null=True, on_delete=models.CASCADE,verbose_name=_('نوع حساب کاربری'))
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('نام '))
    description = models.TextField(blank=True, null=True,verbose_name=_('توضیحات '))
    total_debit = models.DecimalField(verbose_name=" : مقدار کل بدهی ", default="0.00", max_digits=12, decimal_places=2)
    total_credit = models.DecimalField(verbose_name="مقدار کل اعتبار ", default="0.00", max_digits=12, decimal_places=2)
    balance = models.DecimalField(verbose_name="مانده ", default="0.00", max_digits=12, decimal_places=2)
    last_update_date =jmodels.jDateTimeField(blank=True, null=True,verbose_name=_('آخرین بروز رسانی '))

    def __str__(self):
        return self.name


class Transaction(BaseModel):
    class Meta:
        verbose_name = _('مبادلات')
        verbose_name_plural = _('مبادلات')
    trnsaction_type = models.CharField(max_length=32, choices=(('General', 'General'), ('POS', 'POS')), blank=True,
                                       verbose_name=_('نوع میادله '))
    subject = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('موضوع '))
    ref_no = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('شماره مرجع '))
    account_year = models.ForeignKey(AccountYear, blank=True, null=True, on_delete=models.CASCADE,
                                     verbose_name=_('سال حساب کاربری '))
    voucher_no = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('شماره ی ووچر '))
    entry_date =jmodels.jDateTimeField(blank=True, null=True,verbose_name=_('تاریخ وررد '))
    post_status = models.CharField(max_length=32, choices=(('pending', 'pending'), ('posted', 'posted')), blank=True,verbose_name=_('وضعیت بعدی '))

    def __str__(self):
        return self.subject


class TransactionDetails(models.Model):
    transaction = models.ForeignKey(Transaction, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name=_('میادله :'))
    ledger = models.ForeignKey(Ledger, blank=True, null=True, on_delete=models.CASCADE,
                               verbose_name=_('شماره ردیف :'))
    account_holder = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE,
                                       verbose_name=_('صاحب حساب :'))
    description = models.TextField(blank=True, null=True,verbose_name=_('توضیحات :'))
    # quantity      = models.DecimalField(verbose_name="Quantity (Optional)",default="0.00",max_digits=12,decimal_places=2)
    # rate          = models.DecimalField(verbose_name="Rate (Optional)",default="0.00",max_digits=12,decimal_places=2)
    # amount        = models.DecimalField(verbose_name="Credit",default="0.00",max_digits=12,decimal_places=2)
    vat = models.DecimalField(verbose_name="مالیات بر ارزش افزوده :", default="0.00", max_digits=12, decimal_places=2)
    tax = models.DecimalField(verbose_name="مالیت :", default="0.00", max_digits=12, decimal_places=2)
    debit = models.DecimalField(verbose_name="بدهی :", default="0.00", max_digits=12, decimal_places=2)
    credit = models.DecimalField(verbose_name="اعتبار :", default="0.00", max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=255, blank=True, null=True,verbose_name="واحد پولی :")
    # entry_type     = models.CharField(max_length=32, choices=(('debit','debit'),('credit','credit')), blank=True)


class JournalEntry(models.Model):
    class Meta:
        verbose_name = _('(اصلاحی) ثبتهای اصلاحی دفتر')
        verbose_name_plural = _('(اصلاحی) ثبتهای اصلاحی دفتر')
    transaction = models.ForeignKey(Transaction, blank=True, null=True, on_delete=models.CASCADE,verbose_name="مبادله")
    ref_no = models.CharField(max_length=255, blank=True, null=True,verbose_name="شماره مرجع :")
    debit = models.DecimalField(verbose_name="بدهی :", default="0.00", max_digits=12, decimal_places=2)
    credit = models.DecimalField(verbose_name="اعتبار :", default="0.00", max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=255, blank=True, null=True,verbose_name="واحد پولی ")
    entry_date =jmodels.jDateTimeField(blank=True, null=True,verbose_name="تاریخ ورود :")

    def __str__(self):
        return self.transaction.subject
