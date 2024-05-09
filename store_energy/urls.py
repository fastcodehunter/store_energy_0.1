from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import StoreView
from card.views import list_products,place_an_order

urlpatterns = [
    path('admin/',admin.site.urls,name='adminka'),
    path('',StoreView.as_view(),name='store'),
    path('page/<int:page>',StoreView.as_view(),name='store'),
    path('card/',list_products,name='card'),
    path('order/',place_an_order,name='place_an_order'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)