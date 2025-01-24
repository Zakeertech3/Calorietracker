from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Model for Food Items
class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    carbs = models.FloatField(help_text="Carbohydrates in grams")
    protein = models.FloatField(help_text="Protein in grams")
    fats = models.FloatField(help_text="Fats in grams")
    calories = models.FloatField(help_text="Calories in KCal")
    date_added = models.DateField(default=now)

    def __str__(self):
        return self.name

# Model for User Food Log
class UserMealLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.food_item.name} - {self.date}"
