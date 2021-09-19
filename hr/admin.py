from django.contrib import admin

# Register your models here.
from hr.models import Employee
from hr.models import Children, DisciplinaryAction, District, Education, Training
from hr.models import Languages, Address, Promotions, Rest_of_recreation, Retirement_year, ServiceHistory, \
    Employee_Achievement


class ChildrenInline(admin.TabularInline):
    model = Children
    extra = 1


class DisciplinaryActionInline(admin.TabularInline):
    model = DisciplinaryAction
    extra = 1


class DistrictInline(admin.TabularInline):
    model = District
    extra = 1


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class TrainingInline(admin.TabularInline):
    model = Training
    extra = 1


class LanguagesInline(admin.TabularInline):
    model = Languages
    extra = 1


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


class PromotionsInline(admin.TabularInline):
    model = Promotions
    extra = 1


class Rest_of_recreationInline(admin.TabularInline):
    model = Rest_of_recreation
    extra = 1


class Retirement_yearInline(admin.TabularInline):
    model = Retirement_year
    extra = 1


class ServiceHistoryInline(admin.TabularInline):
    model = ServiceHistory
    extra = 1


class Employee_AchievementInline(admin.TabularInline):
    model = Employee_Achievement
    fk_name = 'points_to'
    extra = 1


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    inlines = [ChildrenInline, DisciplinaryActionInline, DistrictInline,
               EducationInline, TrainingInline, LanguagesInline, AddressInline,
               PromotionsInline, Rest_of_recreationInline, Retirement_yearInline, ServiceHistoryInline,
               Employee_AchievementInline]


@admin.register(Employee)
class PetAdmin5989(admin.ModelAdmin):
    list_filter = ('religion', 'archive_status', 'gender', 'blood_group')
    list_display = ('personal_id', 'first_name', 'last_name',
                    'nationalid',
                    'cell_phone',
                    'about',
                    )

# admin.site.register(Employee, EmployeeAdmin)
