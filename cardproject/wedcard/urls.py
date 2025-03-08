from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(""              , views.home,        name="home"),
    # path("about/"        , views.about,       name="about"),
    path("update/"       , views.update,       name="update"),
    path("cards/"       , views.list_cards,       name="cards"),
    # path("contact/"      , views.contact,     name="contact"),
    # path("notice/"       , views.notice,       name="notice"),
    # path("news/"         , views.news,           name="news"),
    # path("remarks/"      , views.remarks,     name="remarks"),
    # path('card/<int:pk>/', views.detail,      name='detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
