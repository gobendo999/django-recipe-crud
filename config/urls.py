from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home import views
from vage.views import recaipe_list, delete_recipe, update_recipe


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('recaipe/', recaipe_list, name='recaipe_list'),

    path(
        'delete-recipe/<int:id>/',
        delete_recipe,
        name='delete_recipe'
    ),

    path(
        'update-recipe/<int:id>/',
        update_recipe,
        name='update_recipe'
    ),

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )