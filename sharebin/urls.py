# Django Imports
from django.urls import path

# Local Imports
from . import views

app_name = "sharebin"

urlpatterns = [
    path('', views.add_or_edit_paste, name="add_or_edit_paste"),
    path('<uuid:paste_uuid>', views.add_or_edit_paste,
         name="add_or_edit_paste"),
    path('view/<uuid:paste_uuid>', views.view_paste,
         name="view_paste"),
    path('raw/<uuid:paste_uuid>', views.view_raw_paste,
         name="view_raw_paste"),
    path('download/<uuid:paste_uuid>', views.download_paste,
         name="download_paste"),
]