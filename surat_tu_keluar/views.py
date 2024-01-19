from django.shortcuts import render

# Create your views here.

def surat_keluar(request):
    return render (request , 'surat_keluar/pages/index.html')