from django.urls import path
from user.views import Login, Join
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('join', Join.as_view(), name='join'),
]

urlpatterns +=static(settings.MEDIA_URL,
                     document_root=settings.MEDIA_ROOT)