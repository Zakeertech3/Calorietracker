from django.contrib import admin
from .models import FoodItem, UserMealLog

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'carbs', 'protein', 'fats', 'calories']

@admin.register(UserMealLog)
class UserMealLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'food_item', 'date']
