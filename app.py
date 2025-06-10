from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


from resources.users import UsersResource
from resources.recipe import RecipeResource
from resources.ingredients import IngredientResource
from resources.categories import CategoryResource


api.add_resource(UsersResource, "/users", "/users/<int:users_id>")
api.add_resource(RecipeResource, "/recipes", "/recipes/<int:recipes_id>")
api.add_resource(IngredientResource, "/ingredients", "/ingredients/<int:ingredients_id>")
api.add_resource(CategoryResource, "/categories", "/categories/<int:categories_id>")