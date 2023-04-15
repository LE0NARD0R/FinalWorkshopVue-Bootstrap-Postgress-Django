from django.conf.urls import url
from carddeck import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r"^places$", views.PlacesApi),
    url(r"^places/([0-9]+)$", views.PlacesApi),

    url(r"^places/savefile", views.SaveFile),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
