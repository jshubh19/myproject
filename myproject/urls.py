from django.conf.urls import url
from django.contrib import admin
from schedule import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^date/', views.curdate, name='curdate'),
    url(r'^time/(\d{1,2})', views.hoursahead, name='hoursahead'),
    url(r'^welcome/',views.input,name='input')
]
