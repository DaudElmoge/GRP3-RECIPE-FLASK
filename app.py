from flask import Flask



app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    return{"message": "Welcome to my recipe app"}

#create users
@app.post('/users')
def create_user():
    return {"message": "User created successfully"}

@app.get('/users')
def get_users():
    return {"message": "List of users"}

#get specific user by ID
@app.get('/users/<int:id>')
def get_user(id):
    return {"message": f"User with ID {id} retrieved successfully"}

@app.patch('/users/<int:id>')
def update_user(id):
    return {"message": f"User with ID {id} updated successfully"}

@app.delete('/users/<int:id>')
def delete_user(id):
    return {"message": f"User with ID {id} deleted successfully"}

#create recipes
@app.post('/recipes')
def create_recipe():
    return {"message": "Recipe created successfully"}

@app.get('/recipes')
def get_recipes():
    return {"message": "List of recipes"}

#get specific recipe by ID
@app.get('/recipes/<int:id>')
def get_recipe(id):
    return {"message": f"Recipe with ID {id} retrieved successfully"}

@app.patch('/recipes/<int:id>')
def update_recipe(id):
    return {"message": f"Recipe with ID {id} updated successfully"}

@app.delete('/recipes/<int:id>')
def delete_recipe(id):
    return {"message": f"Recipe with ID {id} deleted successfully"}

#ingriedients
@app.post('/ingredients')
def create_ingredient():
    return {"message": "Ingredient created successfully"}       

@app.get('/ingredients')
def get_ingredients():
    return {"message": "List of ingredients"}

@app.get('/ingredients/<int:id>')
def get_ingredient(id):
    return {"message": f"Ingredient with ID {id} retrieved successfully"}

@app.patch('/ingredients/<int:id>')
def update_ingredient(id):
    return {"message": f"Ingredient with ID {id} updated successfully"}

@app.delete('/ingredients/<int:id>')
def delete_ingredient(id):
    return {"message": f"Ingredient with ID {id} deleted successfully"}

#category
@app.post('/categories')
def create_category():
    return {"message": "Category created successfully"}

@app.get('/categories')
def get_categories():
    return {"message": "List of categories"}

@app.get('/categories/<int:id>')
def get_category(id):
    return {"message": f"Category with ID {id} retrieved successfully"}

@app.patch('/categories/<int:id>')
def update_category(id):
    return {"message": f"Category with ID {id} updated successfully"}

@app.delete('/categories/<int:id>')
def delete_category(id):
    return {"message": f"Category with ID {id} deleted successfully"}