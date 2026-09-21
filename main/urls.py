from django.urls import path

from main.views import show_main, show_experience, show_certification, create_project, show_projects, get_projects_json, delete_project, show_education, delete_education, create_education, get_education_json

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("certification/", show_certification, name="show_certification"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("education/add/", create_education, name="create_education"),
    path("education/", show_education, name="show_education"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("api/education/", get_education_json, name="get_education_json"),
]