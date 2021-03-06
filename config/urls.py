from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('profile/', include('profiles.urls')),
    path('settings/', include('settings.urls')),
    path('sales/', include('sales.urls')),
    path('leads/', include('leads.urls')),
    path('tasks/', include('tasks.urls')),
    path('teams/', include('teams.urls')),
    path('contacts/', include('contacts.urls')),
    path('customers/', include('customers.urls')),
    path('accounts/', include('accounts.urls')),
    path('opportunity/', include('opportunities.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('accounts-user/', include('allauth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
]
