from django.contrib import admin
from decision.form import DecisionForm, RecForm
from decision.models import Decision, Meeting, Rec,Recommendation
from import_export.admin import ImportExportModelAdmin
admin.site.site_header = "تطبيق المقررات"



class DecisionInline(admin.TabularInline):
    model=Decision
    form =DecisionForm
    extra = 0
  
class RecInline(admin.TabularInline):
    model=Rec
    fieldsets = (
                    ('', {'fields': ('id','title')}),
    )
    extra = 1

@admin.register(Recommendation)
class CustomRecAdmin(ImportExportModelAdmin):
    inlines=[RecInline]
    form =RecForm

@admin.register(Meeting)
class CustomMeetingAdmin(ImportExportModelAdmin):
    inlines=[DecisionInline]

# admin.site.register(Meeting, CustomMeetingAdmin)
# admin.site.register(, CustomRecAdmin)