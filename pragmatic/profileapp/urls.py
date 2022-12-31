from django.contrib import admin
from django.urls import path

from .views import ProfileCreateView
from .views import ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', ProfileCreateView.as_view(), name = 'create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name = 'update'),
]