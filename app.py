from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from models import db
from resources.users import UsersResource
from resources.recipe import RecipeResource
from resources.ingredients import IngredientResource
from resources.categories import CategoryResource


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipe.db"

app.config["SQLALCHEMY_ECHO"] = True

api = Api(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.route("/",methods=["GET"])
def index():
    return {"message":"Welcome to my recipe app"}

api.add_resource(UsersResource, "/users", "/users/<int:users_id>")
api.add_resource(RecipeResource, "/recipes", "/recipes/<int:recipes_id>")
api.add_resource(IngredientResource, "/ingredients", "/ingredients/<int:ingredients_id>")
api.add_resource(CategoryResource, "/categories", "/categories/<int:categories_id>")