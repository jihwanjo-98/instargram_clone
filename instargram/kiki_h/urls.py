from django.urls import path
from kiki_h.views import Main_post, UploadFeed
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',Main_post.as_view(),name='main'),
    path('content/upload',UploadFeed.as_view())
]

urlpatterns +=static(settings.MEDIA_URL,
                     document_root=settings.MEDIA_ROOT)