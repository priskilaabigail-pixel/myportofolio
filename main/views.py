from django.shortcuts import render
from main.models import Experience, Mahasiswa


def show_main(request):
    mahasiswa_list = Mahasiswa.objects.all()
    context = {
        "name": "Priskila",
        "npm": "2506590252",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia in her third semester, who's "
            "always up for trying new hobbies and experiences. Because life is "
            "more than deadlines and doomscrolls."
        ),
        "mahasiswa_list": mahasiswa_list,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Priskila",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
