from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(""              , views.base,        name="base"),
    # path("about/"        , views.about,       name="about"),
    path("update/"       , views.update,       name="update"),
    path("update1/"       , views.update1,       name="update1"),
    # path("contact/"      , views.contact,     name="contact"),
    # path("notice/"       , views.notice,       name="notice"),
    # path("news/"         , views.news,           name="news"),
    # path("remarks/"      , views.remarks,     name="remarks"),
    path('sample_view/'  , views.sample_view, name='sample_view'),
    path('card/<int:pk>/', views.detail,      name='detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
