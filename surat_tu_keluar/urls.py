from django.urls import path
from . import views

urlpatterns = [
    path('surat_keluar/', views.surat_keluar, name='surat_keluar' ),

    # path('surat_keluar/tanggal_nota_dinas/', views.tanggal_nota_dinas, name='tanggal_nota_dinas' ),


    # path('surat_keluar/tambah_tanggal_nota_dinas/', views.tambah_tanggal_nota_dinas, name='tambah_tanggal_nota_dinas' ),
    # path('surat_keluar/tambah_detail_nota_dinas/', views.tambah_detail_nota_dinas, name='tambah_detail_nota_dinas' ),
    # path('surat_keluar/detail_nota_dinas/', views.detail_nota_dinas, name='detail_nota_dinas' ),


    path('surat_keluar/nota_dinas/', views.nota_dinas, name='nota_dinas' ),
    path('surat_keluar/olah_nota_dinas/', views.olah_nota_dinas, name='olah_nota_dinas' ),
    path('surat_keluar/bon_nomor/', views.bon_nomor, name='bon_nomor' ),

    path('surat_keluar/tambah_olah_nota_dinas/', views.tambah_olah_nota_dinas, name='tambah_olah_nota_dinas' ),
    path('surat_keluar/filter_olah_nota_dinas/', views.filter_olah_nota_dinas, name='filter_olah_nota_dinas' ),
    path('surat_keluar/filter_nota_dinas/', views.filter_nota_dinas, name='filter_nota_dinas' ),
    # path('surat_keluar/filter_bon_nomor/', views.filter_bon_nomor, name='filter_bon_nomor' ),
]