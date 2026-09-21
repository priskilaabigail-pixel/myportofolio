from main.models import Experience, Mahasiswa, Certification, Project
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProjectForm


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

def show_certification(request):
    context = {
        "name": "Priskila",
        "certification_list": Certification.objects.all(),
    }
    return render(request, "certification.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Priskila",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Priskila",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")