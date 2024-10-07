from django.contrib import admin
from django.urls import path, include
from . import swagger
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('', include('product.urls')),
    path('', include('decor.urls')),
    path('', include('basket.urls')),
    path('', include('wedding.urls')),
<<<<<<< HEAD
    path('',include('admin_part.urls')),
]
urlpatterns += swagger.urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('', include('sets.urls')),
]
urlpatterns += swagger.urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> origin/kamila
