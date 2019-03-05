from django.conf.urls import url, include
from django.contrib import admin
from schedule import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from . import views  #...import from current package

#for form processing
from schedule.views import contact,completed

#for media files.
from django.conf import settings
from django.views.static import serve

#for classbased views.
from schedule.views import Myview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^schedule/',include('schedule.urls')), #...include the webapps

    url(r'^date/', views.curdate, name='curdate'),

    url(r'^temp/',views.Temp, name='Temp'),

    url(r'^time/(\d{1,2})', views.hoursahead, name='hoursahead'),

    url(r'^welcome/',views.input, name='input'),

    url(r'^$',views.input,name='input'), #.... show the page directly

    url(r'^base/', views.inputb, name='inputb'),

    url(r'^cbview/$',Myview.as_view()), #classbased views url creation

    url(r'doctor/',views.data_fetch,name='data_fetch'),

    url(r'user/',views.user_registration,name='user_registarion'),
   # url(r'usercreated/',views.user_creation_succesfully, name='user_creation_successfully'),



    url(r'^contact/$',contact),
    url(r'^contact/completed/$',completed),

   # url(r'^contact/',views.contact,name='contact'),
    #url(r'^completed/',views.completed, name='completed')
]
# media files url setting
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns +=[
        url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT, }),
    ]




