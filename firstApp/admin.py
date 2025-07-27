from django.contrib import admin

from firstApp.models import College, CustomUser, Student
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'established_year')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age', 'college', 'enrollment_date')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'full_name', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields':('full_name',)}),
        ('Permissions', {'fields':('is_staff', 'is_superuser', 'is_active',
                                   'groups', 'user_permissions')}),
        ('Dates', {'fields':('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email','full_name', 'password1','password2','is_staff','is_active','is_superuser')
        }),
    )
    search_fields = ('email','full_name')
    readonly_fields = ('last_login', 'date_joined')