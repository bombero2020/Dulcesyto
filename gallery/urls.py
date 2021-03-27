from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image'),
    path('image_gallery/', views.image_gallery, name='image_gallery'),
    path('delete_image/', views.delete_image, name='delete_image')
]
