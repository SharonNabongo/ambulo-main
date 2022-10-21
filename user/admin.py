from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserChangeForm, UserCreationForm

# Register your models here.
class UserAdminConfig(UserAdmin):
    
    #add_form = UserCreationForm
    #form = UserChangeForm
    #model = User
    search_fields = ('email', 'username','first_name',)
    list_display = ('email','username','first_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'username','first_name', 'is_staff', 'is_active',)
    
    fieldsets = (
        (None, {'fields': ('email', 'username','first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields':('age','gender',)}),
    )
    add_fieldsets = (
        (None, { 'classes': ('wide',),
                'fields': ('email', 'username','first_name','password1','password2','is_staff', 'is_active',)}),
    )
    
    ordering = ('-date_joined',)
    
admin.site.register(User, UserAdminConfig)