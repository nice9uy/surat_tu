from datetime import date
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . models import NotaDinas

# Create your views here.

@login_required(login_url="/accounts/login/")
def surat_keluar(request):
    context = {
        'page_title'    : 'Surat Keluar',
    }
    return render (request , 'surat_keluar/pages/index.html', context )


@login_required(login_url="/accounts/login/")
def nota_dinas(request):
    nota_dinas                     =  NotaDinas.objects.all()
    context = {
        'page_title'    : 'Nota Dinas',
        'nota_dinas'    :  nota_dinas
    }
    return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html', context)

@login_required(login_url="/accounts/login/")
def tanggal_nota_dinas(request):
    nota_dinas                     =  NotaDinas.objects.all()

    context = {
        'tgl_nota_dinas'   : nota_dinas
    }

    return render (request , 'surat_keluar/pages/nota_dinas/tanggal_nota_dinas.html', context)

@login_required(login_url="/accounts/login/")
def tambah_tanggal_nota_dinas(request):
    username                       =  request.user
    hari_ini                       =  date.today()
    tgl_nota_dinas                 =  NotaDinas.objects.filter(tanggal = hari_ini).values().count()
    nota_dinas                     =  NotaDinas.objects.all()

    print(nota_dinas)
    
    if tgl_nota_dinas  == 0 :
        save_to_no_agenda          =  NotaDinas(   
            username               =  username,
            tanggal                =  hari_ini,                        
        )
        save_to_no_agenda.save()
        return redirect('tambah_tanggal_nota_dinas')
    else:
        pass
    context = {
        'page_title'    : 'Nota Dinas',
        'hari_ini'      :  hari_ini,
        'nota_dinas'    :  nota_dinas
    }
    return render (request , 'surat_keluar/pages/nota_dinas/tanggal_nota_dinas.html', context)


@login_required(login_url="/accounts/login/")
def detail_nota_dinas(request , id_detail_nota_dinas):

    tanggal                          = list(NotaDinas.objects.filter(id = id_detail_nota_dinas ).values_list('tanggal' , flat=True))
    get_tanggal                      = tanggal[0]

    # print(get_tanggal)

    # username                       =  request.user
    # hari_ini                       =  date.today()
    # tgl_nota_dinas                 =  NotaDinas.objects.filter(tanggal = hari_ini).values().count()
    # nota_dinas                     =  NotaDinas.objects.all()
    
    # if tgl_nota_dinas  == 0 :
    #     save_to_no_agenda          =  NotaDinas(   
    #         username               =  username,
    #         tanggal                =  hari_ini,                        
    #     )
    #     save_to_no_agenda.save()
    #     return redirect('tambah_nota_dinas')
    # else:
    #     pass
    context = {
        'page_title'    : 'Nota Dinas',
        'tanggal'       :  get_tanggal
        # 'hari_ini'      :  hari_ini,
        # 'nota_dinas'    :  nota_dinas
    }
    return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas_detail.html', context)