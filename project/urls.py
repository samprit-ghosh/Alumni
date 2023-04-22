


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from APP import views  


# Register your models here.


admin.site.site_header="Samprit Admin"
admin.site.site_title ="Samprit Admin"








urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('json/', views.employee_json, name='employee_json'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
