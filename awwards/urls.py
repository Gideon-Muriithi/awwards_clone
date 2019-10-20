from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^user/profile/$', views.profile, name='profile'),
    url(r'project/post/$',views.post_project,name='post_project'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)