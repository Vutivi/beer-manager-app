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
	
	ibu = models.IntegerField(null=False, default=30, validators=[MaxValueValidator(30), MinValueValidator(50)])
	
	calories = models.IntegerField(null=False, default=64, validators=[MaxValueValidator(64), MinValueValidator(198)])
	
	abv = models.FloatField(default=4.5, validators=[MaxValueValidator(4.5), MinValueValidator(6.2)])
	
	style = models.CharField(null=False, max_length=100,default=None)
	
	brewery_location = models.CharField(null=False, max_length=300,default=None)
	
	def __str__(self):
		return self.name
		
	def clean(self):
		validate_only_one_instance(self)
	
# Review Model
class Review(models.Model):

	beer = models.ForeignKey(Beer, on_delete=models.CASCADE, default=None)
	
	aroma = models.IntegerField(null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
		
	appearance = models.IntegerField(null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
		
	taste = models.IntegerField(null=False, default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
	
	#Calculate overall
	def overall(self):
	
		average = (((self.aroma / 5) * 10)  + ((self.appearance  / 5) * 10) + self.taste)/3
		
		return average