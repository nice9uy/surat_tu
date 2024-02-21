from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from . models import NotaDinas
from django.db.models import Q
from datetime import datetime
from django.utils.dateparse import parse_date

# Create your views here.

@login_required(login_url="/accounts/login/")
def surat_keluar(request): 
    context = {
        'page_title'    : 'Surat Keluar',
    }
    return render (request , 'surat_keluar/pages/index.html', context )

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
        return redirect('bon_nomor')
    
    
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
           
    get_username                         =  request.user
    get_hari_ini                         =  date.today()
    get_no_urut                          =  get_no_akhir
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


































# @login_required(login_url="/accounts/login/")
# def filter_nomor_tersedia(request):
#     tanggal_sekarang                             =  date.today()
#     filter_nomor_tersedia                        =  NotaDinas.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ) , Q(bagian__isnull=False) &  Q(bagian__exact='' ) , tanggal = tanggal_sekarang  )
#     try:
#         if request.method == 'POST':
#             get_tgl_bon_nomor                    =  request.POST.get('tanggal')
#             nomor_tersedia                       =  NotaDinas.objects.filter( Q(no_takah__isnull=False) &  Q(no_takah__exact='' ) , Q(bagian__isnull=False) &  Q(bagian__exact='' ) , tanggal = get_tgl_bon_nomor)
#             tanggal                              =  parse_date(get_tgl_bon_nomor)
#         context = {
#                 'page_title'                     : 'Nota Dinas - No Tersedia',
#                 'filter_nomor_tersedia'          :  nomor_tersedia,
#                 'tgl_sekarang'                   :  tanggal 
#             }
#         return render (request , 'surat_keluar/pages/nota_dinas/filter_nomor_tersedia.html', context)
#     except:
#         filter_no_tersedia_1                     = filter_nomor_tersedia     
#         context = {
#                 'page_title'                     : 'Nota Dinas - No Tersedia',
#                 'filter_nomor_tersedia'          :  filter_no_tersedia_1 ,
#                 'tgl_sekarang'                   :  tanggal_sekarang 
#             }
#         return render (request , 'surat_keluar/pages/nota_dinas/filter_nomor_tersedia.html', context)












    

# @login_required(login_url="/accounts/login/")
# def bon_nomor_isi_nota_dinas(request, id_no_tersedia_isi_nota_dinas):
#     bon_nomor_isi_nota_dinas                     =  get_object_or_404(NotaDinas, pk = id_no_tersedia_isi_nota_dinas)
#     username                                     =  request.user

#     if request.method == 'POST':

#         get_id                                   = id_no_tersedia_isi_nota_dinas
#         get_username                             = str(username)
#         get_tanggal                              = bon_nomor_isi_nota_dinas.tanggal
#         get_no_urut                              = bon_nomor_isi_nota_dinas.no_urut
#         get_no_takah                             = request.POST.get('no_takah') 
#         get_kepada                               = request.POST.get('kepada')
#         get_perihal                              = request.POST.get('perihal') 
#         get_keterangan                           = request.POST.get('keterangan')
#         get_bagian                               = ""
#         get_catatan                              = ""
#         files_upload_bon_nomor                   = request.FILES.get('file_name')

#         bon_nomor_isi_nota_dinas_save    = NotaDinas(
#             id                                   = get_id,
#             username                             = get_username,
#             tanggal                              = get_tanggal,
#             no_urut                              = get_no_urut,
#             no_takah                             = get_no_takah,
#             kepada                               = get_kepada,
#             perihal                              = get_perihal,
#             keterangan                           = get_keterangan,
#             bagian                               = get_bagian,
#             catatan                              = get_catatan,
#             upload_file                          = files_upload_bon_nomor

#         )
        
#         bon_nomor_isi_nota_dinas_save.save()
#         return redirect('nomor_tersedia')


    
# @login_required(login_url="/accounts/login/")    
# def filter_nomor_tersedia_bon_nomor(request, id_filter_nomor_tersedia_bon_nomor):
   
#     filter_nomor_tersedia_isi_bon_nomor          =  get_object_or_404(NotaDinas, pk = id_filter_nomor_tersedia_bon_nomor)
#     username                                     =  request.user

#     if request.method == 'POST':

#         get_id                                   = id_filter_nomor_tersedia_bon_nomor
#         get_username                             = str(username)
#         get_tanggal                              = filter_nomor_tersedia_isi_bon_nomor.tanggal
#         get_no_urut                              = filter_nomor_tersedia_isi_bon_nomor.no_urut
#         get_no_takah                             = ""
#         get_kepada                               = ""
#         get_perihal                              = ""
#         get_keterangan                           = ""
#         get_bagian                               = request.POST.get('bagian')
#         get_catatan                              = request.POST.get('catatan')
#         files_upload_bon_nomor                   = filter_nomor_tersedia_isi_bon_nomor.upload_file


#         bon_nomor_isi_nota_dinas_save    = NotaDinas(
#             id                                   = get_id,
#             username                             = get_username,
#             tanggal                              = get_tanggal,
#             no_urut                              = get_no_urut,
#             no_takah                             = get_no_takah,
#             kepada                               = get_kepada,
#             perihal                              = get_perihal,
#             keterangan                           = get_keterangan,
#             bagian                               = get_bagian,
#             catatan                              = get_catatan,
#             upload_file                          = files_upload_bon_nomor

#         )
        
#         bon_nomor_isi_nota_dinas_save.save()    
#         return redirect('nomor_tersedia')
    
# @login_required(login_url="/accounts/login/")    
# def filter_nomor_tersedia_isi_nota_dinas(request, id_filter_nomor_tersedia_isi_nota_dinas):
   
#     filter_nomor_tersedia_isi_nota_dinas         =  get_object_or_404(NotaDinas, pk = id_filter_nomor_tersedia_isi_nota_dinas)
#     username                                     =  request.user

#     if request.method == 'POST':

#         get_id                                   = id_filter_nomor_tersedia_isi_nota_dinas
#         get_username                             = str(username)
#         get_tanggal                              = filter_nomor_tersedia_isi_nota_dinas.tanggal
#         get_no_urut                              = filter_nomor_tersedia_isi_nota_dinas.no_urut
#         get_no_takah                             = request.POST.get('no_takah') 
#         get_kepada                               = request.POST.get('kepada')
#         get_perihal                              = request.POST.get('perihal') 
#         get_keterangan                           = request.POST.get('keterangan')
#         get_bagian                               = ""
#         get_catatan                              = ""
#         files_upload_bon_nomor                   = request.FILES.get('file_name')


#         bon_nomor_isi_nota_dinas_save    = NotaDinas(
#             id                                   = get_id,
#             username                             = get_username,
#             tanggal                              = get_tanggal,
#             no_urut                              = get_no_urut,
#             no_takah                             = get_no_takah,
#             kepada                               = get_kepada,
#             perihal                              = get_perihal,
#             keterangan                           = get_keterangan,
#             bagian                               = get_bagian,
#             catatan                              = get_catatan,
#             upload_file                          = files_upload_bon_nomor

#         )
        
#         bon_nomor_isi_nota_dinas_save.save()    
#         return redirect('nomor_tersedia')

# @login_required(login_url="/accounts/login/")
# def no_tersedia_isi_nota_dinas(request, id_no_tersedia_isi_nota_dinas):
#     bon_nomor_isi_nota_dinas                     =  get_object_or_404(NotaDinas, pk = id_no_tersedia_isi_nota_dinas)
#     username                                     =  request.user

#     if request.method == 'POST':

#         get_id                                   = id_no_tersedia_isi_nota_dinas
#         get_username                             = str(username)
#         get_tanggal                              = bon_nomor_isi_nota_dinas.tanggal
#         get_no_urut                              = bon_nomor_isi_nota_dinas.no_urut
#         get_no_takah                             = request.POST.get('no_takah') 
#         get_kepada                               = request.POST.get('kepada')
#         get_perihal                              = request.POST.get('perihal') 
#         get_keterangan                           = request.POST.get('keterangan')
#         get_bagian                               = ""
#         get_catatan                              = ""
#         files_upload_bon_nomor                   = request.FILES.get('file_name')

#         bon_nomor_isi_nota_dinas_save    = NotaDinas(
#             id                                   = get_id,
#             username                             = get_username,
#             tanggal                              = get_tanggal,
#             no_urut                              = get_no_urut,
#             no_takah                             = get_no_takah,
#             kepada                               = get_kepada,
#             perihal                              = get_perihal,
#             keterangan                           = get_keterangan,
#             bagian                               = get_bagian,
#             catatan                              = get_catatan,
#             upload_file                          = files_upload_bon_nomor

#         )
        
#         bon_nomor_isi_nota_dinas_save.save()
#         return redirect('nomor_tersedia')
    

    






# @login_required(login_url="/accounts/login/")
# def isi_nomor_tersedia(request, id_isi_nomor_tersedia):
#     bon_nomor_isi_nomor_tersedia                 = get_object_or_404(NotaDinas, pk = id_isi_nomor_tersedia)
#     username                                     = request.user

#     if request.method == 'POST':

#         get_id                                   = id_isi_nomor_tersedia
#         get_username                             = str(username)
#         get_tanggal                              = bon_nomor_isi_nomor_tersedia.tanggal
#         get_no_urut                              = bon_nomor_isi_nomor_tersedia.no_urut
#         get_no_takah                             = request.POST.get('no_takah') 
#         get_kepada                               = request.POST.get('kepada')
#         get_perihal                              = request.POST.get('perihal') 
#         get_keterangan                           = request.POST.get('keterangan')
#         get_bagian                               = bon_nomor_isi_nomor_tersedia.bagian
#         get_catatan                              = bon_nomor_isi_nomor_tersedia.catatan
#         files_upload_nomor_tersedia              = request.FILES.get('file_name')


#         data_bon_nomor                           = bon_nomor_isi_nomor_tersedia.upload_file.name

#         if  files_upload_nomor_tersedia == None:
#             files_upload_nomor_tersedia_bon_nomor= data_bon_nomor

#         else:
#             files_upload_nomor_tersedia_bon_nomor= files_upload_nomor_tersedia
#             bon_nomor_isi_nomor_tersedia.upload_file.delete()

#         nomor_tersedia_bon_nomor = NotaDinas(

#             id                      = get_id,
#             username                = get_username,
#             tanggal                 = get_tanggal,
#             no_urut                 = get_no_urut,
#             no_takah                = get_no_takah,
#             kepada                  = get_kepada,
#             perihal                 = get_perihal,
#             keterangan              = get_keterangan,
#             bagian                  = get_bagian,
#             catatan                 = get_catatan,
#             upload_file             = files_upload_nomor_tersedia_bon_nomor,
            
#             )

#         nomor_tersedia_bon_nomor.save()

#         return redirect('olah_nota_dinas')
 


# ####  Tambah Nomor Nota Dinas #####################################################

# def olah_nota_dinas(request):
#     tanggal_sekarang                             =  date.today()
#     olah_nota_dinas                              =  NotaDinas.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact='') , tanggal = tanggal_sekarang )

#     context = {
#         'page_title'                      : 'Nota Dinas - Olah Nota Dinas', 
#         'olah_nota_dinas'                 :  olah_nota_dinas,
#         'tanggal_sekarang'                :  tanggal_sekarang
#     }
#     return render (request , 'surat_keluar/pages/nota_dinas/olah_nota_dinas.html', context)


# def edit_olah_nota_dinas(request , id_edit_olah_nota_dinas ):
#     edit_olah_nota_dinas                         = get_object_or_404(NotaDinas, pk = id_edit_olah_nota_dinas)
#     username                                     = request.user

#     if request.method == 'POST':

#         get_id                                   = id_edit_olah_nota_dinas
#         get_username                             = str(username)
#         get_tanggal                              = edit_olah_nota_dinas.tanggal
#         get_no_urut                              = edit_olah_nota_dinas.no_urut
#         get_no_takah                             = request.POST.get('no_takah') 
#         get_kepada                               = request.POST.get('kepada')
#         get_perihal                              = request.POST.get('perihal') 
#         get_keterangan                           = request.POST.get('keterangan')
#         get_bagian                               = ""
#         get_catatan                              = ""
#         files_upload_olah_nota_dinas             = request.FILES.get('file_name')

#         data_olah_nota_dinas                     = edit_olah_nota_dinas.upload_file.name


#         if files_upload_olah_nota_dinas == None:
#            data_files_upload_olah_nota_dinas     = data_olah_nota_dinas

#         else:
#             data_files_upload_olah_nota_dinas    = files_upload_olah_nota_dinas
#             edit_olah_nota_dinas.upload_file.delete()

#         olah_nota_dinas_simpan  = NotaDinas(

#             id                      = get_id,
#             username                = get_username,
#             tanggal                 = get_tanggal,
#             no_urut                 = get_no_urut,
#             no_takah                = get_no_takah,
#             kepada                  = get_kepada,
#             perihal                 = get_perihal,
#             keterangan              = get_keterangan,
#             bagian                  = get_bagian,
#             catatan                 = get_catatan,
#             upload_file             = data_files_upload_olah_nota_dinas,
            
#             )

#         olah_nota_dinas_simpan.save()

#         return redirect('olah_nota_dinas')


# @login_required(login_url="/accounts/login/")
# def filter_edit_olah_nota_dinas_data(request , id_filter_edit_olah_nota_dinas_data):
#     filter_edit_olah_nota_dinas_data             = get_object_or_404(NotaDinas, pk = id_filter_edit_olah_nota_dinas_data)
#     username                                     = request.user

#     if request.method == 'POST':

#         get_id                                   = id_filter_edit_olah_nota_dinas_data
#         get_username                             = str(username)
#         get_tanggal                              = filter_edit_olah_nota_dinas_data.tanggal
#         get_no_urut                              = filter_edit_olah_nota_dinas_data.no_urut
#         get_no_takah                             = request.POST.get('no_takah') 
#         get_kepada                               = request.POST.get('kepada')
#         get_perihal                              = request.POST.get('perihal') 
#         get_keterangan                           = request.POST.get('keterangan')
#         get_bagian                               = ""
#         get_catatan                              = ""
#         files_upload_olah_nota_dinas             = request.FILES.get('file_name')

#         data_olah_nota_dinas                     = filter_edit_olah_nota_dinas_data.upload_file.name


#         if files_upload_olah_nota_dinas == None:
#            data_files_upload_olah_nota_dinas     = data_olah_nota_dinas

#         else:
#             data_files_upload_olah_nota_dinas    = files_upload_olah_nota_dinas
#             filter_edit_olah_nota_dinas_data.upload_file.delete()

#         olah_nota_dinas_simpan  = NotaDinas(

#             id                      = get_id,
#             username                = get_username,
#             tanggal                 = get_tanggal,
#             no_urut                 = get_no_urut,
#             no_takah                = get_no_takah,
#             kepada                  = get_kepada,
#             perihal                 = get_perihal,
#             keterangan              = get_keterangan,
#             bagian                  = get_bagian,
#             catatan                 = get_catatan,
#             upload_file             = data_files_upload_olah_nota_dinas,
            
#             )

#         olah_nota_dinas_simpan.save()

#         return redirect('olah_nota_dinas')





  
