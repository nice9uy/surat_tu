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


    path('disposisi_kabadan/', views.disposisi_kabadan, name='disposisi_kabadan'),
    # path('edit_disposisi_kabadan/<int:id_edit_disposisi_kabadan>', views.edit_disposisi_kabadan, name='edit_disposisi_kabadan'),
]
