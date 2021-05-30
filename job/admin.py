from django.contrib import admin

from .models import Project, Employee, Register, Team, MailBox, Designation

# Register your models here.

admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Register)
admin.site.register(Team)
admin.site.register(MailBox)
admin.site.register(Designation)
