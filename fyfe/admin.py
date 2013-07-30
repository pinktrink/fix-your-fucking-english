from django.contrib import admin

from fyfe.models import Fix, Search

class SearchInline(admin.TabularInline):
	model = Search
	extra = 1

class FixAdmin(admin.ModelAdmin):
	inlines = [SearchInline]

admin.site.register(Fix, FixAdmin)
