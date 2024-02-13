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

###################  BON NOMOR               ##############################################
    
@login_required(login_url="/accounts/login/")    
def bon_nomor(request):
    bon_nomor                                =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''))

    context = {
        'page_title'                        : 'Nota Dinas',
        'bon_nomor'                         :  bon_nomor 
    }
    return render (request , 'surat_keluar/pages/nota_dinas/bon_nomor.html', context)

@login_required(login_url="/accounts/login/")
def filter_bon_nomor(request):
    filter_bon_nomor                            =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''))
    try:
        if request.method == 'POST':
            get_tgl_bon_nomor                    =  request.POST.get('tanggal')
            tanggal_bon_filter                   =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''), tanggal = get_tgl_bon_nomor)
            tanggal                              =  parse_date(get_tgl_bon_nomor)
        context = {
                'page_title'                     : 'Nota Dinas',
                'filter_bon_nomor'               :  tanggal_bon_filter,
                'tgl_bon_nomor'                  :  tanggal 
            }
        return render (request , 'surat_keluar/pages/nota_dinas/filter_bon_nomor.html', context)
    except:
        filter_bon_nomor_1                       = filter_bon_nomor     
        context = {
                'page_title'                     : 'Nota Dinas',
                'filter_bon_nomor'               :  filter_bon_nomor_1 
            }
        return render (request , 'surat_keluar/pages/nota_dinas/filter_bon_nomor.html', context)

@login_required(login_url="/accounts/login/")
def bon_nomor_isi_nota_dinas(request, id_bon_nomor_isi_nota_dinas):
    bon_nomor_isi_nota_dinas                     =  get_object_or_404(NotaDinas, pk = id_bon_nomor_isi_nota_dinas)
    username                                     =  request.user

    if request.method == 'POST':

        get_id                                   = id_bon_nomor_isi_nota_dinas
        get_username                             = str(username)
        get_tanggal                              = bon_nomor_isi_nota_dinas.tanggal
        get_no_urut                              = bon_nomor_isi_nota_dinas.no_urut
        get_no_takah                             = request.POST.get('bagian')
        get_kepada                               = request.POST.get('bagian')
        get_perihal                              = request.POST.get('bagian')
        get_keterangan                           = request.POST.get('bagian')
        get_bagian                               = ""
        get_catatan                              = ""
        files_upload_bon_nomor                   = bon_nomor_isi_nota_dinas.upload_file


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
    
################  NO tersedia ####################################################

@login_required(login_url="/accounts/login/")    
def nomor_tersedia(request):
    tanggal_sekarang                         =  date.today()
    bon_nomor                                =  NotaDinas.objects.filter( ~Q(no_takah__isnull=True) & ~Q(no_takah__exact='') , tanggal = tanggal_sekarang).values()

    context = {
        'page_title'                        : 'Nota Dinas',
        'bon_nomor'                         :  bon_nomor,
        'tanggal'                           :  tanggal_sekarang
    }
    return render (request , 'surat_keluar/pages/nota_dinas/nomor_tersedia.html', context)



def tambah_olah_nota_dinas(request):

    tanggal_sekarang                    =  date.today()
    nota_dinas                          =  NotaDinas.objects.filter(tanggal = tanggal_sekarang).values()
    #####################################################################################################
    try:
        no_urut_nota_dinas               = list(NotaDinas.objects.all().values_list('no_urut').last())
        nota_dinas_data                  = no_urut_nota_dinas[0]

        get_no_akhir                     = int(nota_dinas_data) + 1
    except:
        get_no_akhir  = 1
        
    #####################################################################################################   
        
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
        catatan                         = get_catatan,
        bagian                           = get_bagian,
        upload_file                      = get_upload_file
                 
    )

    SemuaNotaDinas_instance.save()

    context = {
        'page_title'        : 'Olah Nota Dinas',
        'tanggal'           :  get_hari_ini,
        'olah_nota_dinas'   :  nota_dinas
    }
    return render (request , 'surat_keluar/pages/nota_dinas/olah_nota_dinas.html', context)




####  Tambah Nomor Nota Dinas #####################################################

def olah_nota_dinas(request):
    olah_nota_dinas                       =  NotaDinas.objects.all()

    context = {
        'page_title'                      : 'Nota Dinas',
        'olah_nota_dinas'                 :  olah_nota_dinas 
    }
    return render (request , 'surat_keluar/pages/nota_dinas/olah_nota_dinas.html', context)



















    
# def bon_nomor(request):
#     # nota_dinas                           =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''))
#     nota_dinas                           =  NotaDinas.objects.all()

#     context = {
#         'page_title'                     : 'Nota Dinas',
#         'olah_nota_dinas'                :  nota_dinas 
#     }
#     return render (request , 'surat_keluar/pages/nota_dinas/bon_nomor.html', context)



# def bon_nomor_filter(request):
#     nota_dinas                               =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''))

#     try:
#         if request.method == 'POST':
#             get_tgl_nota_dinas                   = request.POST.get('tanggal')
#             tanggal_bon_filter                   =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''), tanggal = get_tgl_nota_dinas)
#             tanggal                              = parse_date(get_tgl_nota_dinas)

#         context = {
#                 'page_title'                     : 'Nota Dinas',
#                 'tanggal_bon_filter'             :  tanggal_bon_filter,
#                 'tanggal_nota_dinas'             :  tanggal 

#             }
#         return render (request , 'surat_keluar/pages/nota_dinas/bon_nomor_filter.html', context)
    
#     except:
#         datasurat_keluar                          = nota_dinas     
#         context = {
#                 'page_title'                     : 'Nota Dinas',
#                 'tanggal_bon_filter'             :  datasurat_keluar 
#             }
#         return render (request , 'surat_keluar/pages/nota_dinas/bon_nomor_filter.html', context)

# ##############################################################################################################3
# def filter_tanggal_no_tersedia(request):
#     nota_dinas                           =  NotaDinas.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ))
#     try:
#         if request.method == 'POST':
#             get_tgl_nota_dinas               = request.POST.get('tanggal')
#             data_nota_filter_tanggal         = NotaDinas.objects.filter( Q(no_takah__isnull=False) &  Q(no_takah__exact='' ), tanggal = get_tgl_nota_dinas).values()
#             tanggal                          = parse_date(get_tgl_nota_dinas)


#         context = {
#             'page_title'                    : 'Olah Nota Dinas',
#             'filter_tanggal_no_tersedia'    :  data_nota_filter_tanggal,
#             'tanggal_nota_dinas'            :  tanggal
#         }
#         return render (request , 'surat_keluar/pages/nota_dinas/filter_tanggal_nomor_tersedia.html' , context )
#     except:
#         datasurat_keluar = nota_dinas
#         context = {
#             'page_title'                   : 'Olah Nota Dinas',
#             'filter_tanggal_bon_nomor'    :  datasurat_keluar,
#             # 'tanggal_nota_dinas'           :  tanggal
#         }

#         return render (request , 'surat_keluar/pages/nota_dinas/filter_tanggal_nomor_tersedia.html' , context )


# ################### NO TERSEDIA ##########################
# def no_tersedia(request):
#     nota_dinas                           =  NotaDinas.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ))
#     # print(nota_dinas)
#     context = {
#         'page_title'                     : 'Nota Dinas',
#         'olah_nota_dinas'                :  nota_dinas 
#     }
#     return render (request , 'surat_keluar/pages/nota_dinas/nomor_tersedia.html', context)




# ################## BON NOMOR ####################################################################
# def bon_nomor_halaman(request):
#     nota_dinas                           =  NotaDinas.objects.all()

#     # print(nota_dinas)
#     context = {
#         'page_title'                     : 'Nota Dinas',
#         'olah_nota_dinas'                :  nota_dinas 
#     }
#     return render (request , 'surat_keluar/pages/nota_dinas/bon_nomor.html', context)

# def filter_tanggal_bon_nomor(request):
#     nota_dinas                               =  NotaDinas.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ))

#     try:
#         if request.method == 'POST':
#             get_tgl_nota_dinas               = request.POST.get('tanggal')
#             data_nota_filter_tanggal         = NotaDinas.objects.filter( Q(no_takah__isnull=False) &  Q(no_takah__exact='' ), tanggal = get_tgl_nota_dinas).values()
#             tanggal                          = parse_date(get_tgl_nota_dinas)

#         context = {
#             'page_title'                   : 'Olah Nota Dinas',
#             'filter_tanggal_nota_dinas'    :  data_nota_filter_tanggal,
#             'tanggal_nota_dinas'           :  tanggal
#         }
#         return render (request , 'surat_keluar/pages/nota_dinas/filter_tanggal_nomor_tersedia.html' , context )
#     except:
#         datasurat_keluar = nota_dinas
#         context = {
#             'page_title'                   : 'Olah Nota Dinas',
#             'filter_tanggal_nota_dinas'    :  datasurat_keluar,
#             # 'tanggal_nota_dinas'           :  tanggal
#         }

#         return render (request , 'surat_keluar/pages/nota_dinas/filter_tanggal_nomor_tersedia.html' , context )
# ######################################################################################################################

# def olah_nota_dinas(request):
#     # nota_dinas                      =  NotaDinas.objects.filter(~Q(no_takah__isnull=False) &  ~Q(no_takah__exact='') , ~Q(kepada__isnull=False) &  ~Q(kepada__exact='')  , ~Q(perihal__isnull=False) &  ~Q(perihal__exact='') , ~Q(keterangan__isnull=False) &  ~Q(keterangan__exact=''), ~Q(bagian__isnull=False) &  ~Q(bagian__exact=''), ~Q(catatan__isnull=False) &  ~Q(catatan__exact=''))
#     # nota_dinas                      =  NotaDinas.objects.all()
#     tanggal_sekarang                    =  date.today()
#     nota_dinas                          =  NotaDinas.objects.filter(tanggal = tanggal_sekarang).values()

#     context = {
#         'page_title'          : 'Nota Dinas',
#         'olah_nota_dinas'     :  nota_dinas,
#         'tanggal_sekarang'    : tanggal_sekarang
#     }
#     return render (request , 'surat_keluar/pages/nota_dinas/olah_nota_dinas.html', context)


# def no_tersedia(request):
#     nota_dinas                           =  NotaDinas.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ) , Q(bagian__isnull=False) &  Q(bagian__exact='' ) )
#     context = {
#         'page_title'                     : 'Nota Dinas',
#         'olah_nota_dinas'           :  nota_dinas 
#     }
#     return render (request , 'surat_keluar/pages/nota_dinas/nomor_tersedia.html', context)


# def tambah_olah_nota_dinas(request):
#     tanggal_sekarang                    =  date.today()
#     nota_dinas                          =  NotaDinas.objects.filter(tanggal = tanggal_sekarang).values()
#     #####################################################################################################
#     try:
#         no_urut_nota_dinas               = list(NotaDinas.objects.all().values_list('no_urut').last())
#         nota_dinas_data                  = no_urut_nota_dinas[0]

#         get_no_akhir                     = int(nota_dinas_data) + 1
#     except:
#         get_no_akhir  = 1
        
#     #####################################################################################################   
        
#     get_username                         =  request.user
#     get_hari_ini                         =  date.today()
#     get_no_urut                          =  get_no_akhir
#     get_no_takah                         =  ''
#     get_kepada                           =  ''
#     get_perihal                          =  ''
#     get_keterangan                       =  ''
#     get_catatan                          =  ''
#     get_bagian                           =  ''
#     get_upload_file                      =  ''

#     SemuaNotaDinas_instance = NotaDinas(   

#         username                         = get_username,
#         tanggal                          = get_hari_ini,
#         no_urut                          = get_no_urut,
#         no_takah                         = get_no_takah,
#         kepada                           = get_kepada,
#         perihal                          = get_perihal,
#         keterangan                       = get_keterangan,
#         catatan                         = get_catatan,
#         bagian                           = get_bagian,
#         upload_file                      = get_upload_file
                 
#     )

#     SemuaNotaDinas_instance.save()

#     context = {
#         'page_title'        : 'Olah Nota Dinas',
#         'tanggal'           :  get_hari_ini,
#         'olah_nota_dinas'   :  nota_dinas
#     }
#     return render (request , 'surat_keluar/pages/nota_dinas/olah_nota_dinas.html', context)


    
# def filter_bon_nomor(request):
#     # nota_dinas                               =  NotaDinas.objects.all()
#     tanggal_sekarang                         =  date.today()
#     nota_dinas                               =  NotaDinas.objects.filter(tanggal = tanggal_sekarang).values()

#     try:
#         if request.method == 'POST':
#             get_tgl_nota_dinas               = request.POST.get('tanggal')
#             data_nota_dinas                  = NotaDinas.objects.filter( tanggal = get_tgl_nota_dinas).values()
#         context = {
#             'page_title'                   : 'Olah Nota Dinas',
#             'nota_dinas'                   :  data_nota_dinas,
#             'tanggal_nota_dinas'           :  get_tgl_nota_dinas
#         }
#         return render (request , 'surat_keluar/pages/nota_dinas/filter_bon_nomor.html' , context )
#     except:
#         datasurat_keluar = nota_dinas
#         context = {
#             'page_title'                   : 'Olah Nota Dinas',
#             'nota_dinas'                   :  datasurat_keluar,
#             'tanggal_nota_dinas'           :  get_tgl_nota_dinas
#         }

#         return render (request , 'surat_keluar/pages/nota_dinas/filter_bon_nomor.html' , context )
    
# def filter_tanggal_olah_nota_dinas(request):
#     # nota_dinas                               =  NotaDinas.objects.all()
#     tanggal_sekarang                    =  date.today()
#     nota_dinas                          =  NotaDinas.objects.filter(tanggal = tanggal_sekarang).values()

#     try:
#         if request.method == 'POST':
#             get_tgl_nota_dinas               = request.POST.get('tanggal')
#             data_nota_dinas                  = NotaDinas.objects.filter( tanggal = get_tgl_nota_dinas).values()
#             tanggal                          = parse_date(get_tgl_nota_dinas)

#         context = {
#             'page_title'                   : 'Olah Nota Dinas',
#             'data_olah_nota_dinas'         :  data_nota_dinas,
#             'tanggal_nota_dinas'           :  tanggal,

#         }
#         return render (request , 'surat_keluar/pages/nota_dinas/filter_tanggal_olah_nota_dinas.html' , context )
#     except:
#         datasurat_keluar = nota_dinas
#         context = {
#             'page_title'                   : 'Olah Nota Dinas',
#             'data_olah_nota_dinas'         :  datasurat_keluar,
#             'tanggal_nota_dinas'           :  tanggal_sekarang
#         }

#         return render (request , 'surat_keluar/pages/nota_dinas/filter_tanggal_olah_nota_dinas.html' , context )


# ###########################################################################################################################
# def isi_nota_dinas(request, id_isi_nota_dinas):
#     edit_olah_nota_dinas  = get_object_or_404(NotaDinas, pk = id_isi_nota_dinas)
#     username              = request.user

#     if request.method == 'POST':

#         get_id                         = id_isi_nota_dinas
#         get_username                   = str(username)
#         get_tanggal                    = edit_olah_nota_dinas.tanggal
#         get_no_urut                    = edit_olah_nota_dinas.no_urut
#         get_no_takah                   = request.POST.get('no_takah') 
#         get_kepada                     = request.POST.get('kepada')
#         get_perihal                    = request.POST.get('perihal') 
#         get_keterangan                 = request.POST.get('keterangan')
#         get_bagian                     = edit_olah_nota_dinas.bagian
#         get_catatan                    = edit_olah_nota_dinas.catatan
#         files_upload_olah_nota_dinas   = request.FILES.get('file_name')


#         data_olah_nota_dinas           =  edit_olah_nota_dinas.upload_file.name

#         if  files_upload_olah_nota_dinas == None:
#             files_upload_olah_nota_dinas_final = data_olah_nota_dinas

#         else:
#             files_upload_olah_nota_dinas_final = files_upload_olah_nota_dinas
#             edit_olah_nota_dinas.upload_file.delete()

#         edit_olah_nota_dinas = NotaDinas(

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
#             upload_file             = files_upload_olah_nota_dinas_final,
            
#             )

#         edit_olah_nota_dinas.save()

#         return redirect('olah_nota_dinas')

# def bon_nomor_no_tersedia(request, id_bon_nomor_no_tersedia):

#     bon_nomor_no_yang_tersedia        = get_object_or_404(NotaDinas, pk = id_bon_nomor_no_tersedia)
#     username                          = request.user

#     if request.method == 'POST':

#         get_id                         = id_bon_nomor_no_tersedia
#         get_username                   = str(username)
#         get_tanggal                    = bon_nomor_no_yang_tersedia.tanggal
#         get_no_urut                    = bon_nomor_no_yang_tersedia.no_urut
#         get_no_takah                   = bon_nomor_no_yang_tersedia.no_takah
#         get_kepada                     = bon_nomor_no_yang_tersedia.kepada
#         get_perihal                    = bon_nomor_no_yang_tersedia.perihal
#         get_keterangan                 = bon_nomor_no_yang_tersedia.keterangan
#         get_bagian                     = request.POST.get('bagian')
#         get_catatan                    = request.POST.get('catatan')
#         files_upload_no_yang_tersedia  = bon_nomor_no_yang_tersedia.upload_file


#         edit_olah_nota_dinas = NotaDinas(

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
#             upload_file             = files_upload_no_yang_tersedia,
            
#             )
        
#         edit_olah_nota_dinas.save()
#         return redirect('no_tersedia')
    
# def isi_nota_dinas_bon_nomor(request):
#     pass