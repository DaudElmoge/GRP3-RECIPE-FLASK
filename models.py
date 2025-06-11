from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

metadata = MetaData()

db = SQLAlchemy(metadata = metadata)

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.Text, nullable = False)
    created_at = db.Column(db.TIMESTAMP)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.Text, nullable = False)
    email = db.Column (db.Text, nullable = False)
    password = db.Column (db.Text, nullable = False, unique = True)
    created_at = db.Column(db.TIMESTAMP)

class Recipe(db.Model):
    __tablename__= "recipes"

    id = db.Column (db.Integer, primary_key = True)
    title = db.Column (db.Text, nullable = False)
    instructions = db.Column (db.Text, nullable = False)
    user_id = db.Column (db.Integer, db.ForeignKey("users.id"), nullable = False)
    category_id = db.Column (db.Integer, db.ForeignKey("categories.id"))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column (db.TIMESTAMP)

class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column (db.Integer, primary_key = True)
    name = db.Column (db.Text, nullable = False)
    quantity = db.Column (db.Integer, nullable = False)
    recipe_id = db.Column (db.Integer, db.ForeignKey("recipes.id"))


