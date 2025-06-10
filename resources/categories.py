from flask_restful import Resource

class CategoryResource(Resource):
    def get(self, categories_id = None):
        if categories_id == None:
            return {"message": "List of categories"}
        else:
            return {"message": f"Category with ID {categories_id} retrieved successfully"}
        
    def post(self):
        return {"messages": "Category created successful"}
    
    def patch(self, categories_id):
        return {"message": f"Category with ID {categories_id} updated successfully"}
    
    def delete(self, categories_id):
        return {"message": f"Category with ID {categories_id} deleted successfully"}