from django.urls import path
from . import views

urlpatterns = [
    path('surat_keluar/', views.surat_keluar, name='surat_keluar' ),

    path('surat_keluar/nota_dinas/', views.nota_dinas, name='nota_dinas' ),
    path('surat_keluar/tambah_nota_dinas/', views.tambah_nota_dinas, name='tambah_nota_dinas' ),
    path('surat_keluar/detail_nota_dinas/<int:id_nota_dinas>/', views.detail_nota_dinas, name='detail_nota_dinas' ),
]