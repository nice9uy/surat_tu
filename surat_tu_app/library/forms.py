from django import forms
from ..models import DisposisiDb


class DisposisiForm(forms.ModelForm):
    class Meta:
        model  = DisposisiDb
        fields = ['disposisi', 'no_surat','no_agenda' ,'upload_file_disposisi']


# class DbSuratForm(forms.ModelForm):
#     class Meta:
#         model  = DbSurat
#         fields = [ 'username' ,'klasifikasi',
#                   'tgl_agenda','no_agenda','tgl_surat',
#                   'no_surat','surat_dari','perihal','upload_file'
#                   ]