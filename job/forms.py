"""from django.forms import ModelForm to work with forms"""
from django.forms import ModelForm
"""All models have to import from app to use Modelforms"""
from .models import Employee, Register, Designation, Project, Team, MailBox, Company


class CompanyForm(ModelForm):
    """Modelform for CompanyForm"""
    class Meta:
        model = Company
        fields = "__all__"


class DesignationForm(ModelForm):
    """Modelform for DesignationForm"""
    class Meta:
        model = Designation
        fields = "__all__"


class RegisterForm(ModelForm):
    """Modelform for RegisterForm"""
    class Meta:
        model = Register
        fields = ['emp_name', 'emp_email', 'designation',
                  'gender', 'profile_pic', 'phone', 'qualification', 'experience', 'comp_details']


class EmployeeForm(ModelForm):
    """Modelform for EmployeeForm"""
    class Meta:
        model = Employee
        fields = "__all__"


class ProjectForm(ModelForm):
    """Modelform for ProjectForm"""
    class Meta:
        model = Project
        fields = "__all__"


class TeamForm(ModelForm):
    """Modelform for TeamForm"""
    class Meta:
        model = Team
        fields = "__all__"


class MailBoxForm(ModelForm):
    """Modelform for MailBoxForm"""
    class Meta:
        model = MailBox
        fields = "__all__"
