from django.contrib import admin
from treebeard.forms import movenodeform_factory
from treebeard.admin import TreeAdmin
from accounts.models import Constants, JobPosition, User, Userjob
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from import_export.admin import ImportExportModelAdmin

class UserjobInline(admin.TabularInline):
    model = Userjob
    extra = 1
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [UserjobInline]
    search_fields = ("username", "telegram_user")
    list_display = ("username", "is_admin", "telegram_user")
    list_filter = ["username"]
    fieldsets = (
        ("المعلوات الشخصية", {"fields": ("username", "password", "telegram_user")}),
        (
            "هل هو مسسؤول",
            {
                "fields": ("is_admin",),
            },
        ),
    )



@admin.register(JobPosition)
class MyAdmin(TreeAdmin):
    form = movenodeform_factory(JobPosition)



@admin.register(Constants)
class Cons(ImportExportModelAdmin):
    pass

admin.site.unregister(Group)
