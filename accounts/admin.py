from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from accounts.models import SiwesInformation
from accounts.forms import UserAdminCreationForm, UserAdminChangeForm


# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('matric_number',  'full_name', 'email', 'session', 'College', 'department', 'level', 'timestamp',)
    list_filter = ('admin','is_active','timestamp')
    fieldsets = (
        (None, {'fields': ()}),
        ('Personal info', {'fields': ('matric_number',  'full_name', 'email', 'session', 'College', 'department', 'level','password',)}),
        ('Permissions', {'fields': ('admin','staff','is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('matric_number', 'full_name', 'email', 'session', 'College', 'department', 'level', 'password1', 'password2')}
        ),
    )
    search_fields = ('matric_number',)
    ordering = ('matric_number',)
    filter_horizontal = ()




class SiwesAdmin(admin.ModelAdmin):
    """
        The SiwesAdmin class styles the Admin Add and Change Siwes Information Form
    """

    list_display = ('user', 'bankName', 'accountNo', 'phoneNo', 'industryName', 'industryAddress', 'industrySupervisorname', 'industrySupervisorPhoneno')
    list_filter = ('bankName',)

    """
        The fieldsets styles the Admin Add and Change Siwes Information Form
    """
    fieldsets = (
        (None, {'fields': ()}),
        ('Add/Change Siwes Information', {'fields': ('user','bankName', 'accountNo', 'phoneNo', 'industryName', 'industryAddress', 'industrySupervisorname', 'industrySupervisorPhoneno')}),

    )
    search_fields   = ['accountNo']
    ordering = ('user',)
    filter_horizontal = ()

    class Meta:
        model = SiwesInformation






admin.site.register(get_user_model(), UserAdmin)
admin.site.register(SiwesInformation, SiwesAdmin)




# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

