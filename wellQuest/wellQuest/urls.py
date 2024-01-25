from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cal_count/', include('cal_count.urls')),
    path('find_exercise/', include('find_exe.urls')),
    path('fitness_index/', include('fitness_index.urls')),
]
