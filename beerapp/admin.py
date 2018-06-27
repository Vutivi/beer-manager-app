from django.contrib import admin

# Register your models here.
from .models import Beer, Review

admin.site.register(Beer)
#admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('aroma', 'appearance', 'taste', 'overall')

admin.site.register(Review, ReviewAdmin)