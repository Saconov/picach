from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
path('',views.loginUser,name='test'),
path('ssim',views.simple_upload,name='ssim'),
path('challenges/all',views.get_challenges,name='challenges_all'),
path('challenges/create',views.create_challenge,name='create_challenge'),
path('challenges/createImage',views.upload_image,name='upload_image'),
path('images/<int:image_id>',views.get_image,name='get_image'),
   
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
