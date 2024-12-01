import csv
from flask import Flask, render_template, request

app = Flask(__RecipeRoulette__)

# Function to load recipes from CSV
def load_recipes_from_csv():
    recipes = []
    with open('E:/A/RecipeRoulette/indian_food.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming CSV columns are 'name' for the recipe and 'ingredients' for the list of ingredients
            name = row['name']
            ingredients = row['ingredients'].split(',')  # Assuming ingredients are comma-separated
            recipes.append({
                'name': name,
                'ingredients': [ingredient.strip() for ingredient in ingredients]  # Clean up any spaces
            })
    return recipes

# Load the recipes from the CSV file when the app starts
all_recipes = load_recipes_from_csv()

@app.route('/')
def index():
    """
    Render the homepage.
    """
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    """
    Process the ingredients input and display matching recipes from the CSV dataset.
    """
    ingredients = request.form.get('ingredients', '').lower()
    if not ingredients:
        return render_template('result.html', recipes=[])

    # Find recipes that match the given ingredients
    ingredient_list = [i.strip() for i in ingredients.split(',')]
    filtered_recipes = [
        recipe for recipe in all_recipes
        if any(ingredient.lower() in recipe['ingredients'] for ingredient in ingredient_list)
    ]

    return render_template('result.html', recipes=filtered_recipes)

@app.route('/meal-plan')
def meal_plan():
    """
    Render a page for meal planning and shopping list.
    """
    # Placeholder data for meal plans and shopping list
    meal_plan_data = {
        "Monday": "Pasta Primavera",
        "Tuesday": "Tacos",
        "Wednesday": "Vegetable Stir Fry"
    }
    shopping_list = ["pasta", "tomatoes", "zucchini", "tortilla", "beans", "salsa", "broccoli", "carrot", "soy sauce"]

    return render_template('meal_plan.html', meal_plan=meal_plan_data, shopping_list=shopping_list)

if __name__ == '__main__':
    app.run(debug=True)
