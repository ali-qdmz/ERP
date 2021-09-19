from django.conf.urls import url
from django.urls import path
from project_management import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report, name='report'),
    path('population-chart/', views.time_chart, name='population-chart'),
    path('inventory/', views.inventory, name='inventory'),
    path('print_mto/', views.print_mto, name='print_mto'),
    path('print_mto_report/', views.print_report, name='print_mto'),
    path('gantt-chart/', views.gantt_chart, name='gantt-chart'),
    path('gantt-chart-data/', views.gantt_chart_data, name='gantt-chart-data'),
]