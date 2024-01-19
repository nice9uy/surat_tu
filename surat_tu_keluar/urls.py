from django.urls import path
from . import views

urlpatterns = [
    path('surat_keluar/', views.surat_keluar, name='surat_keluar' ),
]