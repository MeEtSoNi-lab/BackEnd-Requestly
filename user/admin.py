from django.contrib import admin
from .models import UserDetail, ticket, Branch
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = UserDetail
    list_display =('id','email','first_name', 'last_name','phone', 'province','modified_on')
    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("email", "password1", "password2", "first_name","last_name","phone","street_address","province"),
                },
            ),
        )
    fieldsets=UserAdmin.fieldsets
    list_display_links=('id','email','phone')
    search_fields = ('email','first_name','last_name','phone')
    list_per_page = 30

class TicketView(admin.ModelAdmin):
    list_display=('ticket_number','ticket_type','created_by', 'estimated_completion','modified_on','created_on')
    search_field=('ticket_number', 'ticket_type','created_by')
    list_per_page= 30


class BranchView(admin.ModelAdmin):
    list_display = ('branch_number', 'branch_name', 'branch_address', 'branch_phone')
    search_field = ('branch_number','branch_name','branch_city')
    list_per_page = 30

# admin.site.unregister(UserDetail)
admin.site.register(UserDetail, CustomUserAdmin)
admin.site.register(ticket,TicketView)

admin.site.unregister(Group)
Group._meta.verbose_name_plural = 'Groups/Brand'
admin.site.register(Group)

admin.site.register(Branch,BranchView)
