from django.urls import include,path
from resume.views import ProfileUpload

urlpatterns = [
    path('profile/', ProfileUpload.as_view(), name='profile'),
]