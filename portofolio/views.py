from django.shortcuts import render
from main.models import Mahasiswa



def landing_page(request):
    mahasiswa_list = Mahasiswa.objects.all()
    return render(request, "index.html", {'mahasiswa_list': mahasiswa_list})