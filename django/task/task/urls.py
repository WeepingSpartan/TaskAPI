
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from account import views as account_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('',account_views.signup,name='home')

]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
