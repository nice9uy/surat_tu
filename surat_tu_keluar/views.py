from datetime import date
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . models import NotaDinas
from django.db.models import Q
from datetime import datetime

# Create your views here.

@login_required(login_url="/accounts/login/")
def surat_keluar(request): 
    context = {
        'page_title'    : 'Surat Keluar',
    }
    return render (request , 'surat_keluar/pages/index.html', context )

@login_required(login_url="/accounts/login/")
def nota_dinas(request):
    nota_dinas                      =  NotaDinas.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''))
    context = {
        'page_title'    : 'Nota Dinas',
        'nota_dinas'    :  nota_dinas
    }
    return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html', context)


def olah_nota_dinas(request):
    # nota_dinas                      =  NotaDinas.objects.filter(~Q(no_takah__isnull=False) &  ~Q(no_takah__exact='') , ~Q(kepada__isnull=False) &  ~Q(kepada__exact='')  , ~Q(perihal__isnull=False) &  ~Q(perihal__exact='') , ~Q(keterangan__isnull=False) &  ~Q(keterangan__exact=''), ~Q(bagian__isnull=False) &  ~Q(bagian__exact=''), ~Q(catatan__isnull=False) &  ~Q(catatan__exact=''))
    nota_dinas                      =  NotaDinas.objects.filter(Q(no_takah__isnull=False) &  Q(no_takah__exact='' ))

    context = {
        'page_title'          : 'Nota Dinas',
        'olah_nota_dinas'     :  nota_dinas
    }
    return render (request , 'surat_keluar/pages/nota_dinas/olah_nota_dinas.html', context)

def bon_nomor(request):
    nota_dinas                           =  NotaDinas.objects.filter(~Q(bagian__isnull=True) & ~Q(bagian__exact=''))
    context = {
        'page_title'                     : 'Nota Dinas',
        'bon_nomor_nota_dinas'           :  nota_dinas
    }
    return render (request , 'surat_keluar/pages/nota_dinas/bon_nomor.html', context)


# def filter_bon_nomor(request):
#     nota_dinas                           =  NotaDinas.objects.filter(~Q(__isnull=True) & ~Q(bon_oleh__exact=''))
#     try:
#         if request.method == 'POST':
#             get_tgl_nota_dinas               = request.POST.get('tanggal')
#             data_nota_dinas                  = NotaDinas.objects.filter( tanggal = get_tgl_nota_dinas, ~Q(bon_oleh__isnull=True) & ~Q(bon_oleh__exact='')).values()
#         context = {
#             'page_title'                   : 'Olah Nota Dinas',
#             'bon_nomor_nota_dinas'         :  data_nota_dinas,
#             'tanggal_nota_dinas'           :  get_tgl_nota_dinas
#         }
#         return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html' , context )
#     except:
#         datasurat_keluar = nota_dinas
#         context = {
#             'page_title'                   : 'Olah Nota Dinas',
#             'bon_nomor_nota_dinas'         :  datasurat_keluar,
#             'tanggal_nota_dinas'           :  get_tgl_nota_dinas
#         }

#         return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html' , context )


def tambah_olah_nota_dinas(request):
    nota_dinas                          =  NotaDinas.objects.all()
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

def filter_nota_dinas(request):
    nota_dinas                               =  NotaDinas.objects.filter(~Q(no_takah__isnull=True) & ~Q(no_takah__exact=''))
    try:
        if request.method == 'POST':
            get_tgl_nota_dinas               = request.POST.get('tanggal')
            data_nota_dinas                  = NotaDinas.objects.filter( tanggal = get_tgl_nota_dinas).values()
        context = {
            'page_title'                   : 'Olah Nota Dinas',
            'nota_dinas'                   :  data_nota_dinas,
            'tanggal_nota_dinas'           :  get_tgl_nota_dinas
        }
        return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html' , context )
    except:
        datasurat_keluar = nota_dinas
        context = {
            'page_title'                   : 'Olah Nota Dinas',
            'nota_dinas'                   :  datasurat_keluar,
            'tanggal_nota_dinas'           :  get_tgl_nota_dinas
        }

        return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html' , context )
    
def filter_olah_nota_dinas(request):
    nota_dinas                               =  NotaDinas.objects.all()
    try:
        if request.method == 'POST':
            get_tgl_nota_dinas               = request.POST.get('tanggal')
            data_nota_dinas                  = NotaDinas.objects.filter( tanggal = get_tgl_nota_dinas).values()
            # x                                = datetime.strptime(get_tgl_nota_dinas, '%d/%m/%y')

            # print(type(xget_tgl_nota_dinas))

        context = {
            'page_title'                   : 'Olah Nota Dinas',
            'olah_nota_dinas'              :  data_nota_dinas,
            'tanggal_nota_dinas'           :  get_tgl_nota_dinas
        }
        return render (request , 'surat_keluar/pages/nota_dinas/olah_nota_dinas.html' , context )
    except:
        datasurat_keluar = nota_dinas
        context = {
            'page_title'                   : 'Olah Nota Dinas',
            'olah_nota_dinas'              :  datasurat_keluar,
            'tanggal_nota_dinas'           :  get_tgl_nota_dinas
        }

        return render (request , 'surat_keluar/pages/nota_dinas/olah_nota_dinas.html' , context )


















# @login_required(login_url="/accounts/login/")
# def tanggal_nota_dinas(request):
#     nota_dinas                     =  NotaDinas.objects.all()
#     context = {
#         'page_title'       : 'Nota Dinas',
#         'tgl_nota_dinas'   :  nota_dinas
#     } 
#     return render (request , 'surat_keluar/pages/nota_dinas/tanggal_nota_dinas.html', context)

# @login_required(login_url="/accounts/login/")
# def tambah_tanggal_nota_dinas(request):
#     username                       =  request.user
#     hari_ini                       =  date.today()
#     tgl_nota_dinas                 =  NotaDinas.objects.filter(tanggal = hari_ini).values().count()
    
#     if tgl_nota_dinas == 1:
#         return redirect('tanggal_nota_dinas')
#     else: 
#         save_to_no_agenda          =  NotaDinas(   
#             username               =  username,
#             tanggal                =  hari_ini,                        
#         )
#         save_to_no_agenda.save()
#         return redirect('tanggal_nota_dinas')


# @login_required(login_url="/accounts/login/")
# def tambah_detail_nota_dinas(request , id_tambah_detail_nota_dinas):
#     username                         =  request.user

#     id_nota_dinas                    = list(NotaDinas.objects.filter(id = id_tambah_detail_nota_dinas ).values_list('id' , flat=True))
#     get_id_nota_dinas                = id_nota_dinas[0]
#     no_urut_instance, created        = NotaDinas.objects.get_or_create(id = get_id_nota_dinas )
#     # no_akhir                         = SemuaNotaDinas.objects.all().values_list('no_urut' , flat=True).last()
#     # nota_dinas_nomor                 = SemuaNotaDinas.objects.all().values_list('id' , flat=True)


#     print(get_id_nota_dinas)

#     # if no_akhir ==  None:
    #     get_no_akhir                 = 1
    # else:
    #     get_no_akhir                 = int(no_akhir) + 1

    # SemuaNotaDinas_instance = SemuaNotaDinas(   

    #     id_semua_nota_dinas          = no_urut_instance,
    #     username                     = username,
    #     no_urut                      = get_no_akhir,
    #     no_takah                     = "",
    #     kepada                       = "",
    #     perihal                      = "",
    #     keterangan                   = "",
    #     bagian                       = "",
    #     catatan                      = "",
                 
    # )

    # SemuaNotaDinas_instance.save()

    # context = {
    #     'page_title'       : 'Detail Nota Dinas',
    #     # 'nota_dinas_nomor'          :  get_tanggal
    #     # 'hari_ini'      :  hari_ini,
    #     # 'nota_dinas'    :  nota_dinas
    # }

    # return render (request , 'surat_keluar/pages/nota_dinas/tambah_detail_nota_dinas.html',context)

# @login_required(login_url="/accounts/login/")
# def detail_nota_dinas(request):


#     # detail_nota_dinas                 =  SemuaNotaDinas.objects.all()

#     tanggal                           =  list(NotaDinas.objects.all().values_list('tanggal' , flat=True))
#     get_tanggal                       =  tanggal[0]

    


    # username                         =  request.user

    # id_nota_dinas                    = list(NotaDinas.objects.filter(id = id_tambah_detail_nota_dinas ).values_list('id' , flat=True))
    # tanggal                          = list(NotaDinas.objects.filter(id = id_tambah_detail_nota_dinas ).values_list('tanggal' , flat=True))

    # get_id_nota_dinas                = id_nota_dinas[0]
    # get_tanggal                      = tanggal[0]

    # no_urut_instance, created        = NotaDinas.objects.get_or_create(id = get_id_nota_dinas )
    # no_akhir                         = SemuaNotaDinas.objects.all().values_list('no_urut' , flat=True).last()

    # if no_akhir ==  None:
    #     get_no_akhir                 = 1
    # else:
    #     get_no_akhir                 = int(no_akhir) + 1

    # SemuaNotaDinas_instance = SemuaNotaDinas(   

    #     id_semua_nota_dinas          = no_urut_instance,
    #     username                     = username,
    #     no_urut                      = get_no_akhir,
    #     no_takah                     = "",
    #     kepada                       = "",
    #     perihal                      = "",
    #     keterangan                   = "",
    #     bagian                       = "",
    #     catatan                      = "",
                 
    # )

    # SemuaNotaDinas_instance.save()

    # context = {
    #     'page_title'        : 'Detail Nota Dinas',
    #     'detail_nota_dinas' :  detail_nota_dinas,
    #     'tanggal'           :  get_tanggal
    #     # 'hari_ini'      :  hari_ini,
    #     # 'nota_dinas'    :  nota_dinas
    # }

    # return render (request , 'surat_keluar/pages/nota_dinas/detail_nota_dinas.html', context)
  