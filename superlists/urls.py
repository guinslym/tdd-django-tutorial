from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^admin/', admin.site.urls),
]
