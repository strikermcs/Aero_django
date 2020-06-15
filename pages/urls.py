from django.urls import path
from django.conf.urls.static import static
from . import views
from project import settings

urlpatterns = [
        path('', views.my_first_simple_view),
       
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
