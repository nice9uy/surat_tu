from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),

    path('surat_masuk', views.surat_masuk, name='surat_masuk' ),
    path("surat_masuk/tambah_surat/", views.tambah_surat, name="tambah_surat"),

    path("surat_masuk/olah_surat/", views.olah_surat, name="olah_surat"),
    path('surat_masuk/edit_olah_surat/<int:id_edit_olah_surat>', views.edit_olah_surat, name='edit_olah_surat'),
    path('surat_masuk/delete_olah_surat/<int:id_delete_olah_surat>', views.delete_olah_surat, name='delete_olah_surat'),
    
    path('surat_masuk/disposisi/', views.disposisi, name='disposisi'),

    path('surat_masuk/olah_disposisi/', views.olah_disposisi, name='olah_disposisi'),
    path('surat_masuk/olah_disposisi_edit/<int:id_edit_disposisi>', views.olah_disposisi_edit, name='olah_disposisi_edit'),
    path('surat_masuk/olah_disposisi_delete/<int:id_delete_disposisi>', views.olah_disposisi_delete, name='olah_disposisi_delete'),
    
    path('surat_masuk/kabaranahan/<int:getIDdisosisi_kabaranahan>', views.kabaranahan, name='kabaranahan'),
    path('surat_masuk/sekretariat/<int:getIDdisosisi_sekretariat>', views.sekretariat, name='sekretariat'),
    path('surat_masuk/bagum/<int:getIDdisosisi_bagum>', views.bagum, name='bagum'),

    path('surat_masuk/upload_disposisi/', views.upload_disposisi, name='upload_disposisi'),

    path('surat_masuk/filter_tanggal/', views.filter_tanggal, name='filter_tanggal'),
    path('surat_masuk/filter_tanggal_olah_surat/', views.filter_tanggal_olah_surat, name='filter_tanggal_olah_surat'),
    path('surat_masuk/generate_no_agenda/', views.generate_no_agenda, name='generate_no_agenda'),


    path('surat_masuk/laporan_harian/', views.laporan_harian, name='laporan_harian'),
]


