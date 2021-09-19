import json

from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from utility.models import UserProfile, Company, CompanyBranch, PredfinedPointsRule
from project_management.models import Project, ProjectManager, Task, TaskPerformed, TaskPerformedReport, OverTime
from project_management.models import *
from django.contrib import admin
from . import models


# from hr.models import Employee_achievement


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class ProjectManagerInline(admin.TabularInline):
    model = ProjectManager
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [ProjectManagerInline, TaskInline]


class TaskPerformedReportInline(admin.TabularInline):
    model = TaskPerformedReport
    extra = 1


class TaskPerformedAdmin(admin.ModelAdmin):
    model = TaskPerformed
    inlines = [TaskPerformedReportInline]


class OverTimeAdmin(admin.ModelAdmin):
    model = OverTime


class MaterialAdmin(admin.ModelAdmin):
    model = Material


class MTO_Content_Inline(admin.TabularInline):
    model = MTO_Content
    extra = 0
    inlines = [MTO_Content]
    limited_fields_qc = (
    'part_name', 'sps_part', 'ver', 'material_type', 'description', 'material', 'quantity', 'raw_material_dimension',
    'mass', 'remark', 'pdf', 'delivery_date', 'material_cost')

    def get_readonly_fields(self, request, obj=None):
        return self.limited_fields_qc


@admin.register(MTO_Headers)
class MTO_HeadersAdmin(admin.ModelAdmin):
    list_display = ('agenda_number', 'sp_code', 'machine_name', 'collection', 'doc_no', 'serial_no')
    list_filter = ('producer', 'verified_by',)
    list_per_page = 10
    # search_fields = ['agenda_number__agenda_number', 'agenda_number', 'form_code', 'sp_code', 'machine_name',
    #                  'collection', 'doc_no', 'agenda_description', 'serial_no',
    #                  'agenda_number__customer_name__first_name',
    #                  'agenda_number__customer_name__last_name']

    search_fields = ['agenda_number__agenda_number', 'serial_no']

    model = MTO_Headers
    inlines = [MTO_Content_Inline]


@admin.register(Agenda)
class PetAdmin2(admin.ModelAdmin):
    list_display = ('customer_name', 'agenda_number', 'agenda_date', 'date_required',
                    'scheduling_send_date',
                    'design_document_predicted_time',
                    'design_document_actual_time',
                    'project_eng_document_predicted_time',
                    'project_eng_document_actual_time')
    list_filter = ('status', 'quiddity', 'production_site',
                   'project_control_responsible',
                   'schedule_control_responsible',
                   )
    search_fields = ['customer_name__first_name', 'customer_name__last_name',
                     'agenda_number', 'secondary_code',
                     'agenda_detail', 'considerations']


@admin.register(Cutting)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()
    list_per_page = 2
    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()
    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)


def get_readonly_fields(self, request, obj=None):
    if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
        return self.limited_fields_qc

    if request.user.groups.filter(name='مدیر تولید').exists():
        return self.limited_fields_pr

    if request.user.groups.filter(name='مدیر کل').exists():
        return self.limited_fields_admin

    return super().get_fieldsets(request, obj=obj)


@admin.register(TN50)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(TN71)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(TPK90)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(s100_rosi)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(TP120)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(UniversalFerez)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(VerticalFerez)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(Kharzani)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(Drilling)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(LathingCnc)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(Carousel)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(StaticBalancing)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(PreAssembling)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(Welding)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(Assembling)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(Painting)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(PackingDelivery)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


@admin.register(Casting)
class PetAdmin23(admin.ModelAdmin):
    list_display = ('start_planning', 'start_actual', 'finish_planning', 'finish_actual', 'qc_approv')
    list_filter = ('qc_approv', 'finish_actual', 'start_planning', 'part_code')
    search_fields = ['part_code', 'start_planning']
    readonly_fields_qc = ()  # whatever fields you have by default
    limited_fields_qc = ()

    readonly_fields_admin = ()  # whatever fields you have by default
    limited_fields_admin = ()

    readonly_fields_pr = ()  # whatever fields you have by default
    limited_fields_pr = ('start_planning', 'finish_planning', 'qc_approv',)

    # def get_readonly_fields(self, request, obj=None):
    #     if request.user.groups.filter(name='مدیر برنامه ریزی و کنترل کیفیت').exists():
    #         return self.limited_fields_qc
    #
    #     if request.user.groups.filter(name='مدیر تولید').exists():
    #         return self.limited_fields_pr
    #
    #     if request.user.groups.filter(name='مدیر کل').exists():
    #         return self.limited_fields_admin
    #
    #     return super().get_fieldsets(request, obj=obj)


# admin.site.register(Project, ProjectAdmin)
admin.site.register(TaskPerformed, TaskPerformedAdmin)
admin.site.register(OverTime, OverTimeAdmin)

admin.site.register(Material, MaterialAdmin)
# admin.site.register(Cutting, MaterialAdmin)
# admin.site.register(TN50, MaterialAdmin)
# admin.site.register(TN71, MaterialAdmin)
# admin.site.register(TPK90, MaterialAdmin)
# admin.site.register(s100_rosi, MaterialAdmin)
# admin.site.register(TP120, MaterialAdmin)
# admin.site.register(UniversalFerez, MaterialAdmin)
# admin.site.register(VerticalFerez, MaterialAdmin)
# admin.site.register(Kharzani, MaterialAdmin)
# admin.site.register(Drilling, MaterialAdmin)
# admin.site.register(LathingCnc, MaterialAdmin)
# admin.site.register(Carousel, MaterialAdmin)
# admin.site.register(StaticBalancing, MaterialAdmin)
# admin.site.register(PreAssembling, MaterialAdmin)
# admin.site.register(Welding, MaterialAdmin)
# admin.site.register(Assembling, MaterialAdmin)
# admin.site.register(Painting, MaterialAdmin)
# admin.site.register(PackingDelivery, MaterialAdmin)
admin.site.register(Outsourcing, MaterialAdmin)
admin.site.register(Casting_Model, MaterialAdmin)
# admin.site.register(PP, MaterialAdmin)
# admin.site.register(Casting, MaterialAdmin)
# admin.site.register(MTO_Headers, MaterialAdmin)

# admin.site.register(Agenda, MaterialAdmin)


from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from project_management.models import PP
from project_management.forms import MovieChangeListForm


class MovieChangeList(ChangeList):

    def __init__(self, request, model, list_display,
                 list_display_links, list_filter, date_hierarchy,
                 search_fields, list_select_related, list_per_page,
                 list_max_show_all, list_editable, model_admin):
        super(MovieChangeList, self).__init__(request, model,
                                              list_display, list_display_links, list_filter,
                                              date_hierarchy, search_fields, list_select_related,
                                              list_per_page, list_max_show_all, list_editable,
                                              model_admin)

        # these need to be defined here, and not in MovieAdmin
        self.list_display = ['cutting', 'tn50']
        self.list_display_links = ['cutting', 'tn50']
        self.list_editable = ['cutting', 'tn50']


class MovieAdmin(admin.ModelAdmin):

    def get_changelist(self, request, **kwargs):
        return MovieChangeList

    def get_changelist_form(self, request, **kwargs):
        return MovieChangeListForm


# admin.site.register(PP, MovieAdmin)


@admin.register(PP)
class ProductAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # y = form.base_fields["sps_part"].widget.attrs['class']
        # print(y)

        form = super().get_form(request, obj, **kwargs)
        form.base_fields["cutting"].queryset = Cutting.objects.filter(part_code=str(obj))
        form.base_fields["tn50"].queryset = TN50.objects.filter(part_code=str(obj))
        form.base_fields["tn71"].queryset = TN71.objects.filter(part_code=str(obj))
        form.base_fields["tpk90"].queryset = TPK90.objects.filter(part_code=str(obj))
        form.base_fields["s100_rosi"].queryset = s100_rosi.objects.filter(part_code=str(obj))
        form.base_fields["tp120"].queryset = TP120.objects.filter(part_code=str(obj))
        form.base_fields["universal_ferez"].queryset = UniversalFerez.objects.filter(part_code=str(obj))
        form.base_fields["vertical_ferez"].queryset = VerticalFerez.objects.filter(part_code=str(obj))
        form.base_fields["kharzani"].queryset = Kharzani.objects.filter(part_code=str(obj))
        form.base_fields["drilling"].queryset = Drilling.objects.filter(part_code=str(obj))
        form.base_fields["lath_cnc"].queryset = LathingCnc.objects.filter(part_code=str(obj))
        form.base_fields["carousel"].queryset = Carousel.objects.filter(part_code=str(obj))
        form.base_fields["static_balancing"].queryset = StaticBalancing.objects.filter(part_code=str(obj))
        form.base_fields["pre_assembling"].queryset = PreAssembling.objects.filter(part_code=str(obj))
        form.base_fields["welding"].queryset = Welding.objects.filter(part_code=str(obj))
        form.base_fields["assembly"].queryset = Assembling.objects.filter(part_code=str(obj))
        form.base_fields["painting"].queryset = Painting.objects.filter(part_code=str(obj))
        form.base_fields["packing_delivery"].queryset = PackingDelivery.objects.filter(part_code=str(obj))
        form.base_fields["outsourcing"].queryset = Outsourcing.objects.filter(sps_part=str(obj))
        form.base_fields["casting_model"].queryset = Casting_Model.objects.filter(model_code=str(obj))
        form.base_fields["casting"].queryset = Casting.objects.filter(part_code=str(obj))

        return form

    def get_queryset(self, request):
        print(request)
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(shop__owner=request.user)
