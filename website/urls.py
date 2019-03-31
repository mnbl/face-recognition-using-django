from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login_redirect),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls')),
]
