from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import DbSurat , DbKlasifikasi, DisposisiDb
from datetime import date
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .library.forms import DisposisiForm


def kabaranahan(request, getIDdisosisi_kabaranahan ):
    # dbDisposisi = DisposisiDb.objects.filter(id).values()
    getIDdisposisi = get_object_or_404(DbSurat, pk = getIDdisosisi_kabaranahan)
    template = get_template('pdf_disposisi/kabaranahan.html')

    no_agenda   = getIDdisposisi.no_agenda
    tgl_agenda  = getIDdisposisi.tgl_agenda
    surat_dari = getIDdisposisi.surat_dari
    no_surat   = getIDdisposisi.no_surat
    tgl_surat  = getIDdisposisi.tgl_surat
    klasifikasi = getIDdisposisi.klasifikasi

    html_content = template.render({
        'no_agenda'       : no_agenda,
        'tgl_agenda'      : tgl_agenda,
        'surat_dari'      : surat_dari,
        'no_surat'        : no_surat,
        'tgl_surat'       : tgl_surat,
        'klasifikasi'     : klasifikasi
    })

    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="people_report.pdf"'
    return response

def sekretariat(request, getIDdisosisi_sekretariat):
    getIDdisposisi = get_object_or_404(DbSurat, pk = getIDdisosisi_sekretariat)
    template = get_template('pdf_disposisi/sekretariat.html')

    no_agenda   = getIDdisposisi.no_agenda
    tgl_agenda  = getIDdisposisi.tgl_agenda
    surat_dari = getIDdisposisi.surat_dari
    no_surat   = getIDdisposisi.no_surat
    tgl_surat  = getIDdisposisi.tgl_surat
    klasifikasi = getIDdisposisi.klasifikasi
 

    html_content = template.render({
        'no_agenda'       : no_agenda,
        'tgl_agenda'      : tgl_agenda,
        'surat_dari'      : surat_dari,
        'no_surat'        : no_surat,
        'tgl_surat'       : tgl_surat,
        'klasifikasi'     : klasifikasi
    })

    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="people_report.pdf"'
    return response

def bagum(request , getIDdisosisi_bagum):
    getIDdisposisi = get_object_or_404(DbSurat, pk = getIDdisosisi_bagum)
    template = get_template('pdf_disposisi/bagum.html')

    no_agenda   = getIDdisposisi.no_agenda
    tgl_agenda  = getIDdisposisi.tgl_agenda
    surat_dari = getIDdisposisi.surat_dari
    no_surat   = getIDdisposisi.no_surat
    tgl_surat  = getIDdisposisi.tgl_surat
    klasifikasi = getIDdisposisi.klasifikasi

    html_content = template.render({
        'no_agenda'       : no_agenda,
        'tgl_agenda'      : tgl_agenda,
        'surat_dari'      : surat_dari,
        'no_surat'        : no_surat,
        'tgl_surat'       : tgl_surat,
        'klasifikasi'     : klasifikasi
    })

    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="people_report.pdf"'
    return response


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

    # hari_ini = date.today()
    username = request.user
    klasifikasi    = DbKlasifikasi.objects.all().values_list('klasifikasi', flat=True )

    if request.method == 'POST':

        get_klasifikasi = request.POST.get('klasifikasi')
        get_tanggal_agenda = request.POST.get('tanggal_agenda')
        get_no_agenda = request.POST.get('no_agenda')
        get_tanggal_surat = request.POST.get('tanggal_surat')
        get_no_surat = request.POST.get('no_surat')
        get_surat_dari = request.POST.get('surat_dari')
        get_perihal = request.POST.get('perihal')
        files_upload = request.FILES.get('file_name')

        tambah_data_surat = DbSurat(
            username    = username,
            klasifikasi = get_klasifikasi,
            tgl_agenda  = get_tanggal_agenda,
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

    # if request.method == 'POST':

    #     get_klasifikasi = request.POST.get('klasifikasi')
    #     get_no_agenda = request.POST.get('no_agenda')
    #     get_tanggal_surat = request.POST.get('tanggal_surat')
    #     get_no_surat = request.POST.get('no_surat')
    #     get_surat_dari = request.POST.get('surat_dari')
    #     get_perihal = request.POST.get('perihal')
    #     files_upload = request.FILES.get('file_name')

    #     tambah_data_surat = DbSurat(
    #         # username    = username,
    #         klasifikasi = get_klasifikasi,
    #         # tgl_agenda  = hari_ini,
    #         no_agenda   = get_no_agenda,
    #         tgl_surat   = get_tanggal_surat,
    #         no_surat    = get_no_surat,
    #         surat_dari  = get_surat_dari,
    #         perihal     = get_perihal,
    #         upload_file = files_upload
            
    #         )
        
    #     tambah_data_surat.save()

    #     return redirect('home')



    context = {
        'disposisi' : disposisi
    }

    return render(request,'pages/olah_disposisi.html' , context )

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'myapp/post_detail.html', {'post': post})


def disposisi_kabadan(request):
        
    if request.method == 'POST':
        no_surat_id = request.POST.get('no_surat')
        no_surat = get_object_or_404(DbSurat, pk=no_surat_id)

        print(no_surat)

        no_agenda = request.POST.get('no_agenda')
        catatan  =  request.POST.get('catatan')
        files_upload_disposisi = request.FILES.get('file_disposisi')

        DisposisiDb.objects.create(
            no_surat = no_surat,
            no_agenda = no_agenda,
            catatan = catatan,
            upload_file_disposisi = files_upload_disposisi
        )
        # dispo_kabadan.save()
        # return redirect(disposisi , pk= dispo_kabadan.pk)






    #     form = DisposisiForm(request.POST)

    #     print(form)
    #     if form.is_valid:
    #         disposisi_kabadan = form.save()

    #         print(disposisi_kabadan)
    #         return redirect('olah_disposisi', pk = disposisi_kabadan.pk )


    # else:
    #     print("hkdagfkagfaf")
    #     form = DisposisiForm()
    # return render(request, 'pages/olah_disposisi.html', {'form': form})





        # no_surat_id = request.POST.get('no_surat')
        # no_surat = DbSurat.objects.get(id)

        # get_no_agenda = request.POST.get('no_agenda')
        # get_catatan  =  request.POST.get('catatan')
        # files_upload_disposisi = request.FILES.get('file_disposisi')

        # DisposisiDb.objects.create(
        #     # disposisi               = disposisi,
        #     no_surat                = no_surat_id,
        #     no_agenda               = get_no_agenda,
        #     catatan                 = get_catatan,
        #     upload_file_disposisi   = files_upload_disposisi
        # )
    # else:
    #     return render

        # form  = DisposisiForm(request.POST , request.FILES)

        # if form.is_valid():
        #     x = form.save(commit =False)
        #     x.save()
        #     return redirect('olah_disposisi', pk= x.pk)
        
    # else:
    #     print("Gagal")
    #     form = DisposisiForm()

        # disposisi = "KABADAN"
        # get_no_surat = request.POST.get('no_surat')
        # get_no_agenda = request.POST.get('no_agenda')
        # get_catatan  =  request.POST.get('catatan')
        # files_upload_disposisi = request.FILES.get('file_disposisi')

        # no_surat = get_object_or_404(DbSurat, pk = id)
        # no_surat = DbSurat.objects.get(pk=get_no_surat)


        # print(no_surat)


        # disposisi_kabadan = DisposisiDb.objects.create(
        #     disposisi               = str(disposisi),
        #     no_surat                = str(no_surat),
        #     no_agenda               = get_no_agenda,
        #     catatan                 = get_catatan,
        #     upload_file_disposisi   = files_upload_disposisi

        # )

        # disposisi_kabadan  = DisposisiDb (
        #     disposisi               = disposisi,
        #     # no_surat                = Dbsurat_id,
        #     no_agenda               = get_no_agenda,
        #     catatan                 = get_catatan,
        #     upload_file_disposisi   = files_upload_disposisi,
        
        #     )
        
        # disposisi_kabadan.save()

    #     return redirect('olah_disposisi')

    # context = {
    #     'disposisi' : disposisi
    # }

    # return render(request,'pages/olah_disposisi.html' , context )

