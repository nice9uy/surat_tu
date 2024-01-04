from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path("tambah_surat/", views.tambah_surat, name="tambah_surat"),

    path("olah_surat/", views.olah_surat, name="olah_surat"),
    path('edit_olah_surat/<int:id_edit_olah_surat>', views.edit_olah_surat, name='edit_olah_surat'),
    path('delete_olah_surat/<int:id_delete_olah_surat>', views.delete_olah_surat, name='delete_olah_surat'),
    
    path('disposisi/', views.disposisi, name='disposisi'),

    path('olah_disposisi/', views.olah_disposisi, name='olah_disposisi'),
    path('olah_disposisi_edit/<int:id_edit_disposisi>', views.olah_disposisi_edit, name='olah_disposisi_edit'),
    path('olah_disposisi_delete/<int:id_delete_disposisi>', views.olah_disposisi_delete, name='olah_disposisi_delete'),
    
    path('kabaranahan/<int:getIDdisosisi_kabaranahan>', views.kabaranahan, name='kabaranahan'),
    path('sekretariat/<int:getIDdisosisi_sekretariat>', views.sekretariat, name='sekretariat'),
    path('bagum/<int:getIDdisosisi_bagum>', views.bagum, name='bagum'),

    # path('duplikasi_surat/', views.duplikasi_surat, name='duplikasi_surat'),

    # path('disposisi_ses/', views.disposisi_ses, name='disposisi_ses'),
    # path('disposisi_bagum/', views.disposisi_bagum, name='disposisi_bagum'),

    path('upload_disposisi/', views.upload_disposisi, name='upload_disposisi'),


    path('filter_tanggal/', views.filter_tanggal, name='filter_tanggal'),
    path('filter_tanggal_olah_surat/', views.filter_tanggal_olah_surat, name='filter_tanggal_olah_surat'),


    path('generate_no_agenda/', views.generate_no_agenda, name='generate_no_agenda'),

]


