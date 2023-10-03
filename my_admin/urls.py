from django.urls import path
# Create your views here.
from my_admin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('singup/',views.SignPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('',views.HomePage,name='home'),
    path('form/',views.FormPage,name='form'),
    path('jadval/',views.JadvalPage,name='jadval'),
    path('kasalik_turi/',views.KasalikPage,name='kasalik'),

    path('logout/', views.LogoutPage, name='logout'),
    path('api/', views.MyApiView.as_view(), name='api'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
