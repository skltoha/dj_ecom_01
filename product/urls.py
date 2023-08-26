from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path("<int:productlink>", views.product, name='product'),
    path("__debug__/", include("debug_toolbar.urls")),
]

for app_name, app_config in settings.APP_MEDIA_CONFIG.items():
    if settings.DEBUG:
        urlpatterns += static(app_config['MEDIA_URL'], document_root=app_config['MEDIA_ROOT'])
