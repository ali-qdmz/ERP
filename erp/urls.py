"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from erp import settings

urlpatterns = [
		url(r'^$', TemplateView.as_view(template_name='home.html')),
		# path('admin/', admin.site.urls),
		url(r'^accounts/', include('allauth.urls')),
		url(r'^accounting/', include('accounting.urls')),
		url(r'^attendance/', include('attendance.urls')),
		url(r'^project_management/', include('project_management.urls')),
		url(r'^crm/', include('crm.urls')),
		url(r'^hr/', include('hr.urls')),
		url(r'^inventory/', include('inventory.urls')),
		url(r'^payroll/', include('payroll.urls')),
		url(r'^pos/', include('pos.urls')),
		url(r'^utility/', include('utility.urls')),
		#url(r'^restapp/', include('restapp.urls', namespace='restapp')),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    # If no prefix is given, use the default language
    prefix_default_language=False
)



admin.site.index_title = _('پنل کاربری')
admin.site.site_header = _('شیمی پژوهش صنعت تبریز')
admin.site.site_title = _('مدیر سایت من')