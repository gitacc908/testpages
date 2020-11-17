from django.contrib import admin
from .models import Pages
# Register your models here.

class PagesAdmin(admin.ModelAdmin):
	list_display = ('title', 'update_date')
	ordering = ('title',)
	search_fields = ('title',)


admin.site.register(Pages, PagesAdmin)