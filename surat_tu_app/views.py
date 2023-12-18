from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import DbSurat , DbKlasifikasi, DisposisiDb
from datetime import date

# Create your views here.
@login_required(login_url="/accounts/login/")
def home(request):

    # hari_ini = date.today()
    

    # print(hari_ini)

    datasemuasurat = DbSurat.objects.all()
    Klasifikasi    = DbKlasifikasi.objects.all().values_list('klasifikasi', flat=True )
    dispoKabadan   = DisposisiDb.objects.all()


    context = {
        'page_title'   : 'Home',
        'data_surat'   : datasemuasurat,
        'klasifikasi'  : Klasifikasi,
        'dispoKabadan' : dispoKabadan,
     }
    return render (request , 'pages/index.html' , context )
    

def tambah_surat(request):
    hari_ini = date.today()
    username = request.user
    klasifikasi    = DbKlasifikasi.objects.all().values_list('klasifikasi', flat=True )

    if request.method == 'POST':

        get_klasifikasi = request.POST.get('klasifikasi')
        # get_tanggal_agenda = request.POST.get('tanggal_agenda')
        get_no_agenda = request.POST.get('no_agenda')
        get_tanggal_surat = request.POST.get('tanggal_surat')
        get_no_surat = request.POST.get('no_surat')
        get_surat_dari = request.POST.get('surat_dari')
        get_perihal = request.POST.get('perihal')
        files_upload = request.FILES.get('file_name')

        tambah_data_surat = DbSurat(
            username    = username,
            klasifikasi = get_klasifikasi,
            tgl_agenda  = hari_ini,
            no_agenda   = get_no_agenda,
            tgl_surat   = get_tanggal_surat,
            no_surat    = get_no_surat,
            surat_dari  = get_surat_dari,
            perihal     = get_perihal,
            upload_file = files_upload
            
            )
        
        tambah_data_surat.save()

        return redirect('home')
    

    context = {
        'page_title' : 'Tambah Surat',
        'klasifikasi': klasifikasi
    }
    return render (request , 'pages/tambah_surat.html' , context )


def olah_surat(request) :
    datasemuasurat = DbSurat.objects.all()
    Klasifikasi    = DbKlasifikasi.objects.all().values_list('klasifikasi', flat=True )
    
    context = {
        'page_title' : 'Olah Surat',
        'data_surat' : datasemuasurat,
        'klasifikasi': Klasifikasi
    }
    
    return render (request , 'pages/olah_surat.html' , context )

def edit_olah_surat(request , id_edit_olah_surat ):
    username = request.user
    edit_olah_surat = get_object_or_404(DbSurat, pk = id_edit_olah_surat)

    if request.method == 'POST':

        get_klasifikasi = request.POST.get('klasifikasi')
        get_tgl_agenda  = request.POST.get('tanggal_agenda')          
        get_no_agenda = request.POST.get('no_agenda')
        get_tanggal_surat = request.POST.get('tanggal_surat')
        get_no_surat = request.POST.get('no_surat')
        get_surat_dari = request.POST.get('surat_dari')
        get_perihal = request.POST.get('perihal')
        files_upload = edit_olah_surat.upload_file.name

        edit_olah_surat = DbSurat(

            id          = id_edit_olah_surat,
            username    = str(username),
            klasifikasi = get_klasifikasi,
            tgl_agenda  = get_tgl_agenda,
            no_agenda   = get_no_agenda,
            tgl_surat   = get_tanggal_surat,
            no_surat    = get_no_surat,
            surat_dari  = get_surat_dari,
            perihal     = get_perihal,
            upload_file = files_upload
            
            )

        edit_olah_surat.save()
        return redirect('home')
    
    return render(request,'pages/olah_surat.html')

def delete_olah_surat(request , id_delete_olah_surat):
    delete_olah_surat = get_object_or_404(DbSurat, pk = id_delete_olah_surat)
    if request.method == 'POST':
        delete_olah_surat.upload_file.delete()
        delete_olah_surat.delete()
        return redirect('home')
    
    return render(request,'pages/olah_surat.html')


def disposisi(request ):
    disposisi = DisposisiDb.objects.all()
    context = {
        'disposisi' : disposisi
    }

    return render(request,'pages/disposisi.html' , context )


def olah_disposisi(request):
    disposisi = DisposisiDb.objects.all()

    if request.method == 'POST':

        get_klasifikasi = request.POST.get('klasifikasi')
        get_no_agenda = request.POST.get('no_agenda')
        get_tanggal_surat = request.POST.get('tanggal_surat')
        get_no_surat = request.POST.get('no_surat')
        get_surat_dari = request.POST.get('surat_dari')
        get_perihal = request.POST.get('perihal')
        files_upload = request.FILES.get('file_name')

        tambah_data_surat = DbSurat(
            # username    = username,
            klasifikasi = get_klasifikasi,
            # tgl_agenda  = hari_ini,
            no_agenda   = get_no_agenda,
            tgl_surat   = get_tanggal_surat,
            no_surat    = get_no_surat,
            surat_dari  = get_surat_dari,
            perihal     = get_perihal,
            upload_file = files_upload
            
            )
        
        tambah_data_surat.save()

        return redirect('home')



    context = {
        'disposisi' : disposisi
    }

    return render(request,'pages/olah_disposisi.html' , context )


def disposisi_kabadan(request):
    disposisi = "KABADAN"

    if request.method == 'POST':

        get_no_surat = request.POST.get('no_surat')
        get_tgl_agenda = request.POST.get('tgl_agenda')
        get_no_agenda = request.POST.get('no_agenda')
        get_catatan = request.POST.get('catatan')
        files_upload_disposisi = request.FILES.get('file_disposisi')

        disposisi_kabadan  = DisposisiDb (
            disposisi               = disposisi,
            no_surat                = get_no_surat,
            tgl_agenda              = get_tgl_agenda,
            no_agenda               = get_no_agenda,
            catatan                 = get_catatan,
            upload_file_disposisi   = files_upload_disposisi,
        
            )
        
        disposisi_kabadan.save()

        return redirect('disposisi')

    context = {
        'disposisi' : disposisi
    }

    return render(request,'pages/olah_disposisi.html' , context )

# def edit_disposisi_kabadan(request ):
#     disposisi = "KABADAN"
#     edit_disposisi_kabadan = get_object_or_404(DisposisiDb, pk = id_edit_disposisi_kabadan)

#     if request.method == 'POST':

#         get_no_surat = request.POST.get('no_surat')
#         get_tgl_agenda = request.POST.get('tgl_agenda')
#         get_no_agenda = request.POST.get('no_agenda')
#         get_catatan = request.POST.get('catatan')
#         files_upload_disposisi = request.FILES.get('file_disposisi')


#         edit_disposisi_kabadan  = DisposisiDb (
#             id                      = id_edit_disposisi_kabadan,
#             disposisi               = disposisi,
#             no_surat                = get_no_surat,
#             tgl_agenda              = get_tgl_agenda,
#             no_agenda               = get_no_agenda,
#             catatan                 = get_catatan,
#             upload_file_disposisi   = files_upload_disposisi,
        
#             )
        
#         edit_disposisi_kabadan.save()

#     context = {
#         'disposisi' : disposisi
#     }

#     return render(request,'pages/disposisi.html' , context )
