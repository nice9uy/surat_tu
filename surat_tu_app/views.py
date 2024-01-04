import uuid
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import DbSurat , DbKlasifikasi, DisposisiDb, DbJenisSurat,DbDerajatSurat
from datetime import date
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required
# from django.shortcuts import create_object

@login_required(login_url="/accounts/login/")
def kabaranahan(request, getIDdisosisi_kabaranahan ):
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

@login_required(login_url="/accounts/login/")
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

@login_required(login_url="/accounts/login/")
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


@login_required(login_url="/accounts/login/")
def home(request):
   
    datasemuasurat = DbSurat.objects.all()
    Klasifikasi    = DbKlasifikasi.objects.all().values_list('klasifikasi', flat=True )
    jenis_surat    = DbJenisSurat.objects.all().values_list('jenis_surat', flat=True )


    context = {
        'page_title'   : 'Home',
        'data_surat'   : datasemuasurat,
        'klasifikasi'  : Klasifikasi,
        'jenis_surat'  : jenis_surat
     }
    return render (request , 'pages/index.html' , context )


@login_required(login_url="/accounts/login/")
def tambah_surat(request):
    
    # hari_ini       = date.today()
    username       = request.user
    klasifikasi    = DbKlasifikasi.objects.all().values_list('klasifikasi', flat=True )
    jenis_surat    = DbJenisSurat.objects.all().values_list('jenis_surat', flat=True )
    derajat_surat  = DbDerajatSurat.objects.all().values_list('dejarat_surat', flat=True )

    try:
        if request.method == 'POST':

            get_jenis_surat = request.POST.get('jenis_surat')
            get_klasifikasi = request.POST.get('klasifikasi')
            get_tanggal_agenda = request.POST.get('tanggal_agenda')
            get_no_agenda = request.POST.get('no_agenda')

            get_tanggal_surat = request.POST.get('tanggal_surat')

            get_no_surat = request.POST.get('no_surat')
            get_surat_dari = request.POST.get('surat_dari')
            get_derajat_surat = request.POST.get('derajat_surat')
            get_perihal = request.POST.get('perihal')
            files_upload = request.FILES.get('file_name')

            tambah_data_surat = DbSurat(

                username      = username,
                jenis_surat   = get_jenis_surat,
                klasifikasi   = get_klasifikasi,
                tgl_agenda    = get_tanggal_agenda,
                no_agenda     = get_no_agenda,

                tgl_surat     = get_tanggal_surat if get_tanggal_surat else None ,

                no_surat      = get_no_surat,
                surat_dari    = get_surat_dari,
                derajat_surat = get_derajat_surat,
                perihal       = get_perihal,
                upload_file   = files_upload
                
                )
            
            tambah_data_surat.save()

            return redirect('olah_surat')
        
        context = {
            'page_title' : 'Tambah Surat',
            'klasifikasi': klasifikasi,
            'jenis_surat' : jenis_surat,
            'derajat_surat' : derajat_surat
        }
        return render (request , 'pages/tambah_surat.html' , context )
    except:
        return render (request , 'pages/error_upload_surat.html' )
    
@staff_member_required(login_url="/surat/")
@login_required(login_url="/accounts/login/")
def olah_surat(request) :
    datasemuasurat = DbSurat.objects.all()
    Klasifikasi    = DbKlasifikasi.objects.all().values_list('klasifikasi', flat=True )
    jenis_surat    = DbJenisSurat.objects.all().values_list('jenis_surat', flat=True )
    
    context = {
        'page_title' : 'Olah Surat',
        'data_surat' : datasemuasurat,
        'klasifikasi': Klasifikasi,
        'jenis_surat' : jenis_surat
    }
    
    return render (request , 'pages/olah_surat.html' , context )

@login_required(login_url="/accounts/login/")
def edit_olah_surat(request , id_edit_olah_surat ):
    username = request.user
    edit_olah_surat = get_object_or_404(DbSurat, pk = id_edit_olah_surat)
    
    try:
        if request.method == 'POST':
            get_jenis_surat           = request.POST.get('jenis_surat')
            get_klasifikasi           = request.POST.get('klasifikasi')
            get_tgl_agenda            = request.POST.get('tanggal_agenda')          
            get_no_agenda             = request.POST.get('no_agenda')

            get_tanggal_surat         = request.POST.get('tanggal_surat')

            get_no_surat              = request.POST.get('no_surat')
            get_surat_dari            = request.POST.get('surat_dari')
            get_derajat_surat         = request.POST.get('derajat_surat')
            get_perihal               = request.POST.get('perihal')
            files_upload_data         = request.FILES.get('file_name')

            data_surat =  edit_olah_surat.upload_file.name

            if  files_upload_data == None:
                files_upload  = data_surat

            else:
                files_upload = files_upload_data
                edit_olah_surat.upload_file.delete()

            edit_olah_surat = DbSurat(

                id             = id_edit_olah_surat,
                username       = str(username),
                jenis_surat    = get_jenis_surat,
                klasifikasi    = get_klasifikasi,
                tgl_agenda     = get_tgl_agenda,
                no_agenda      = get_no_agenda,
                
                tgl_surat      = get_tanggal_surat if get_tanggal_surat else None ,

                no_surat       = get_no_surat,
                surat_dari     = get_surat_dari,
                derajat_surat  = get_derajat_surat,
                perihal        = get_perihal,
                upload_file    = files_upload
                
                )
            
            edit_olah_surat.save()
            return redirect('olah_surat')
        
        return render(request,'pages/olah_surat.html')
    except:
        return render (request , 'pages/error_edit_surat.html' )

@login_required(login_url="/accounts/login/")
def delete_olah_surat(request , id_delete_olah_surat):
    delete_olah_surat = get_object_or_404(DbSurat, pk = id_delete_olah_surat)
    if request.method == 'POST':
        delete_olah_surat.upload_file.delete()
        delete_olah_surat.delete()
        return redirect('home')
    
    return render(request,'pages/olah_surat.html')

@login_required(login_url="/accounts/login/")
def disposisi(request ):

    if request.method == 'POST':
        get_no_surat = request.POST.get('filter_no_surat')

        filtered =  get_object_or_404(DbSurat, no_surat = get_no_surat)
        disposisi = DisposisiDb.objects.filter(no_surat = filtered).values()

        context = {
            'disposisi': disposisi,
        }

        return render(request, 'pages/disposisi.html',  context)

    return render(request, 'pages/disposisi.html')
  
@login_required(login_url="/accounts/login/")
def olah_disposisi(request):

    if request.method == 'POST':
        get_no_surat = request.POST.get('filter_no_surat')

        filtered =  get_object_or_404(DbSurat, no_surat = get_no_surat)
        disposisi = DisposisiDb.objects.filter(no_surat = filtered).values()

        context = {
            'page_title' : 'Olah Disposisi',
            'disposisi': disposisi,
        }

        return render(request, 'pages/olah_disposisi.html',  context)

    return render(request, 'pages/olah_disposisi.html')  

@login_required(login_url="/accounts/login/")
def olah_disposisi_edit(request , id_edit_disposisi):

    username = request.user
    edit_olah_surat = get_object_or_404(DisposisiDb, pk = id_edit_disposisi)

    edit_surat_convert_id = edit_olah_surat.id
    edit_surat_convert_nomor_surat_id = edit_olah_surat.no_surat_id

    if request.method == 'POST':

        get_tgl_disposisi              = request.POST.get('tgl_disposisi')
        get_tgl_disposisi_kembali      = request.POST.get('tgl_disposisi_kembali')
        get_disposisi                  = request.POST.get('disposisi')
        no_agenda                      = request.POST.get('no_agenda')
        catatan                        = request.POST.get('catatan')
        files_upload_disposisi         = request.FILES.get('file_name')


        data_surat =  edit_olah_surat.upload_file_disposisi.name

        if  files_upload_disposisi == None:
            files_upload_disposisi_surat = data_surat

        else:
            files_upload_disposisi_surat = files_upload_disposisi
            edit_olah_surat.upload_file_disposisi.delete()

        edit_olah_disposisi = DisposisiDb(

            id                      = edit_surat_convert_id,
            no_surat_id             = edit_surat_convert_nomor_surat_id,
            username                = str(username),
            tgl_disposisi           = get_tgl_disposisi,
            tgl_disposisi_kembali   =  get_tgl_disposisi_kembali,
            disposisi               = get_disposisi,
            no_agenda               = no_agenda,
            catatan                 = catatan,
            upload_file_disposisi   = files_upload_disposisi_surat,
            
            )

        edit_olah_disposisi.save()
        return redirect('olah_surat')

    return render(request,'pages/olah_disposisi.html')

@login_required(login_url="/accounts/login/")
def olah_disposisi_delete(request , id_delete_disposisi) :
    delete_disposisi_surat = get_object_or_404(DisposisiDb, pk = id_delete_disposisi)

    if request.method == 'POST':
        delete_disposisi_surat.upload_file_disposisi.delete()
        delete_disposisi_surat.delete()
        return redirect('olah_surat')
    
    return render(request,'pages/olah_disposisi.html')
 

@login_required(login_url="/accounts/login/")
def upload_disposisi(request):
    hari_ini       = date.today()
    username       = request.user

    try:
        if request.method == 'POST':

            no_surat_data = request.POST.get('no_surat')
            no_surat_instance , created = DbSurat.objects.get_or_create(no_surat = no_surat_data )

            get_tgl_disposisi      = hari_ini
            get_disposisi          = request.POST.get('disposisi')
            no_agenda              = request.POST.get('no_agenda')
            catatan                = request.POST.get('catatan')
            files_upload_disposisi = request.FILES.get('file_name')

            disposisi_instance = DisposisiDb(   

                no_surat              = no_surat_instance,
                username              = username,
                tgl_disposisi         = get_tgl_disposisi,
                disposisi             = get_disposisi,
                no_agenda             = no_agenda,
                catatan               = catatan,
                upload_file_disposisi = files_upload_disposisi
                
            )

            disposisi_instance.save()
    except Exception as e:
       pass

    return redirect('olah_surat')
 

def filter_tanggal(request):

    data_x = DbSurat.objects.all()

    try:
        if request.method == 'POST':
            get_tgl_agenda = request.POST.get('tgl_agenda')
            datasemuasurat = DbSurat.objects.filter( tgl_agenda = get_tgl_agenda)
        
        context = {
            'page_title'   : 'Home',
            'data_surat'   : datasemuasurat,
        }
        return render (request , 'pages/index.html' , context )
    
    except:

        datasurat = data_x

        context = {
            'page_title'   : 'Home',
            'data_surat'   : datasurat,
        }

        return render (request , 'pages/index.html' , context )
    
def filter_tanggal_olah_surat(request):

    data_x = DbSurat.objects.all()

    try:
        if request.method == 'POST':
            get_tgl_agenda = request.POST.get('tgl_agenda')
            datasemuasurat = DbSurat.objects.filter( tgl_agenda = get_tgl_agenda)
        
        context = {
            'page_title'   : 'Olah Surat',
            'data_surat'   : datasemuasurat,
        }
        return render (request , 'pages/olah_surat.html' , context )
    
    except:

        datasurat = data_x

        context = {
            'page_title'   : 'Olah Surat',
            'data_surat'   : datasurat,
        }

        return render (request , 'pages/olah_surat.html' , context )
    
def generate_no_agenda(request):
    
    pass