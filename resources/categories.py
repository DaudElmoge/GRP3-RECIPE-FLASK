from flask import request #allows access to http requests
from flask_restful import Resource
from models import Category, db

class CategoryResource(Resource):
    def get(self, categories_id = None):
        #Return all categories
        if categories_id == None:
            categories = Category.query.all()
            return [{
                "id":cat.id,
                "name":cat.name,
                "created_at":cat.created_at
            }
            for cat in categories
            ]
        else:#return a specific category using id
            category = Category.query.get(categories_id)
            if category:
                return {
                "id":category.id,
                "name":category.name,
                "created_at":category.created_at
            }
            return {"error":"Category not found"}
        
    def post(self):
        return {"messages": "Category created successful"}
    
    def patch(self, categories_id):
        return {"message": f"Category with ID {categories_id} updated successfully"}
    
    def delete(self, categories_id):
        return {"message": f"Category with ID {categories_id} deleted successfully"}