from django.conf import settings
from django.urls import path
from . import views
app_name = 'myapp'

from django.conf.urls.static import static

urlpatterns = [
    path('',views.demo,name='demo'),
    path('shop/<int:book_id>',views.detail,name='detail'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


