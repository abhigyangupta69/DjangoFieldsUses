from django.contrib import admin
from .models import JobApplication
from .models import CompanyApplication
from .models import Jobs

# admin.site.register(JobApplication)
admin.site.register(Jobs)
# admin.site.register(CompanyApplication)
# Register your models here.


@admin.register(JobApplication)
class JobAdmin(admin.ModelAdmin):
    ###########Display Field in Admin pannel###############
    list_display = JobApplication.DisplayFields
    list_filter = JobApplication.FilterFields
    search_fields = JobApplication.SearchFields

@admin.register(CompanyApplication)
class CompanyApplicationAdmin(admin.ModelAdmin):
    ###########Display Field in Admin pannel###############
    list_display = CompanyApplication.DisplayFields




