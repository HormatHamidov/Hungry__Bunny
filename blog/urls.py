from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.urls import re_path as url
from rest_framework_simplejwt import views as jwt_views

from home.views import (
    faq_view,
    home_view,
    about_view,
    terms_view,
    menu_view,
    booking_view,
    contact_view,
    faq_view,
    paypal_view,
)

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path('about/', about_view, name='about'),
    path('menu/', menu_view, name='menu'),
    path('booking/', booking_view, name='booking'),
    path('contact/', contact_view, name='contact'),
    path('faq/', faq_view, name='faq'),
    path('paypal/', paypal_view, name='paypal'),
    path('terms/', terms_view, name='terms'),

    path('user/', include('user.urls')),
    path('articles/', include('article.urls', namespace='article')),
    
    
    path('api/post/', include('api.urls',namespace='post')),
    path('api/article/', include('article.api.urls')),
    path('api/account/', include('user.api.urls')),


    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
