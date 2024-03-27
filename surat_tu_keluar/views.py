from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from . models import NotaDinas, Biasa
from django.db.models import Q
from datetime import datetime
from django.utils.dateparse import parse_date
import pandas as pd
from django.http import HttpResponse


# Create your views here.

@login_required(login_url="/accounts/login/")
def surat_keluar(request): 
    context = {
        'page_title'    : 'Surat Keluar',
    }
    return render (request , 'surat_keluar/pages/index.html', context )

###############################################################################################
#################### NOTA DINAS ############################################################

@login_required(login_url="/accounts/login/")
def nota_dinas(request):
    # tanggal_sekarang                        =  date.today()
    nota_dinas                              =  NotaDinas.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''))
    context = {
        'page_title'        : 'Nota Dinas',
        'nota_dinas'        :  nota_dinas,
        # 'tanggal_sekarang'  :  tanggal_sekarang
    }
    return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html', context)

@login_required(login_url="/accounts/login/")
def filter_nota_dinas(request):
    nota_dinas                               =  NotaDinas.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''))
    try:
        if request.method == 'POST':
            get_tgl_nota_dinas               =  request.POST.get('tanggal')
            data_nota_dinas                  =  NotaDinas.objects.filter( ~Q(no_takah__isnull=True) & ~Q(no_takah__exact='') , tanggal = get_tgl_nota_dinas).values()
            tanggal                          =  parse_date(get_tgl_nota_dinas)
        context = {
            'page_title'                   : 'Olah Nota Dinas',
            'nota_dinas'                   :  data_nota_dinas,
            'tanggal_nota_dinas'           :  tanggal
        }
        return render (request , 'surat_keluar/pages/nota_dinas/filter_nota_dinas.html' , context )
    except:
        datasurat_keluar = nota_dinas
        context = {
            'page_title'                   : 'Olah Nota Dinas',
            'nota_dinas'                   :  datasurat_keluar,
            'tanggal_nota_dinas'           :  get_tgl_nota_dinas
        }

        return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html' , context )

###################       BON NOMOR      ##############################################
    
@login_required(login_url="/accounts/login/")    
def bon_nomor(request):
    bon_nomor                                =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''))

    print(list(bon_nomor))

    context = {
        'page_title'                        : 'Nota Dinas - Bon Nomor',
        'bon_nomor'                         :  bon_nomor 
    }
    return render (request , 'surat_keluar/pages/nota_dinas/bon_nomor_pages/bon_nomor.html', context)


@login_required(login_url="/accounts/login/")
def filter_bon_nomor(request):
    filter_bon_nomor                             =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''))
    try:
        if request.method == 'POST':
            get_tgl_bon_nomor                    =  request.POST.get('tanggal')
            tanggal_bon_filter                   =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''), tanggal = get_tgl_bon_nomor)
            tanggal                              =  parse_date(get_tgl_bon_nomor)

        context = {
                'page_title'                     : 'Nota Dinas - Bon Nomor',
                'filter_bon_nomor'               :  tanggal_bon_filter,
                'tgl_bon_nomor'                  :  tanggal 
            }
        return render (request , 'surat_keluar/pages/nota_dinas/bon_nomor_pages/filter_bon_nomor.html', context)
    except:
        filter_bon_nomor_1                       = filter_bon_nomor     
        context = {
                'page_title'                     : 'Nota Dinas - Bon Nomor',
                'filter_bon_nomor'               :  filter_bon_nomor_1 
            }
        return render (request , 'surat_keluar/pages/nota_dinas/bon_nomor_pages/filter_bon_nomor.html', context)

@login_required(login_url="/accounts/login/")
def bon_nomor_isi_nota_dinas(request, id_bon_nomor_isi_nota_dinas):
    bon_nomor_isi_nota_dinas                     =  get_object_or_404(NotaDinas, pk = id_bon_nomor_isi_nota_dinas)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_bon_nomor_isi_nota_dinas
        get_username                             = str(username)
        get_tanggal                              = bon_nomor_isi_nota_dinas.tanggal
        get_no_urut                              = bon_nomor_isi_nota_dinas.no_urut
        get_no_takah                             = request.POST.get('no_takah') 
        get_kepada                               = request.POST.get('kepada')
        get_perihal                              = request.POST.get('perihal') 
        get_keterangan                           = request.POST.get('keterangan')
        get_bagian                               = ""
        get_catatan                              = ""
        files_upload_bon_nomor                   = request.FILES.get('file_name')

        bon_nomor_isi_nota_dinas_save    = NotaDinas(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        bon_nomor_isi_nota_dinas_save.save()
        return redirect('bon_nomor')

@login_required(login_url="/accounts/login/")
def filter_bon_nomor_isi_nota_dinas(request, id_filter_bon_nomor_isi_nota_dinas):
    bon_nomor_isi_nota_dinas                     =  get_object_or_404(NotaDinas, pk = id_filter_bon_nomor_isi_nota_dinas)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_filter_bon_nomor_isi_nota_dinas
        get_username                             = str(username)
        get_tanggal                              = bon_nomor_isi_nota_dinas.tanggal
        get_no_urut                              = bon_nomor_isi_nota_dinas.no_urut
        get_no_takah                             = request.POST.get('no_takah') 
        get_kepada                               = request.POST.get('kepada')
        get_perihal                              = request.POST.get('perihal') 
        get_keterangan                           = request.POST.get('keterangan')
        get_bagian                               = ""
        get_catatan                              = ""
        files_upload_bon_nomor                   = request.FILES.get('file_name')

        bon_nomor_isi_nota_dinas_save    = NotaDinas(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        bon_nomor_isi_nota_dinas_save.save()
        return redirect('filter_bon_nomor')
    


@login_required(login_url="/accounts/login/")
def bon_nomor_edit_bon_nomor(request, id_bon_nomor_edit_bon_nomor):
    bon_nomor_edit_bon_nomor                     =  get_object_or_404(NotaDinas, pk = id_bon_nomor_edit_bon_nomor)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_bon_nomor_edit_bon_nomor
        get_username                             = str(username)
        get_tanggal                              = bon_nomor_edit_bon_nomor.tanggal
        get_no_urut                              = bon_nomor_edit_bon_nomor.no_urut
        get_no_urut_temp                         = bon_nomor_edit_bon_nomor.no_urut_temp
        get_no_takah                             = ""
        get_kepada                               = ""
        get_perihal                              = ""
        get_keterangan                           = ""
        get_bagian                               = request.POST.get('bagian')
        get_catatan                              = request.POST.get('catatan')
        files_upload_bon_nomor                   = bon_nomor_edit_bon_nomor.upload_file

        bon_nomor_isi_nota_dinas_save    = NotaDinas(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_urut_temp                         = get_no_urut_temp,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        bon_nomor_isi_nota_dinas_save.save()
        return redirect('bon_nomor')
    
@login_required(login_url="/accounts/login/")
def filter_bon_nomor_edit_bon_nomor(request, id_filter_bon_nomor_edit_bon_nomor):
    filter_bon_nomor_edit_bon_nomor              =  get_object_or_404(NotaDinas, pk = id_filter_bon_nomor_edit_bon_nomor)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_filter_bon_nomor_edit_bon_nomor
        get_username                             = str(username)
        get_tanggal                              = filter_bon_nomor_edit_bon_nomor.tanggal
        get_no_urut                              = filter_bon_nomor_edit_bon_nomor.no_urut
        get_no_takah                             = ""
        get_kepada                               = ""
        get_perihal                              = ""
        get_keterangan                           = ""
        get_bagian                               = request.POST.get('bagian')
        get_catatan                              = request.POST.get('catatan')
        files_upload_bon_nomor                   = filter_bon_nomor_edit_bon_nomor.upload_file

        filter_edit_bon_nomor_save    = NotaDinas(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        filter_edit_bon_nomor_save.save()
        return redirect('filter_bon_nomor')
    
    
    
# #####################    Nomor Tersedia       ####################################################
    
@login_required(login_url="/accounts/login/")    
def nomor_tersedia(request):
    tanggal_sekarang                         =  date.today()
    nomor_tersedia                           =  NotaDinas.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ) , Q(bagian__isnull=False) &  Q(bagian__exact='' ) , tanggal = tanggal_sekarang)

    context = {
        'page_title'                        :  'Nota Dinas - No Tersedia',
        'nomor_tersedia'                    :  nomor_tersedia,
        'tanggal'                           :  tanggal_sekarang
    }
    return render (request , 'surat_keluar/pages/nota_dinas/nomor_tersedia_pages/nomor_tersedia.html', context)


@login_required(login_url="/accounts/login/")
def nomor_tersedia_tambah_nomor(request): 

    try:
        no_urut_nota_dinas               = list(NotaDinas.objects.all().values_list('no_urut').last())
        nota_dinas_data                  = no_urut_nota_dinas[0]

        get_no_akhir                     = int(nota_dinas_data) + 1
    except:
        get_no_akhir  = 1

    bulan_ini  = date.today().month
    tahun_ini  = date.today().year

    if bulan_ini == 1:
            bulan = 'I'
    elif bulan_ini == 2:
            bulan = 'II'
    elif bulan_ini == 3:
            bulan = 'III'
    elif bulan_ini == 4:
            bulan = 'IV'
    elif bulan_ini == 5:
            bulan = 'V'
    elif bulan_ini == 6:
            bulan = 'VI'
    elif bulan_ini == 7:
            bulan = 'VII'
    elif bulan_ini == 8:
            bulan = 'VIII'
    elif bulan_ini == 9:
            bulan = 'IX'
    elif bulan_ini == 10:
            bulan = 'X'
    elif bulan_ini == 11:
            bulan = 'XI'
    else:
            bulan = 'XII'

           
    get_username                         =  request.user
    get_hari_ini                         =  date.today()
    get_no_urut                          =  get_no_akhir
    get_no_urut_temp                     =  f"B/ND/{get_no_akhir}/{bulan}/{tahun_ini}/..."
    get_no_takah                         =  ''
    get_kepada                           =  ''
    get_perihal                          =  ''
    get_keterangan                       =  ''
    get_catatan                          =  ''
    get_bagian                           =  ''
    get_upload_file                      =  ''

    SemuaNotaDinas_instance = NotaDinas(   

        username                         = get_username,
        tanggal                          = get_hari_ini,
        no_urut                          = get_no_urut,
        no_urut_temp                     = get_no_urut_temp,
        no_takah                         = get_no_takah,
        kepada                           = get_kepada,
        perihal                          = get_perihal,
        keterangan                       = get_keterangan,
        catatan                          = get_catatan,
        bagian                           = get_bagian,
        upload_file                      = get_upload_file
                 
    )

    SemuaNotaDinas_instance.save()
    return redirect('nomor_tersedia')


@login_required(login_url="/accounts/login/")    
def nomor_tersedia_bon_nomor(request, id_nomor_tersedia_bon_nomor):
   
    nomor_tersedia_isi_nota_dinas                =  get_object_or_404(NotaDinas, pk = id_nomor_tersedia_bon_nomor)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_nomor_tersedia_bon_nomor
        get_username                             = str(username)
        get_tanggal                              = nomor_tersedia_isi_nota_dinas.tanggal
        get_no_urut                              = nomor_tersedia_isi_nota_dinas.no_urut
        get_no_urut_temp                         = nomor_tersedia_isi_nota_dinas.no_urut_temp
        get_no_takah                             = ""
        get_kepada                               = ""
        get_perihal                              = ""
        get_keterangan                           = ""
        get_bagian                               = request.POST.get('bagian')
        get_catatan                              = request.POST.get('catatan')
        files_upload_bon_nomor                   = nomor_tersedia_isi_nota_dinas.upload_file


        bon_nomor_isi_nota_dinas_save    = NotaDinas(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_urut_temp                         = get_no_urut_temp,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        bon_nomor_isi_nota_dinas_save.save()    
        return redirect('nomor_tersedia')


@login_required(login_url="/accounts/login/")
def nomor_tersedia_isi_nota_dinas(request, id_nomor_tersedia_isi_nota_dinas):
    bon_nomor_isi_nota_dinas                     =  get_object_or_404(NotaDinas, pk = id_nomor_tersedia_isi_nota_dinas)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_nomor_tersedia_isi_nota_dinas
        get_username                             = str(username)
        get_tanggal                              = bon_nomor_isi_nota_dinas.tanggal
        get_no_urut                              = bon_nomor_isi_nota_dinas.no_urut
        get_no_takah                             = request.POST.get('no_takah') 
        get_kepada                               = request.POST.get('kepada')
        get_perihal                              = request.POST.get('perihal') 
        get_keterangan                           = request.POST.get('keterangan')
        get_bagian                               = ""
        get_catatan                              = ""
        files_upload_bon_nomor                   = request.FILES.get('file_name')

        bon_nomor_isi_nota_dinas_save    = NotaDinas(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        bon_nomor_isi_nota_dinas_save.save()
        return redirect('nomor_tersedia')


@login_required(login_url="/accounts/login/")
def filter_nomor_tersedia(request):
    tanggal_sekarang                             =  date.today()
    filter_nomor_tersedia                        =  NotaDinas.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ) , Q(bagian__isnull=False) &  Q(bagian__exact='' ) , tanggal = tanggal_sekarang)
    
    try:
        if request.method == 'POST':
            tanggal_sekarang_now                 =  request.POST.get('tanggal')
            nomor_tersedia                       =  NotaDinas.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ) , Q(bagian__isnull=False) &  Q(bagian__exact='' ) , tanggal = tanggal_sekarang_now)
            tanggal                              =  parse_date(tanggal_sekarang_now)

        context = {
                'page_title'                     : 'Nota Dinas - No Tersedia',
                'filter_nomor_tersedia'          :  nomor_tersedia,
                'tgl_nomor_tersedia'             :  tanggal 
            }
        return render (request , 'surat_keluar/pages/nota_dinas/nomor_tersedia_pages/filter_nomor_tersedia.html', context)
    except:
        filter_bon_nomor_1                       = filter_nomor_tersedia     
        context = {
                'page_title'                     : 'Nota Dinas - No Tersedia',
                'filter_nomor_tersedia'          :  filter_bon_nomor_1 ,
                'tgl_nomor_tersedia'             :  tanggal_sekarang 
            }
        return render (request , 'surat_keluar/pages/nota_dinas/nomor_tersedia_pages/filter_nomor_tersedia.html', context)


@login_required(login_url="/accounts/login/")    
def filter_nomor_tersedia_bon_nomor(request, id_filter_nomor_tersedia_bon_nomor):
   
    nomor_tersedia_isi_nota_dinas                =  get_object_or_404(NotaDinas, pk = id_filter_nomor_tersedia_bon_nomor)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_filter_nomor_tersedia_bon_nomor
        get_username                             = str(username)
        get_tanggal                              = nomor_tersedia_isi_nota_dinas.tanggal
        get_no_urut                              = nomor_tersedia_isi_nota_dinas.no_urut
        get_no_urut_temp                         = nomor_tersedia_isi_nota_dinas.no_urut_temp
        get_no_takah                             = ""
        get_kepada                               = ""
        get_perihal                              = ""
        get_keterangan                           = ""
        get_bagian                               = request.POST.get('bagian')
        get_catatan                              = request.POST.get('catatan')
        files_upload_bon_nomor                   = nomor_tersedia_isi_nota_dinas.upload_file


        bon_nomor_isi_nota_dinas_save    = NotaDinas(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_urut_temp                         = get_no_urut_temp,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        bon_nomor_isi_nota_dinas_save.save()    
        return redirect('filter_nomor_tersedia')



@login_required(login_url="/accounts/login/")
def filter_nomor_tersedia_isi_nota_dinas(request, id_filter_nomor_tersedia_isi_nota_dinas):
    bon_nomor_isi_nota_dinas                     =  get_object_or_404(NotaDinas, pk = id_filter_nomor_tersedia_isi_nota_dinas)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_filter_nomor_tersedia_isi_nota_dinas
        get_username                             = str(username)
        get_tanggal                              = bon_nomor_isi_nota_dinas.tanggal
        get_no_urut                              = bon_nomor_isi_nota_dinas.no_urut
        get_no_takah                             = request.POST.get('no_takah') 
        get_kepada                               = request.POST.get('kepada')
        get_perihal                              = request.POST.get('perihal') 
        get_keterangan                           = request.POST.get('keterangan')
        get_bagian                               = ""
        get_catatan                              = ""
        files_upload_bon_nomor                   = request.FILES.get('file_name')

        bon_nomor_isi_nota_dinas_save    = NotaDinas(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        bon_nomor_isi_nota_dinas_save.save()
        return redirect('filter_nomor_tersedia')
    
# #####################    OLAH NOTA DINAS       ####################################################

def edit_nota_dinas(request):
    edit_nota_dinas                              =  NotaDinas.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''))

    context = {
                'page_title'                     : 'Nota Dinas - Edit Nota Dinas', 
                'edit_nota_dinas'                :  edit_nota_dinas,

    }
    return render (request , 'surat_keluar/pages/nota_dinas/edit_nota_dinas_pages/edit_nota_dinas.html', context)


@login_required(login_url="/accounts/login/")
def edit_nota_dinas_modal(request, id_edit_nota_dinas_modal):
    edit_nota_dinas_modal                           =  get_object_or_404(NotaDinas, pk = id_edit_nota_dinas_modal)
    username                                        =  request.user

    try:
        if request.method == 'POST':
            get_id                                   = id_edit_nota_dinas_modal
            get_username                             = str(username)
            get_tanggal                              = edit_nota_dinas_modal.tanggal
            get_no_urut                              = edit_nota_dinas_modal.no_urut
            get_no_takah                             = request.POST.get('no_takah') 
            get_kepada                               = request.POST.get('kepada')
            get_perihal                              = request.POST.get('perihal') 
            get_keterangan                           = request.POST.get('keterangan')
            get_bagian                               = ""
            get_catatan                              = ""
            files_upload_edit_bon_nomor              = request.FILES.get('file_name')

            file_data_nota_dinas                     =  edit_nota_dinas_modal.upload_file.name

            if  files_upload_edit_bon_nomor == None:
                data_files_upload  = file_data_nota_dinas

            else:
                data_files_upload = files_upload_edit_bon_nomor
                edit_nota_dinas_modal.upload_file.delete()

            edit_nomor_nota_dinas = NotaDinas(

                id                                   = get_id,
                username                             = get_username,
                tanggal                              = get_tanggal,
                no_urut                              = get_no_urut,
                no_takah                             = get_no_takah,
                kepada                               = get_kepada,
                perihal                              = get_perihal,
                keterangan                           = get_keterangan,
                bagian                               = get_bagian,
                catatan                              = get_catatan,
                upload_file                          = data_files_upload
                
                )
            
            edit_nomor_nota_dinas.save()
            return redirect('edit_nota_dinas')
        
        return render (request , 'surat_keluar/pages/nota_dinas/edit_nota_dinas_pages/edit_nota_dinas.html')
    except:
        return render (request , 'surat_keluar/pages/nota_dinas/edit_nota_dinas_pages/edit_nota_dinas.html')


@login_required(login_url="/accounts/login/")
def filter_edit_nota_dinas(request):
    tanggal_sekarang                       =  date.today()
    edit_filter_nota_dinas_all             =  NotaDinas.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''))
    # print(edit_filter_nota_dinas_all)
    try:
        if request.method == 'POST':
            get_tgl_nota_dinas             =  request.POST.get('tanggal')
            edit_filter_nota_dinas         =  NotaDinas.objects.filter( ~Q(no_takah__isnull=True) & ~Q(no_takah__exact='') , tanggal = get_tgl_nota_dinas).values()
            tanggal                        =  parse_date(get_tgl_nota_dinas)

        context = {
            'page_title'                   : 'Olah Nota Dinas',
            'filter_edit_nota_dinas'       :  edit_filter_nota_dinas,
            'tanggal_edit_nota_dinas'      :  tanggal
        }

        return render (request , 'surat_keluar/pages/nota_dinas/edit_nota_dinas_pages/filter_edit_nota_dinas.html', context)
    except:
        edit_filter                        = edit_filter_nota_dinas_all
        context = {
            'page_title'                   : 'Olah Nota Dinas',
            'filter_edit_nota_dinas'       :  edit_filter,
            'tanggal_edit_nota_dinas'      :  tanggal_sekarang
        }

        return render (request , 'surat_keluar/pages/nota_dinas/edit_nota_dinas_pages/filter_edit_nota_dinas.html', context)


@login_required(login_url="/accounts/login/")
def filter_edit_nota_dinas_modal(request, id_filter_edit_nota_dinas_modal):
    filter_edit_nota_dinas_modal                     =  get_object_or_404(NotaDinas, pk = id_filter_edit_nota_dinas_modal)
    username                                         =  request.user

    try:
        if request.method == 'POST':
            get_id                                   = id_filter_edit_nota_dinas_modal
            get_username                             = str(username)
            get_tanggal                              = filter_edit_nota_dinas_modal.tanggal
            get_no_urut                              = filter_edit_nota_dinas_modal.no_urut
            get_no_takah                             = request.POST.get('no_takah') 
            get_kepada                               = request.POST.get('kepada')
            get_perihal                              = request.POST.get('perihal') 
            get_keterangan                           = request.POST.get('keterangan')
            get_bagian                               = ""
            get_catatan                              = ""
            files_upload_edit_bon_nomor              = request.FILES.get('file_name')

            file_data_nota_dinas                     = filter_edit_nota_dinas_modal.upload_file.name

            if  files_upload_edit_bon_nomor == None:
                data_files_upload  = file_data_nota_dinas

            else:
                data_files_upload = files_upload_edit_bon_nomor
                filter_edit_nota_dinas_modal.upload_file.delete()

            edit_nomor_nota_dinas = NotaDinas(

                id                                   = get_id,
                username                             = get_username,
                tanggal                              = get_tanggal,
                no_urut                              = get_no_urut,
                no_takah                             = get_no_takah,
                kepada                               = get_kepada,
                perihal                              = get_perihal,
                keterangan                           = get_keterangan,
                bagian                               = get_bagian,
                catatan                              = get_catatan,
                upload_file                          = data_files_upload
                
                )
            
            edit_nomor_nota_dinas.save()
            return redirect('filter_edit_nota_dinas')
        
        return render (request , 'surat_keluar/pages/nota_dinas/edit_nota_dinas_pages/filter_edit_nota_dinas.html')
    except:
        return render (request , 'surat_keluar/pages/nota_dinas/edit_nota_dinas_pages/filter_edit_nota_dinas.html')


@login_required(login_url="/accounts/login/")
def export_ke_excel_nota_dinas(request):

    try:
    
        if request.method == 'POST':
            # hari_ini                  = date.today()
            tanggal_awal              = request.POST.get('tanggal_awal')
            tanggal_akhir             = request.POST.get('tanggal_akhir')

            awal                      = parse_date(tanggal_awal)
            akhir                     = parse_date(tanggal_akhir)

            data_filter               = pd.DataFrame(list(NotaDinas.objects.filter( ~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''), tanggal__range=[awal, akhir]).values()))
            tanggal                   = pd.to_datetime(data_filter['tanggal']).dt.strftime("%d-%m-%Y")
            data_1                    = pd.DataFrame(data_filter, columns =['no_takah','kepada','perihal','keterangan'])  

            gabung_data               = pd.concat([tanggal, data_1 ], axis=1 )

            df                        = pd.DataFrame(gabung_data)
            df.rename(columns         = {
                                            'tanggal'      :'TANGGAL', 
                                            'no_takah'    :'NOMOR TAKAH',
                                            'kepada'       :'KEPADA',
                                            'perihal'      :'PERIHAL',
                                            'keterangan'   :'KETERANGAN',
                                            
                                        }, inplace = True) 
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="laporan_nota_dinas.xlsx"'                                        
            df.to_excel(response , index=False) 
            return response 

        return redirect('edit_nota_dinas')
    except:
        return redirect('edit_nota_dinas')



@login_required(login_url="/accounts/login/")
def filter_export_ke_excel_nota_dinas(request):

    try:
    
        if request.method == 'POST':
            # hari_ini                  = date.today()
            tanggal_awal              = request.POST.get('tanggal_awal')
            tanggal_akhir             = request.POST.get('tanggal_akhir')

            awal                      = parse_date(tanggal_awal)
            akhir                     = parse_date(tanggal_akhir)

            data_filter               = pd.DataFrame(list(NotaDinas.objects.filter( ~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''), tanggal__range=[awal, akhir]).values()))
            tanggal                   = pd.to_datetime(data_filter['tanggal']).dt.strftime("%d-%m-%Y")
            data_1                    = pd.DataFrame(data_filter, columns =['no_takah','kepada','perihal','keterangan'])  

            gabung_data               = pd.concat([tanggal, data_1 ], axis=1 )

            df                        = pd.DataFrame(gabung_data)
            df.rename(columns         = {
                                            'tanggal'      :'TANGGAL', 
                                            'no_takah'    :'NOMOR TAKAH',
                                            'kepada'       :'KEPADA',
                                            'perihal'      :'PERIHAL',
                                            'keterangan'   :'KETERANGAN',
                                            
                                        }, inplace = True) 
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="laporan_nota_dinas.xlsx"'                                        
            df.to_excel(response , index=False) 
            return response 

        return redirect('filter_edit_nota_dinas')
    except:
        return redirect('filter_edit_nota_dinas')

##########################################################################################################
##################################  BIASA  ################################################################
##########################################################################################################

@login_required(login_url="/accounts/login/")
def biasa(request):
    surat_biasa                              =  Biasa.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''))

    context = {
        'page_title'          : 'Surat Biasa',
        'data_surat_biasa'    :  surat_biasa
    }
    return render (request , 'surat_keluar/pages/biasa/surat_biasa.html', context )


##################   Surat Biasa Bon Nomor      ########
@login_required(login_url="/accounts/login/")
def biasa_bon_nomor(request):
    surat_biasa                              =  Biasa.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''))

    context = {
        'page_title'                         : 'Bon Nomor',
        'surat_biasa_isi_bon_nomor'          :  surat_biasa
    }

    return render (request , 'surat_keluar/pages/biasa/bon_nomor_pages/bon_nomor.html', context )


@login_required(login_url="/accounts/login/")
def biasa_bon_nomor_edit_bon_nomor(request, id_biasa_bon_nomor_edit_bon_nomor):
    biasa_bon_nomor_edit_bon_nomor               =  get_object_or_404(Biasa, pk = id_biasa_bon_nomor_edit_bon_nomor)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_biasa_bon_nomor_edit_bon_nomor
        get_username                             = str(username)
        get_tanggal                              = biasa_bon_nomor_edit_bon_nomor.tanggal
        get_no_urut                              = biasa_bon_nomor_edit_bon_nomor.no_urut
        get_no_takah                             = ""
        get_kepada                               = ""
        get_perihal                              = ""
        get_keterangan                           = ""
        get_bagian                               = request.POST.get('bagian')
        get_catatan                              = request.POST.get('catatan')
        files_upload_bon_nomor                   = biasa_bon_nomor_edit_bon_nomor.upload_file

        biasa_bon_nomor_isi_nota_dinas_save    = Biasa(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        biasa_bon_nomor_isi_nota_dinas_save.save()
        return redirect('biasa_bon_nomor')


@login_required(login_url="/accounts/login/")
def biasa_nomor_tersedia_isi_surat_biasa(request, id_biasa_nomor_tersedia_isi_surat_biasa):
    biasa_bon_nomor_isi_surat_biasa              =  get_object_or_404(Biasa, pk = id_biasa_nomor_tersedia_isi_surat_biasa)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_biasa_nomor_tersedia_isi_surat_biasa
        get_username                             = str(username)
        get_tanggal                              = biasa_bon_nomor_isi_surat_biasa.tanggal
        get_no_urut                              = biasa_bon_nomor_isi_surat_biasa.no_urut
        get_no_takah                             = request.POST.get('no_takah') 
        get_kepada                               = request.POST.get('kepada')
        get_perihal                              = request.POST.get('perihal') 
        get_keterangan                           = request.POST.get('keterangan')
        get_bagian                               = ""
        get_catatan                              = ""
        files_upload_bon_nomor                   = request.FILES.get('file_name')

        biasa_bon_nomor_isi_surat_biasa_save    = Biasa(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        biasa_bon_nomor_isi_surat_biasa_save.save()
        return redirect('biasa_bon_nomor')


@login_required(login_url="/accounts/login/")
def filter_bon_nomor_surat_biasa(request):
    tanggal_sekarang                       =  date.today()
    filter_bon_nomor_surat_biasa_all       =  Biasa.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''))


    try:
        if request.method == 'POST':
            get_tgl_surat_biasa            =  request.POST.get('tanggal')
            filter_bon_nomor_surat_biasa   =  Biasa.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''), tanggal = get_tgl_surat_biasa).values()
            tanggal                        =  parse_date(get_tgl_surat_biasa)


        context = {
            'page_title'                          : 'Bon Nomor - Filter Surat Biasa',
            'filter_bon_nomor_surat_biasa'        :  filter_bon_nomor_surat_biasa,
            'tanggal_filter_bon_nomor_surat_biasa':  tanggal
        }

        return render (request , 'surat_keluar/pages/biasa/bon_nomor_pages/filter_bon_nomor.html', context)
    except:
        edit_filter                        = filter_bon_nomor_surat_biasa_all
        context = {
            'page_title'                          : 'Bon Nomor - Filter Surat Biasa',
            'filter_bon_nomor_surat_biasa'        :  edit_filter,
            'tanggal_filter_bon_nomor_surat_biasa':  tanggal_sekarang
        }

        return render (request , 'surat_keluar/pages/biasa/bon_nomor_pages/filter_bon_nomor.html', context)
    

@login_required(login_url="/accounts/login/")
def filter_surat_biasa_bon_nomor_edit_bon_nomor(request, id_filter_surat_biasa_bon_nomor_edit_bon_nomor):
    filter_surat_biasa_bon_nomor_edit_bon_nomor        =  get_object_or_404(Biasa, pk = id_filter_surat_biasa_bon_nomor_edit_bon_nomor)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_filter_surat_biasa_bon_nomor_edit_bon_nomor
        get_username                             = str(username)
        get_tanggal                              = filter_surat_biasa_bon_nomor_edit_bon_nomor.tanggal
        get_no_urut                              = filter_surat_biasa_bon_nomor_edit_bon_nomor.no_urut
        get_no_takah                             = ""
        get_kepada                               = ""
        get_perihal                              = ""
        get_keterangan                           = ""
        get_bagian                               = request.POST.get('bagian')
        get_catatan                              = request.POST.get('catatan')
        files_upload_bon_nomor                   = filter_surat_biasa_bon_nomor_edit_bon_nomor.upload_file

        filter_surat_biasa_bon_nomor_edit_bon_nomor_save    = Biasa(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        filter_surat_biasa_bon_nomor_edit_bon_nomor_save.save()
        return redirect('filter_bon_nomor_surat_biasa')


@login_required(login_url="/accounts/login/")
def filter_surat_biasa_nomor_tersedia_isi_surat_biasa(request, id_filter_surat_biasa_nomor_tersedia_isi_surat_biasa):
    filter_surat_biasa_nomor_tersedia_isi_surat_biasa  =  get_object_or_404(Biasa, pk = id_filter_surat_biasa_nomor_tersedia_isi_surat_biasa)
    username                                           =  request.user

    if request.method == 'POST':

        get_id                                   = id_filter_surat_biasa_nomor_tersedia_isi_surat_biasa
        get_username                             = str(username)
        get_tanggal                              = filter_surat_biasa_nomor_tersedia_isi_surat_biasa.tanggal
        get_no_urut                              = filter_surat_biasa_nomor_tersedia_isi_surat_biasa.no_urut
        get_no_takah                             = request.POST.get('no_takah') 
        get_kepada                               = request.POST.get('kepada')
        get_perihal                              = request.POST.get('perihal') 
        get_keterangan                           = request.POST.get('keterangan')
        get_bagian                               = ""
        get_catatan                              = ""
        files_upload_bon_nomor                   = request.FILES.get('file_name')

        filter_surat_biasa_nomor_tersedia_isi_surat_biasa_save    = Biasa(
            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        filter_surat_biasa_nomor_tersedia_isi_surat_biasa_save.save()
        return redirect('filter_bon_nomor_surat_biasa')


#################   Surat Biasa Nomor Tersedia   ########
    
@login_required(login_url="/accounts/login/")
def biasa_no_tersedia(request):
    tanggal_sekarang                         =  date.today()
    surat_biasa_nomor_tersedia               =  Biasa.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ) , Q(bagian__isnull=False) &  Q(bagian__exact='' ) , tanggal = tanggal_sekarang)
    
    context = {
        'page_title'                         : 'Biasa - No Tersedia',
        'surat_biasa_nomor_tersedia'         :  surat_biasa_nomor_tersedia,
        'tanggal_nomor_tersedia'             :  tanggal_sekarang
    }
    return render (request , 'surat_keluar/pages/biasa/nomor_tersedia_pages/nomor_tersedia.html', context )


@login_required(login_url="/accounts/login/")
def filter_biasa_nomor_tersedia(request):
    tanggal_sekarang                             =  date.today()
    filter_surat_biasa_nomor_tersedia            =  Biasa.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ) , Q(bagian__isnull=False) &  Q(bagian__exact='' ) , tanggal = tanggal_sekarang)
    
    try: 
        if request.method == 'POST':
            tanggal_sekarang_now                 =  request.POST.get('tanggal')
            nomor_tersedia                       =  Biasa.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ) , Q(bagian__isnull=False) &  Q(bagian__exact='' ) , tanggal = tanggal_sekarang_now)
            tanggal                              =  parse_date(tanggal_sekarang_now)

        context = {
                'page_title'                     : 'Biasa - Filter No Tersedia',
                'filter_biasa_nomor_tersedia'    :  nomor_tersedia,
                'tgl_nomor_tersedia'             :  tanggal 
            }
        
        return render (request , 'surat_keluar/pages/biasa/nomor_tersedia_pages/filter_nomor_tersedia.html', context )
    except:
        filter_no_tersedia_data                  = filter_surat_biasa_nomor_tersedia     
        context = {
                'page_title'                     : 'Biasa - Filter No Tersedia',
                'filter_biasa_nomor_tersedia'    :  filter_no_tersedia_data ,
                'tgl_nomor_tersedia'             :  tanggal_sekarang 
            }
        return render (request , 'surat_keluar/pages/biasa/nomor_tersedia_pages/filter_nomor_tersedia.html', context )
    

@login_required(login_url="/accounts/login/")
def surat_biasa_nomor_tersedia_tambah_nomor(request):

    try:
        no_urut_surat_biasa              = list(Biasa.objects.all().values_list('no_urut').last())
        data_surat_biasa                 = no_urut_surat_biasa[0]

        get_no_akhir                     = int(data_surat_biasa) + 1
    except:
        get_no_akhir  = 1

    bulan_ini  = date.today().month
    tahun_ini  = date.today().year

    if bulan_ini == 1:
            bulan = 'I'
    elif bulan_ini == 2:
            bulan = 'II'
    elif bulan_ini == 3:
            bulan = 'III'
    elif bulan_ini == 4:
            bulan = 'IV'
    elif bulan_ini == 5:
            bulan = 'V'
    elif bulan_ini == 6:
            bulan = 'VI'
    elif bulan_ini == 7:
            bulan = 'VII'
    elif bulan_ini == 8:
            bulan = 'VIII'
    elif bulan_ini == 9:
            bulan = 'IX'
    elif bulan_ini == 10:
            bulan = 'X'
    elif bulan_ini == 11:
            bulan = 'XI'
    else:
            bulan = 'XII'

           
    get_username                         =  request.user
    get_hari_ini                         =  date.today()
    get_no_urut                          =  get_no_akhir
    get_no_urut_temp                     =  f"B/ND/{get_no_akhir}/{bulan}/{tahun_ini}/..."
    get_no_takah                         =  ''
    get_kepada                           =  ''
    get_perihal                          =  ''
    get_keterangan                       =  ''
    get_catatan                          =  ''
    get_bagian                           =  ''
    get_upload_file                      =  ''

    Surat_Biasa_instance    = Biasa(   

        username                         = get_username,
        tanggal                          = get_hari_ini,
        no_urut                          = get_no_urut,
        no_urut_temp                     = get_no_urut_temp,
        no_takah                         = get_no_takah,
        kepada                           = get_kepada,
        perihal                          = get_perihal,
        keterangan                       = get_keterangan,
        catatan                          = get_catatan,
        bagian                           = get_bagian,
        upload_file                      = get_upload_file
                 
    )

    Surat_Biasa_instance.save()
    return redirect('biasa_no_tersedia')

######################
@login_required(login_url="/accounts/login/")    
def surat_biasa_nomor_tersedia_isi_bon_nomor(request, id_surat_biasa_nomor_tersedia_isi_bon_nomor):
   
    nomor_tersedia_isi_surat_biasa               = get_object_or_404(Biasa, pk = id_surat_biasa_nomor_tersedia_isi_bon_nomor)
    username                                     = request.user

    if request.method == 'POST':

        get_id                                   = id_surat_biasa_nomor_tersedia_isi_bon_nomor
        get_username                             = str(username)
        get_tanggal                              = nomor_tersedia_isi_surat_biasa.tanggal
        get_no_urut                              = nomor_tersedia_isi_surat_biasa.no_urut
        get_no_takah                             = ""
        get_kepada                               = ""
        get_perihal                              = ""
        get_keterangan                           = ""
        get_bagian                               = request.POST.get('bagian')
        get_catatan                              = request.POST.get('catatan')
        files_upload_bon_nomor                   = nomor_tersedia_isi_surat_biasa.upload_file


        nomor_tersedia_isi_bon_nomor_save    = Biasa(
            id                                   = get_id,
            username                             = get_username, 
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        nomor_tersedia_isi_bon_nomor_save.save()    
        return redirect('biasa_no_tersedia')
    
    

@login_required(login_url="/accounts/login/")
def surat_biasa_nomor_tersedia_isi_surat_biasa(request, id_surat_biasa_nomor_tersedia_isi_surat_biasa):
    nomor_tersedia_isi_surat_biasa               =  get_object_or_404(Biasa, pk = id_surat_biasa_nomor_tersedia_isi_surat_biasa)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_surat_biasa_nomor_tersedia_isi_surat_biasa
        get_username                             = str(username)
        get_tanggal                              = nomor_tersedia_isi_surat_biasa.tanggal
        get_no_urut                              = nomor_tersedia_isi_surat_biasa.no_urut
        get_no_takah                             = request.POST.get('no_takah') 
        get_kepada                               = request.POST.get('kepada')
        get_perihal                              = request.POST.get('perihal') 
        get_keterangan                           = request.POST.get('keterangan')
        get_bagian                               = ""
        get_catatan                              = ""
        files_upload_isi_surat_biasa             = request.FILES.get('file_name')

        nomor_tersedia_isi_surat_biasa_save = Biasa(

            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_isi_surat_biasa

        )
        
        nomor_tersedia_isi_surat_biasa_save.save()
        return redirect('biasa_no_tersedia')


@login_required(login_url="/accounts/login/")    
def filter_surat_biasa_nomor_tersedia_isi_bon_nomor(request, id_filter_surat_biasa_nomor_tersedia_isi_bon_nomor):
   
    filter_nomor_tersedia_isi_surat_biasa        = get_object_or_404(Biasa, pk = id_filter_surat_biasa_nomor_tersedia_isi_bon_nomor)
    username                                     = request.user

    if request.method == 'POST':

        get_id                                   = id_filter_surat_biasa_nomor_tersedia_isi_bon_nomor
        get_username                             = str(username)
        get_tanggal                              = filter_nomor_tersedia_isi_surat_biasa.tanggal
        get_no_urut                              = filter_nomor_tersedia_isi_surat_biasa.no_urut
        get_no_takah                             = ""
        get_kepada                               = ""
        get_perihal                              = ""
        get_keterangan                           = ""
        get_bagian                               = request.POST.get('bagian')
        get_catatan                              = request.POST.get('catatan')
        files_upload_bon_nomor                   = filter_nomor_tersedia_isi_surat_biasa.upload_file


        nomor_tersedia_isi_bon_nomor_save    = Biasa(
            id                                   = get_id,
            username                             = get_username, 
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_bon_nomor

        )
        
        nomor_tersedia_isi_bon_nomor_save.save()    
        return redirect('filter_biasa_nomor_tersedia')
    
@login_required(login_url="/accounts/login/")
def filter_surat_biasa_nomor_tersedia_isi_surat_biasa(request, id_filter_surat_biasa_nomor_tersedia_isi_surat_biasa):
    filter_nomor_tersedia_isi_surat_biasa        =  get_object_or_404(Biasa, pk = id_filter_surat_biasa_nomor_tersedia_isi_surat_biasa)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_filter_surat_biasa_nomor_tersedia_isi_surat_biasa
        get_username                             = str(username)
        get_tanggal                              = filter_nomor_tersedia_isi_surat_biasa.tanggal
        get_no_urut                              = filter_nomor_tersedia_isi_surat_biasa.no_urut
        get_no_takah                             = request.POST.get('no_takah') 
        get_kepada                               = request.POST.get('kepada')
        get_perihal                              = request.POST.get('perihal') 
        get_keterangan                           = request.POST.get('keterangan')
        get_bagian                               = ""
        get_catatan                              = ""
        files_upload_isi_surat_biasa             = request.FILES.get('file_name')

        filter_nomor_tersedia_isi_surat_biasa_save = Biasa(

            id                                   = get_id,
            username                             = get_username,
            tanggal                              = get_tanggal,
            no_urut                              = get_no_urut,
            no_takah                             = get_no_takah,
            kepada                               = get_kepada,
            perihal                              = get_perihal,
            keterangan                           = get_keterangan,
            bagian                               = get_bagian,
            catatan                              = get_catatan,
            upload_file                          = files_upload_isi_surat_biasa

        )
        
        filter_nomor_tersedia_isi_surat_biasa_save.save()
        return redirect('filter_biasa_nomor_tersedia')



#### Untuk Edit Surat Biasa      ########
    
@login_required(login_url="/accounts/login/")
def biasa_edit_surat_biasa(request):
    edit_surat_biasa                              =  Biasa.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''))
    context = {
        'page_title'          : 'Biasa - Edit Surat Biasa',
        'edit_surat_biasa'    :  edit_surat_biasa
    }
    return render (request , 'surat_keluar/pages/biasa/edit_surat_biasa_pages/edit_surat_biasa.html', context )


@login_required(login_url="/accounts/login/")
def edit_surat_biasa_edit_surat(request, id_edit_surat_biasa_edit_surat):
    edit_surat_biasa_edit_surat                      =  get_object_or_404(Biasa, pk = id_edit_surat_biasa_edit_surat)
    username                                         =  request.user

    try:
        if request.method == 'POST':
            get_id                                   = id_edit_surat_biasa_edit_surat
            get_username                             = str(username)
            get_tanggal                              = edit_surat_biasa_edit_surat.tanggal
            get_no_urut                              = edit_surat_biasa_edit_surat.no_urut
            get_no_takah                             = request.POST.get('no_takah') 
            get_kepada                               = request.POST.get('kepada')
            get_perihal                              = request.POST.get('perihal') 
            get_keterangan                           = request.POST.get('keterangan')
            get_bagian                               = ""
            get_catatan                              = ""
            files_upload_edit_surat_biasa            = request.FILES.get('file_name')

            file_data_surat_biasa                    = edit_surat_biasa_edit_surat.upload_file.name

            if  files_upload_edit_surat_biasa == None:
                data_files_upload  = file_data_surat_biasa

            else:
                data_files_upload = files_upload_edit_surat_biasa
                edit_surat_biasa_edit_surat.upload_file.delete()

            edit_nomor_nota_dinas = Biasa(

                id                                   = get_id,
                username                             = get_username,
                tanggal                              = get_tanggal,
                no_urut                              = get_no_urut,
                no_takah                             = get_no_takah,
                kepada                               = get_kepada,
                perihal                              = get_perihal,
                keterangan                           = get_keterangan,
                bagian                               = get_bagian,
                catatan                              = get_catatan,
                upload_file                          = data_files_upload
                
                )
            
            edit_nomor_nota_dinas.save()
            return redirect('biasa_edit_surat_biasa')
        
        return render (request , 'surat_keluar/pages/biasa/edit_surat_biasa_pages/edit_surat_biasa.html')
    except:
        return render (request , 'surat_keluar/pages/biasa/edit_surat_biasa_pages/edit_surat_biasa.html')



@login_required(login_url="/accounts/login/")
def filter_edit_surat_biasa(request):
    tanggal_sekarang                             =  date.today()
    filter_edit_surat_biasa                      =  Biasa.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact='')) 
    
    try: 
        if request.method == 'POST':
            tanggal_sekarang_now                 =  request.POST.get('tanggal')
            edit_surat_biasa_filter              =  Biasa.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact='') , tanggal = tanggal_sekarang_now)
            tanggal                              =  parse_date(tanggal_sekarang_now)

        context = {
                'page_title'                     : 'Biasa - Filter Surat Biasa',
                'edit_surat_biasa_filter'        :  edit_surat_biasa_filter,
                'tgl_edit_surat_biasa'           :  tanggal 
            }
        
        return render (request , 'surat_keluar/pages/biasa/edit_surat_biasa_pages/filter_edit_surat_biasa.html', context )
    
    except:

        filter_edit_surat_biasa_data             = filter_edit_surat_biasa     
        
        context = {

                'page_title'                     :  'Biasa - Filter Surat Biasa',
                'edit_surat_biasa_filter'        :  filter_edit_surat_biasa_data ,
                'tgl_edit_surat_biasa'           :  tanggal_sekarang 

            }
        
        return render (request , 'surat_keluar/pages/biasa/edit_surat_biasa_pages/filter_edit_surat_biasa.html', context )
    

@login_required(login_url="/accounts/login/")
def filter_edit_surat_biasa_edit_surat(request, id_filter_edit_surat_biasa_edit_surat):
    filter_edit_surat_biasa_edit_surat               =  get_object_or_404(Biasa, pk = id_filter_edit_surat_biasa_edit_surat)
    username                                         =  request.user

    try:
        if request.method == 'POST':
            get_id                                   = id_filter_edit_surat_biasa_edit_surat
            get_username                             = str(username)
            get_tanggal                              = filter_edit_surat_biasa_edit_surat.tanggal
            get_no_urut                              = filter_edit_surat_biasa_edit_surat.no_urut
            get_no_takah                             = request.POST.get('no_takah') 
            get_kepada                               = request.POST.get('kepada')
            get_perihal                              = request.POST.get('perihal') 
            get_keterangan                           = request.POST.get('keterangan')
            get_bagian                               = ""
            get_catatan                              = ""
            files_upload_filter_edit_surat_biasa     = request.FILES.get('file_name')

            file_data_surat_biasa                    = filter_edit_surat_biasa_edit_surat.upload_file.name

            if  files_upload_filter_edit_surat_biasa == None:
                data_files_upload  = file_data_surat_biasa

            else:
                data_files_upload = files_upload_filter_edit_surat_biasa
                filter_edit_surat_biasa_edit_surat.upload_file.delete()

            filter_edit_nomor_nota_dinas = Biasa(

                id                                   = get_id,
                username                             = get_username,
                tanggal                              = get_tanggal,
                no_urut                              = get_no_urut,
                no_takah                             = get_no_takah,
                kepada                               = get_kepada,
                perihal                              = get_perihal,
                keterangan                           = get_keterangan,
                bagian                               = get_bagian,
                catatan                              = get_catatan,
                upload_file                          = data_files_upload
                
                )
            
            filter_edit_nomor_nota_dinas.save()
            return redirect('filter_edit_surat_biasa')
        
        return render (request , 'surat_keluar/pages/biasa/edit_surat_biasa_pages/filter_edit_surat_biasa.html')
    except:
        return render (request , 'surat_keluar/pages/biasa/edit_surat_biasa_pages/filter_edit_surat_biasa.html')
