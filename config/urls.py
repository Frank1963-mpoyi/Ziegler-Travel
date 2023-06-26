from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('', include('logsheet.urls')),
    path('account/', include('account.urls')),
    # path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
] 
    
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)

if settings.DEBUG and settings.IS_ENV == 'DEV':

    import debug_toolbar

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
