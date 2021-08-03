from django.urls import path

from . import views

app_name = "job"

urlpatterns = [
    path("home/", views.home, name="homepage"),
    path("emp/", views.register, name="register"),
    path("des/", views.set_designation, name="designation"),
    path("approval/", views.approval, name="approval"),
    path("eligible/", views.eligible, name="eligible"),
    path("details/", views.emp_details, name="detail_entry"),
    path("save/", views.emp_data, name="save"),
    path("login/", views.emp_login, name="login_page"),
    path("check/", views.check, name="login_check"),
    path("logout/", views.emp_logout, name="logout"),
    path("list/", views.emp_list, name="employees_list"),
    path("forgot/", views.forgot, name="forgot"),
    path("replace/", views.replace, name="email_sent"),
    path("team/", views.add_team, name="team"),
    path("project/", views.project, name="project"),
    path("mails/", views.mailbox, name="mails"),
    path("profile/", views.profile, name="profile"),
    path("all_mails/", views.all_mails, name="all_mails"),
    path("company/", views.set_company, name="company"),
    path("save_team/", views.save_team, name="save_team"),
]
