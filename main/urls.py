from django.urls import path

from main.views import show_main, show_experience, show_certification, create_project, show_projects, get_projects_json, delete_project, show_education, delete_education, create_education, get_education_json, edit_education, register, login_user, logout_user, project_toggle_star, create_project_ajax, education_toggle_star

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
    path("education/<uuid:education_id>/edit/", edit_education, name="edit_education"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path(
    "projects/<uuid:project_id>/star/",
    project_toggle_star,
    name="toggle_star"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path(
        "education/<uuid:education_id>/star/",
        education_toggle_star,
        name="education_toggle_star"),
]