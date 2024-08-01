# urls.py

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    # Include the i18n URL configuration
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('references_app.urls')),
    path(_('admin/'), admin.site.urls),
)
