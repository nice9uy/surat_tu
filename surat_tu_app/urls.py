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
    path('kabaranahan/<int:getIDdisosisi_kabaranahan>', views.kabaranahan, name='kabaranahan'),
    path('sekretariat/<int:getIDdisosisi_sekretariat>', views.sekretariat, name='sekretariat'),
    path('bagum/<int:getIDdisosisi_bagum>', views.bagum, name='bagum'),

    path('disposisi_kabadan/<int:pk>', views.disposisi_kabadan, name='disposisi_kabadan'),
]
