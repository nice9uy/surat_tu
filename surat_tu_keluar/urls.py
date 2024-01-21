from django.urls import path
from . import views

urlpatterns = [
    path('surat_keluar/', views.surat_keluar, name='surat_keluar' ),
    path('surat_keluar/nota_dinas', views.nota_dinas, name='nota_dinas' ),
]