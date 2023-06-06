from django.db import models
from app_user.models import Client

# Create your models here.
# creation de la classe adstraite 

#  Dans notre model nous avons plusieurs nourriture dans un restauran et chaque nouture 
# et categoriser la relation de notre model est ONE TO MANY
class FoodCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name # Food category name
    
class Food(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField()
    description = models.TextField()
    foot_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.title}  {self.foot_category}" # Food title by category name
    

class Order(models.Model):
    date = models.DateField()
    number_food = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)