from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserMealLog, FoodItem
from .forms import MealLogForm, FoodItemForm
from datetime import date

# Home page view
@login_required
def home(request):
    calorie_goal = 2000  # Default calorie goal

    # Handle meal logging
    if request.method == 'POST':
        form = MealLogForm(request.POST)
        if form.is_valid():
            meal_log = form.save(commit=False)
            meal_log.user = request.user
            meal_log.date = date.today()
            meal_log.save()
            return redirect('home')
    else:
        form = MealLogForm()

    # Fetch today's logged meals for the user
    today_logs = UserMealLog.objects.filter(user=request.user, date=date.today())

    # Nutritional breakdown
    total_carbs = sum(log.food_item.carbs for log in today_logs)
    total_protein = sum(log.food_item.protein for log in today_logs)
    total_fats = sum(log.food_item.fats for log in today_logs)

    # Progress bar calculation
    total_calories = sum(log.food_item.calories for log in today_logs)
    calorie_progress = min((total_calories / calorie_goal) * 100, 100)

    context = {
        'form': form,
        'today_logs': today_logs,
        'total_calories': total_calories,
        'calorie_goal': calorie_goal,
        'calorie_progress': calorie_progress,
        'total_carbs': total_carbs,
        'total_protein': total_protein,
        'total_fats': total_fats,
    }
    return render(request, 'myapp/home.html', context)


# View for managing food items
@login_required
def manage_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_food')
    else:
        form = FoodItemForm()

    food_items = FoodItem.objects.all()
    return render(request, 'myapp/manage_food.html', {'form': form, 'food_items': food_items})

# View for deleting a food item
@login_required
def delete_food(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)
    food.delete()
    return redirect('manage_food')
