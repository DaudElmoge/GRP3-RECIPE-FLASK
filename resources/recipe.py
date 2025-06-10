from flask_restful import Resource

class RecipeResource(Resource):
    def get(self, recipes_id = None):
        if recipes_id == None:
            return {"message": "List of recipes"}
        else:
            return {"message": f"Recipe with ID {recipes_id} retrieved successfully"}
        
    def post(self):
        return {"messages": "Recipe created successful"}
    
    def patch(self, recipes_id):
        return {"message": f"Recipe with ID {recipes_id} updated successfully"}
    
    def delete(self, recipes_id):
        return {"message": f"Recipe with ID {recipes_id} deleted successfully"}