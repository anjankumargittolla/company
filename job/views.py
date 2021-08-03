"""To generate random password random module is imported"""
import random

"""To send the email to employees smtplib is imported"""
import smtplib

"""This is also for generate random password in the form of string"""
import string

"""auth model has the inbuilt function for login and logout"""
from django.contrib.auth import login, logout, get_user_model

"""From django.contrib.auth.decorators login_required is imported"""
from django.contrib.auth.decorators import login_required

"""To accessing the User model """
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

"""From forms all the model forms are imported"""
from .forms import RegisterForm, DesignationForm, TeamForm, ProjectForm, MailBoxForm, CompanyForm

"""From app models all the models are imported"""
from .models import Register, Employee, Team, MailBox, Project

""" from django.db import connection to use raw queries """
from django.db import connection


# Create your views here.


def home(request):
    """This is for home page"""
    return render(request, "job/home.html", {})


def set_company(request):
    """TO save the all the designations in the organisation"""
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "job/company.html", {"comp": CompanyForm()})
    else:
        form = CompanyForm()
        return render(request, "job/company.html", {"comp": form})


def set_designation(request):
    """TO save the all the designations in the organisation"""
    if request.method == "POST":
        form = DesignationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "job/designation.html", {"des": DesignationForm()})
    else:
        form = DesignationForm()
        return render(request, "job/designation.html", {"des": form})


def register(request):
    """For the Register table"""
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "job/register.html", {"register": RegisterForm()})
    else:
        form = RegisterForm()
        return render(request, "job/register.html", {"register": form})


def hr_status(request):
    """To check the designation of every user"""
    des = Employee.objects.get(employee=request.user)
    emp_des = des.emp_details.designation
    if emp_des.role == "CEO" or emp_des.role == "MANAGER" or emp_des.role == "HR":
        return True
    else:
        return False


def approval(request):
    if hr_status(request):
        reg = Register.objects.all()
        return render(request, "job/approval.html", {"list": reg})


def eligible(request):
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        return HttpResponse("ok")


def emp_details(request):
    """To enter the all the employee's details"""
    return render(request, "job/emp_details.html")


def emp_data(request):
    """For employee table to store the all the required details"""
    import pdb
    pdb.set_trace()
    st = Register.objects.get(emp_email=request.POST["email"])
    if request.method == 'POST' and st.is_verified:
        user = User.objects.create_user(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            username=request.POST['username'],
            email=request.POST["first_name"] + request.POST["last_name"] + st.comp_details.domain,
            password=request.POST['password'],
        )
        print(user.email)
        user.set_password('password')
        Employee.objects.create(emp_details=st,
                                employee=user,
                                salary=request.POST['salary'],
                                address=request.POST['address'],
                                )
        return HttpResponseRedirect('/job/home/')
    else:
        return HttpResponse("Approval is not given")


def emp_login(request):
    """To go login page to login"""
    return render(request, "job/login.html", {})


def forgot(request):
    """This view is responsible for set password"""
    return render(request, "job/forgot.html")


def replace(request):
    """This view for send the new password to the user"""
    if request.method == "POST":
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        n = 8
        res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase +
                                     string.digits, k=n))
        s.login("anjan2anju@gmail.com", "haianju02")
        message = "password is " + res
        s.sendmail("anjan2anju@gmail.com", request.POST["email"], message)
        user = User.objects.get(email=request.POST["email"])
        user.set_password('res')
        return render(request, "job/redirect.html", {})


@login_required(login_url='/job/login/')
def profile(request):
    """This view is responsible for display the employee details"""
    # import pdb
    # pdb.set_trace()
    emp = Employee.objects.get(employee=request.user)
    # team_details = Team.objects.get(team_members=emp)
    # print(team_details, "----------------------@@@@@@@@@@@")
    # mails = MailBox.objects.filter(sender=emp)
    # inbox = MailBox.objects.filter(receiver=emp)
    # project = Project.objects.get(teams=team_details)

    # print(mails, inbox, project, "-------")
    data = {
        'Name': emp.emp_details.emp_name,
        "Email": emp.employee.email,
        "Role": emp.emp_details.designation.role,
        "phone": emp.emp_details.phone,
        "qualification": emp.emp_details.qualification,
        "experience": emp.emp_details.experience,
        "profile_pic": emp.emp_details.profile_pic,
        "company" : emp.emp_details.comp_details.comp_name,
        # "team_name": team_details,
        # "sent": mails,
        # "inbox": inbox,
        "is_verified": emp.emp_details.is_verified,
        # "project": project,
    }
    if hr_status(request):
        return render(request, 'job/hr.html', {'primary': data})
    else:
        return render(request, 'job/show_details.html', {'primary': data})


def all_mails(request):
    """To display the all mails for current user"""
    emp = Employee.objects.get(employee=request.user)
    mails = MailBox.objects.filter(sender=emp)
    inbox = MailBox.objects.filter(receiver=emp)
    return render(request, "job/all_mails.html", {"inbox": inbox, "sent": mails})


def check(request):
    """This view is for check for whether the given email and password is matched or not"""
    usermod = get_user_model()
    if request.method == "POST":
        try:
            user = usermod.objects.get(email=request.POST['email'])
            print(user, "----------------------------------------")
        except usermod.DoesNotExist:
            return HttpResponse('employee credentials are not correct')
        else:
            if user.check_password(request.POST['password']):
                login(request, user)
                return profile(request)
            else:
                return HttpResponseRedirect("/job/login/")
    else:
        return render(request, 'job/login.html', {})


def emp_logout(request):
    """This view for logout functionality"""
    logout(request)
    return HttpResponseRedirect('/job/login/')


@login_required(login_url='/job/login/')
def emp_list(request):
    """To show the all the employees details in that organisation"""
    # import pdb
    # pdb.set_trace()
    user = request.user
    emp = Employee.objects.get(employee=user)
    # cursor = connection.cursor()
    # a = cursor.execute('''select * from job_employee
    # where id=(select id from job_register where id={})'''.format(emp.id))
    # b = a.fetchall()
    # print(b, "----------------------------------")
    reg = Register.objects.filter(comp_details=emp.emp_details.comp_details).values_list("id")
    new_list = Employee.objects.filter(emp_details__in=reg)
    return render(request, "job/emp_list.html", {"emp": new_list})

    # import pdb
    # pdb.set_trace()
    # user = request.user
    # emp = Employee.objects.get(employee=user)
    # comp = emp.emp_details.comp_details.comp_name
    # emp_all = Employee.objects.all()
    # new = []
    # for i in emp_all:
    #     if i.emp_details.comp_details.comp_name == comp:
    #         new.append(i)
    #     else:
    #         continue
    # # reg = Register.objects.filter(comp_details=emp.emp_details.comp_details)
    # return render(request, "job/emp_list.html", {"emp" : new})


@login_required(login_url='/job/login/')
def add_team(request):
    """To add the new team"""
    # import pdb
    # pdb.set_trace()
    if hr_status(request):
        user = request.user
        emp = Employee.objects.get(employee=user)
        reg = Register.objects.filter(comp_details=emp.emp_details.comp_details).values_list("id")
        new_list = Employee.objects.filter(emp_details__in=reg)
        return render(request, "job/team.html", {"team": new_list})
    else:
        return HttpResponse("Only HR and MANAGER can access this page")


def save_team(request):
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        Team.objects.create(team_name=request.POST["team_name"],
                            team_members=request.POST["team_members"])
        print(request.POST["team_members"])
        return HttpResponseRedirect("/job/team/")


@login_required(login_url='/job/login/')
def project(request):
    """To add the new project"""
    if hr_status(request):
        if request.method == "POST":
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "job/project.html", {"project": ProjectForm()})
        else:
            form = ProjectForm()
            return render(request, "job/project.html", {"project": form})
    else:
        return HttpResponse("Only HR and MANAGER can access this page")


@login_required(login_url='/job/login/')
def mailbox(request):
    """To send email from one employee to another"""
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        form = MailBoxForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "job/mailbox.html", {"mail": MailBoxForm()})
        else:
            return HttpResponse("form is invalid")
    else:
        form = MailBoxForm()
        return render(request, "job/mailbox.html", {"mail": form})
