from django.urls import path
from . import views

urlpatterns = [
    path('surat_keluar/', views.surat_keluar, name='surat_keluar' ),

    path('surat_keluar/nota_dinas/', views.nota_dinas, name='nota_dinas' ),
    path('surat_keluar/olah_nota_dinas/', views.olah_nota_dinas, name='olah_nota_dinas' ),

    path('surat_keluar/bon_nomor/', views.bon_nomor, name='bon_nomor' ),
    path('surat_keluar/bon_nomor_halaman/', views.bon_nomor_halaman, name='bon_nomor_halaman' ),
    path('surat_keluar/bon_nomor_filter/', views.bon_nomor_filter, name='bon_nomor_filter' ),
    path('surat_keluar/filter_tanggal_bon_nomor/', views.filter_tanggal_bon_nomor, name='filter_tanggal_bon_nomor' ),
    path('surat_keluar/filter_tanggal_olah_nota_dinas/', views.filter_tanggal_olah_nota_dinas, name='filter_tanggal_olah_nota_dinas' ),

    
    
    path('surat_keluar/no_tersedia/', views.no_tersedia, name='no_tersedia' ),
    path('surat_keluar/filter_tanggal_no_tersedia/', views.filter_tanggal_no_tersedia, name='filter_tanggal_no_tersedia' ),

    path('surat_keluar/tambah_olah_nota_dinas/', views.tambah_olah_nota_dinas, name='tambah_olah_nota_dinas' ),


    path('surat_keluar/filter_nota_dinas/', views.filter_nota_dinas, name='filter_nota_dinas' ),


    path('surat_keluar/isi_nota_dinas/<int:id_isi_nota_dinas>/', views.isi_nota_dinas, name='isi_nota_dinas' ),


]