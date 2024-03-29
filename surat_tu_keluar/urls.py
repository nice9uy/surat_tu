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

    path('surat_masuk/nota_dinas/edit_nota_dinas_modal/export_ke_excel_nota_dinas/', views.export_ke_excel_nota_dinas, name='export_ke_excel_nota_dinas' ),
    path('surat_masuk/nota_dinas/edit_nota_dinas_modal/filter_export_ke_excel_nota_dinas/', views.filter_export_ke_excel_nota_dinas, name='filter_export_ke_excel_nota_dinas' ),

   
   ############################################################ BIASA #####################################################
    path('surat_keluar/biasa/', views.biasa, name='biasa' ),

    ### Untuk Bon Nomor ####################
    path('surat_keluar/biasa/bon_nomor/', views.biasa_bon_nomor, name='biasa_bon_nomor' ),
    path('surat_keluar/biasa/biasa_bon_nomor_edit_bon_nomor/<int:id_biasa_bon_nomor_edit_bon_nomor>/', views.biasa_bon_nomor_edit_bon_nomor, name='biasa_bon_nomor_edit_bon_nomor' ),
    path('surat_keluar/biasa/biasa_nomor_tersedia_isi_surat_biasa/<int:id_biasa_nomor_tersedia_isi_surat_biasa>/', views.biasa_nomor_tersedia_isi_surat_biasa, name='biasa_nomor_tersedia_isi_surat_biasa' ),

    path('surat_keluar/biasa/filter_bon_nomor/', views.filter_bon_nomor_surat_biasa, name='filter_bon_nomor_surat_biasa' ),
    path('surat_keluar/biasa/filter_surat_biasa_bon_nomor_edit_bon_nomor/<int:id_filter_surat_biasa_bon_nomor_edit_bon_nomor>/', views.filter_surat_biasa_bon_nomor_edit_bon_nomor, name='filter_surat_biasa_bon_nomor_edit_bon_nomor' ),
    path('surat_keluar/biasa/filter_surat_biasa_nomor_tersedia_isi_surat_biasa/<int:id_filter_surat_biasa_nomor_tersedia_isi_surat_biasa>/', views.filter_surat_biasa_nomor_tersedia_isi_surat_biasa, name='filter_surat_biasa_nomor_tersedia_isi_surat_biasa' ),

    ### Untuk No tersedia ##################
    
    path('surat_keluar/biasa/no_tersedia/', views.biasa_no_tersedia, name='biasa_no_tersedia' ),
    path('surat_keluar/biasa/surat_biasa_nomor_tersedia_isi_bon_nomor/<int:id_surat_biasa_nomor_tersedia_isi_bon_nomor>/', views.surat_biasa_nomor_tersedia_isi_bon_nomor, name='surat_biasa_nomor_tersedia_isi_bon_nomor' ),
    path('surat_keluar/biasa/surat_biasa_nomor_tersedia_isi_surat_biasa/<int:id_surat_biasa_nomor_tersedia_isi_surat_biasa>/', views.surat_biasa_nomor_tersedia_isi_surat_biasa, name='surat_biasa_nomor_tersedia_isi_surat_biasa' ),
    
    path('surat_keluar/biasa/filter_biasa_nomor_tersedia/', views.filter_biasa_nomor_tersedia, name='filter_biasa_nomor_tersedia' ),
    path('surat_keluar/biasa/filter_surat_biasa_nomor_tersedia_isi_bon_nomor/<int:id_filter_surat_biasa_nomor_tersedia_isi_bon_nomor>/', views.filter_surat_biasa_nomor_tersedia_isi_bon_nomor, name='filter_surat_biasa_nomor_tersedia_isi_bon_nomor' ),
    path('surat_keluar/biasa/filter_surat_biasa_nomor_tersedia_isi_surat_biasa/<int:id_filter_surat_biasa_nomor_tersedia_isi_surat_biasa>/', views.filter_surat_biasa_nomor_tersedia_isi_surat_biasa, name='filter_surat_biasa_nomor_tersedia_isi_surat_biasa' ),

    path('surat_keluar/biasa/surat_biasa_nomor_tersedia_tambah_nomor/', views.surat_biasa_nomor_tersedia_tambah_nomor, name='surat_biasa_nomor_tersedia_tambah_nomor' ),

    ### Untuk Edit Surat Biasa #############
    path('surat_keluar/biasa/edit_surat_biasa/', views.biasa_edit_surat_biasa, name='biasa_edit_surat_biasa' ),
    path('surat_keluar/biasa/edit_surat_biasa_edit_surat/<int:id_edit_surat_biasa_edit_surat>/', views.edit_surat_biasa_edit_surat, name='edit_surat_biasa_edit_surat' ),

    path('surat_keluar/biasa/filter_edit_surat_biasa/', views.filter_edit_surat_biasa, name='filter_edit_surat_biasa' ),
    path('surat_keluar/biasa/filter_edit_surat_biasa_edit_surat/<int:id_filter_edit_surat_biasa_edit_surat>/', views.filter_edit_surat_biasa_edit_surat, name='filter_edit_surat_biasa_edit_surat' ),

   



]