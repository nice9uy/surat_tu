from django.urls import path
from . import views

urlpatterns = [
    path('surat_keluar/', views.surat_keluar, name='surat_keluar' ),

    path('surat_keluar/nota_dinas/', views.nota_dinas, name='nota_dinas' ),
    path('surat_keluar/nota_dinas/filter_nota_dinas/', views.filter_nota_dinas, name='filter_nota_dinas' ),

    ############ NOTA DINAS -> BON NOMOR ##########################################
    path('surat_keluar/nota_dinas/bon_nomor/', views.bon_nomor, name='bon_nomor' ),
    path('surat_keluar/nota_dinas/bon_nomor_isi_nota_dinas/<int:id_bon_nomor_isi_nota_dinas>/', views.bon_nomor_isi_nota_dinas, name='bon_nomor_isi_nota_dinas' ),
    path('surat_keluar/nota_dinas/filter_bon_nomor/', views.filter_bon_nomor, name='filter_bon_nomor' ),
    path('surat_keluar/nota_dinas/filter_bon_nomor_isi_nota_dinas/<int:id_filter_bon_nomor_isi_nota_dinas>/', views.filter_bon_nomor_isi_nota_dinas, name='filter_bon_nomor_isi_nota_dinas' ),
    path('surat_keluar/nota_dinas/bon_nomor_edit_bon_nomor/<int:id_bon_nomor_edit_bon_nomor>/', views.bon_nomor_edit_bon_nomor, name='bon_nomor_edit_bon_nomor' ),

 
    ############ NOTA DINAS -> Nomor Tersedia #####################################
    path('surat_keluar/nota_dinas/nomor_tersedia/', views.nomor_tersedia, name='nomor_tersedia' ),
    path('surat_keluar/nota_dinas/nomor_tersedia_bon_nomor/<int:id_nomor_tersedia_bon_nomor>/', views.nomor_tersedia_bon_nomor, name='nomor_tersedia_bon_nomor' ),
    path('surat_keluar/nota_dinas/nomor_tersedia_isi_nota_dinas/<int:id_nomor_tersedia_isi_nota_dinas>/', views.nomor_tersedia_isi_nota_dinas, name='nomor_tersedia_isi_nota_dinas' ),
    path('surat_keluar/nota_dinas/nomor_tersedia_tambah_nomor/', views.nomor_tersedia_tambah_nomor, name='nomor_tersedia_tambah_nomor' ),
    path('surat_keluar/nota_dinas/filter_nomor_tersedia/', views.filter_nomor_tersedia, name='filter_nomor_tersedia' ),
   
    path('surat_keluar/nota_dinas/filter_nomor_tersedia_bon_nomor/<int:id_filter_nomor_tersedia_bon_nomor>/', views.filter_nomor_tersedia_bon_nomor, name='filter_nomor_tersedia_bon_nomor' ),
    path('surat_keluar/nota_dinas/filter_nomor_tersedia_isi_nota_dinas/<int:id_filter_nomor_tersedia_isi_nota_dinas>/', views.filter_nomor_tersedia_isi_nota_dinas, name='filter_nomor_tersedia_isi_nota_dinas' ),
    path('surat_keluar/nota_dinas/filter_bon_nomor_edit_bon_nomor/<int:id_filter_bon_nomor_edit_bon_nomor>/', views.filter_bon_nomor_edit_bon_nomor, name='filter_bon_nomor_edit_bon_nomor' ),


    ############ NOTA DINAS -> Olah Nota DInas #####################################     
    path('surat_keluar/nota_dinas/edit_nota_dinas/', views.edit_nota_dinas, name='edit_nota_dinas' ),
    path('surat_keluar/nota_dinas/filter_edit_nota_dinas/', views.filter_edit_nota_dinas, name='filter_edit_nota_dinas' ),
    path('surat_keluar/nota_dinas/edit_nota_dinas_modal/<int:id_edit_nota_dinas_modal>/', views.edit_nota_dinas_modal, name='edit_nota_dinas_modal' ),
    path('surat_keluar/nota_dinas/filter_edit_nota_dinas_modal/<int:id_filter_edit_nota_dinas_modal>/', views.filter_edit_nota_dinas_modal, name='filter_edit_nota_dinas_modal' ),


   
]