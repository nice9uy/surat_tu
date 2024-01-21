from datetime import date
from django.shortcuts import redirect, render
from . models import NotaDinas

# Create your views here.

def surat_keluar(request):
    context = {
        'page_title'    : 'Surat Keluar',
    }
    return render (request , 'surat_keluar/pages/index.html', context )


def nota_dinas(request):
    nota_dinas                     =  NotaDinas.objects.all()
    context = {
        'page_title'    : 'Nota Dinas',
        'nota_dinas'    :  nota_dinas
    }
    return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html', context)

def tambah_nota_dinas(request):
    username                       =  request.user
    hari_ini                       =  date.today()
    tgl_nota_dinas                 =  NotaDinas.objects.filter(tanggal = hari_ini).values().count()
    nota_dinas                     =  NotaDinas.objects.all()
    
    if tgl_nota_dinas  == 0 :
        save_to_no_agenda          =  NotaDinas(   
            username               =  username,
            tanggal                =  hari_ini,                        
        )
        save_to_no_agenda.save()
        return redirect('tambah_nota_dinas')
    else:
        pass
    context = {
        'page_title'    : 'Nota Dinas',
        'hari_ini'      :  hari_ini,
        'nota_dinas'    :  nota_dinas
    }
    return render (request , 'surat_keluar/pages/nota_dinas/nota_dinas.html', context)


def detail_nota_dinas(request , id_nota_dinas):

    tanggal                          = list(NotaDinas.objects.filter(id = id_nota_dinas ).values_list('tanggal' , flat=True))
    get_tanggal                      = tanggal[0]


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