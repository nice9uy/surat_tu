from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path("tambah_surat/", views.tambah_surat, name="tambah_surat"),

    path("olah_surat/", views.olah_surat, name="olah_surat"),
    path('edit_olah_surat/<int:id_edit_olah_surat>', views.edit_olah_surat, name='edit_olah_surat'),
    
]