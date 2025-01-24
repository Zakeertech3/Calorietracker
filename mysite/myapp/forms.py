from django import forms
from .models import UserMealLog, FoodItem
from django.core.exceptions import ValidationError

# Form for logging meals
class MealLogForm(forms.ModelForm):
    class Meta:
        model = UserMealLog
        fields = ['food_item']
        widgets = {
            'food_item': forms.Select(attrs={'class': 'form-control'}),
        }

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'carbs', 'protein', 'fats', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'carbs': forms.NumberInput(attrs={'class': 'form-control'}),
            'protein': forms.NumberInput(attrs={'class': 'form-control'}),
            'fats': forms.NumberInput(attrs={'class': 'form-control'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        carbs = cleaned_data.get('carbs')
        protein = cleaned_data.get('protein')
        fats = cleaned_data.get('fats')

        if carbs < 0 or protein < 0 or fats < 0:
            raise ValidationError("Nutritional values cannot be negative.")

        return cleaned_data