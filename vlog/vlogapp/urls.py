from django.contrib import admin
from django.urls import path
from . import views


app_name= 'vlogapp'

urlpatterns = [
    path('arkadaslar/',views.arkadaşlar, name="arkadaslar"),
    path('',views.anasayfa, name="anasayfa"),
    path('notlar/',views.notlarım,name='notlarim'),
    path('tekce/',views.tekce,name='tekce'),
    path('omar/',views.omar,name='omar'),
    path('talip/',views.talip,name='talip'),
    path('isa/',views.isa,name='isa'),
    path('oyunlarim/',views.oyunlarim,name='oyunlarim'),
    path('dizivefilm/',views.dizivefilm,name='dizivefilm'),
    path('cyberpunk/',views.cyberpunk,name='cyberpunk'),
    path('godofwar/',views.godofwar,name='godofwar'),
    path('valorant/',views.valorant,name='valorant'),
    path('suyunönemi/',views.suyunönemi,name='suyunonemi'),
    path('teknoloji/',views.teknoloji,name='teknoloji'),
    path('kitap/',views.kitap,name='kitap'),
    path('korkukapani/',views.korkukapani,name='korkukapani'),
    path('batman/',views.batman,name='batman'),
    path('arcane/',views.arcane,name='arcane')
]