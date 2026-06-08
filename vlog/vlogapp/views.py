from django.shortcuts import render

# Create your views here.
def anasayfa(request):
    return render(request,'vlogapp/anasayfa.html')
def arkadaşlar(request):
    return render(request,'vlogapp/arkadaslarim.html')

def dizifilmoneri(request):
    return render(request,'vlogapp/dizivefilmönerisi.html')

def notlarım(request):
    return render(request,'vlogapp/notlarim.html')

def iletisim(request):
    return render(request,'vlogapp/iletişim.html')

def tekce(request):
    return render(request,'vlogapp/tekce.html')

def omar(request):
    return render(request,'vlogapp/omar.html')

def talip(request):
    return render(request,'vlogapp/talip.html')

def isa(request):
    return render(request,'vlogapp/isa.html')

def oyunlarim(request):
    return render(request,'vlogapp/oyunlarim.html')


def dizivefilm(request):
    return render(request,'vlogapp/dizivefilm.html')

def cyberpunk(request):
    return render(request,'vlogapp/cyberpunk.html')


def godofwar(request):
    return render(request,'vlogapp/godofwar.html')

def valorant(request):
    return render(request,'vlogapp/valorant.html')

def suyunönemi(request):
    return render(request,'vlogapp/suyunönemi.html')


def teknoloji(request):
    return render(request,'vlogapp/teknoloji.html')

def kitap(request):
    return render(request,'vlogapp/kitap.html')

def korkukapani(request):
    return render(request,'vlogapp/korkukapani.html')

def batman(request):
    return render(request,'vlogapp/batman.html')

def arcane(request):
    return render(request,'vlogapp/arcane.html')


    