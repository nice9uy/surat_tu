from django.urls import path
from . import views

urlpatterns = [
    path('surat_keluar/', views.surat_keluar, name='surat_keluar' ),

    path('surat_keluar/tanggal_nota_dinas/', views.tanggal_nota_dinas, name='tanggal_nota_dinas' ),


    path('surat_keluar/tambah_tanggal_nota_dinas/', views.tambah_tanggal_nota_dinas, name='tambah_tanggal_nota_dinas' ),
    path('surat_keluar/tambah_detail_nota_dinas/', views.tambah_detail_nota_dinas, name='tambah_detail_nota_dinas' ),
    path('surat_keluar/detail_nota_dinas/', views.detail_nota_dinas, name='detail_nota_dinas' ),

]