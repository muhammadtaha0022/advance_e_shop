from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name','last_name','username','last_login','data_joined' ,'is_active']
    filter_horizontal =()
    list_display_links=('email', 'first_name','last_name')
    readonly_fields = ('last_login','data_joined' ,'is_active')
    ordering = [ '-data_joined']
    search_fields = ('username',)
    list_filter =()
    fieldsets =()
    list_per_page = 20
    save_on_top = True
admin.site.register(Account,AccountAdmin)

admin.site.site_header = "Great Kart"
admin.site.site_title = "We shop"
admin.site.index_title = "super market"