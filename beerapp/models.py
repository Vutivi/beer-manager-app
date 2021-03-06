from django.db.models import Avg, Sum
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

def validate_only_one_instance(obj):

	model = obj.__class__
	
	if (model.objects.count() > 0 and
			obj.id != model.objects.get().id):
			
			raise ValidationError("Can only create 1 beer instance per day.")

	
# Beer Model
class Beer(models.Model):

	name = models.CharField(max_length=100,default=None)
	
	ibu = models.IntegerField(null=False, default=30, validators=[MaxValueValidator(50), MinValueValidator(30)])
	
	calories = models.IntegerField(null=False, default=64, validators=[MaxValueValidator(198), MinValueValidator(64)])
	
	abv = models.FloatField(default=4.5, validators=[MaxValueValidator(6.2), MinValueValidator(4.5)])
	
	style = models.CharField(null=False, max_length=100,default=None)
	
	brewery_location = models.CharField(null=False, max_length=300,default=None)
	
	def overall_ratings(self):
		
		aroma_sum = Review.objects.filter(beer=self.id).aggregate(Sum('aroma'))
		
		appearance_sum = Review.objects.filter(beer=self.id).aggregate(Sum('appearance'))
		
		taste_sum = Review.objects.filter(beer=self.id).aggregate(Sum('taste'))
		
		count = Review.objects.filter(beer=self.id).count()
		
		try:
			return  (((aroma_sum.get("aroma__sum")/(5 * count))*10) + ((appearance_sum.get("appearance__sum")/(5 * count))*10) + (((taste_sum.get("taste__sum")/(10 * count))*10)))/ (3 * count)
		except:
			return 0
		
	def __str__(self):
		return self.name
		
	
		
	#def clean(self):
		#validate_only_one_instance(self)
	
# Review Model
class Review(models.Model):

	beer = models.ForeignKey(Beer, on_delete=models.CASCADE, default=None)
	
	aroma = models.IntegerField(null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
		
	appearance = models.IntegerField(null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
		
	taste = models.IntegerField(null=False, default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
	
	
	def __str__(self):
		return "for "+str(self.beer)
	
	
	def overall(self):
	
		average = (((self.aroma / 5) * 10)  + ((self.appearance  / 5) * 10) + self.taste)/3
		
		return average