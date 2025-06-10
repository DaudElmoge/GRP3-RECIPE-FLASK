from flask_restful import Resource

class IngredientResource(Resource):
    def get(self, ingredients_id = None):
        if ingredients_id == None:
            return {"message": "List of ingredients"}
        else:
            return {"message": f"Ingredient with ID {ingredients_id} retrieved successfully"}
        
    def post(self):
        return {"messages": "Ingredient created successful"}
    
    def patch(self, ingredients_id):
        return {"message": f"Ingredient with ID {ingredients_id} updated successfully"}
    
    def delete(self, ingredients_id):
        return {"message": f"Ingredient with ID {ingredients_id} deleted successfully"}