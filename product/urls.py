from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path("<int:productlink>", views.product, name='product'),
    path("<slug:product_slug>", views.productitem, name='productitem'),
    path("__debug__/", include("debug_toolbar.urls")),

    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/view/', views.view_cart, name='view_cart'),
    path('cart/merge/', views.merge_cart, name='merge_cart'),
]

for app_name, app_config in settings.APP_MEDIA_CONFIG.items():
    if settings.DEBUG:
        urlpatterns += static(app_config['MEDIA_URL'], document_root=app_config['MEDIA_ROOT'])
