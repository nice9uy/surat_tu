from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login/")
def home(request):
    context = {
        'page_title' : 'Home'
    }
    return render (request , 'pages/index.html' , context )
    

def tambah_surat(request):
    username = request.user

    # dbSurat = DbSurat.objects.filter(id_user = id_username).values_list("nama_klasifikasi" , flat=True)
    # kelompok = KelompokSurat.objects.filter(id_user = id_username).values_list("nama_kelompok", flat=True)
   
    get_surat = request.POST.get('surat')
    get_klasifikasi = request.POST.get('klasifikasi')
    get_kelompok = request.POST.get('kelompok')
    get_tanggal = request.POST.get('tanggal')

    files_upload = request.FILES.get('file_name')
    files_name = str(files_upload).split(',')

    filename_list_count = len(files_name)
   
    # try:  
    #     no_surat = files_name[0]
    #     kepada = files_name[1]
    #     prihal = files_name[2] 
    #     prihal_surat = prihal[:-4]

    #     upload_data = DatabaseSurat(
    #         id_user     = id_username,
    #         username    = username,
    #         surat       = get_surat,
    #         klasifikasi = get_klasifikasi,
    #         kelompok    = get_kelompok,
    #         tgl         = get_tanggal,
    #         no_surat    = no_surat,
    #         kepada      = kepada,
    #         perihal     = prihal_surat,
    #         upload_file = files_upload,
    #         today       = hari_ini,
    #         tahun       = year,
    #     )
        
    # except Exception:
    #     pass
        
    # else:
    #     if filename_list_count == 3:
    #         upload_data.save()
    #         return redirect('home')
    #     else:
    #         messages.warning(request,'bzdbdbzdb')
    #         print("ada yang salah, cek lagi ")
        
    # context = {
    #     'page_title' : 'Tambah Data',
    #     'klasifikasi' : klasifikasi,
    #     'kelompok' : kelompok,
        
    # }


    
    context = {
        'page_title' : 'Tambah Surat'
    }
    return render (request , 'pages/tambah_surat.html' , context )


def olah_surat(request) :
    
    
    context = {
        'page_title' : 'Olah Surat'
    }
    
    return render (request , 'pages/olah_surat.html' , context )
