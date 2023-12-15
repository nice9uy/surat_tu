from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import DbSurat , DbKlasifikasi
from datetime import date

# Create your views here.
@login_required(login_url="/accounts/login/")
def home(request):

    hari_ini = date.today()
    

    print(hari_ini)

    datasemuasurat = DbSurat.objects.all()
    Klasifikasi    = DbKlasifikasi.objects.all().values_list('klasifikasi', flat=True )

    context = {
        'page_title' : 'Home',
        'data_surat' : datasemuasurat,
        'klasifikasi': Klasifikasi
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

def edit_olah_surat(request):
    pass


    # return render (request , 'pages/olah_surat.html' , context )
