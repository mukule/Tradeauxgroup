from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import index, tender_details
from django.conf import settings
from django.conf.urls.static import static


app_name = 'tenders'
urlpatterns = [
    path('', index.as_view(), name='index'),
    path('<int:pk>', tender_details.as_view(), name='tender_details'),
    path('initiate_payment', views.initiate_payment, name='initiate_payment'),
    path('payment_push', views.payment_push, name='payment_push'),
    # path('payment_error', views.payment_error, name='payment_error'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)