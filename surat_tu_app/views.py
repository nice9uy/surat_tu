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


    
    context = {
        'page_title' : 'Tambah Surat'
    }
    return render (request , 'pages/tambah_surat.html' , context )