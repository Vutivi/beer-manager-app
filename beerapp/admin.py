from django.contrib import admin

# Register your models here.
from .models import Beer, Review

#admin.site.register(Beer)
class BeerAdmin(admin.ModelAdmin):

	list_display = ('name','ibu', 'calories', 'abv', 'style', 'brewery_location')

	
#admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):

	list_display = ('beer','aroma', 'appearance', 'taste', 'overall')

admin.site.register(Review, ReviewAdmin)

admin.site.register(Beer, BeerAdmin)