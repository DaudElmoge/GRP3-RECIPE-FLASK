# Simple Recipe App

## Models

- *User*
  - id
  - name
  - email
  - password
  - created_at

- *Recipe*
  - id
  - title
  - instructions
  - user_id
  - category_id
  - created_at
  - updated_at

- *Ingredient*
  - id
  - name
  - quantity
  - recipe_id

- *Category*
  - id
  - name
  - created_at

## Routes (CRUD)

### User

- POST /users – Create a user  
- GET /users – Get all users  
- GET /users/<id> – Get one user  
- PATCH /users/<id> – Update user  
- DELETE /users/<id> – Delete user  

### Recipe

- POST /recipes – Create a recipe  
- GET /recipes – Get all recipes  
- GET /recipes/<id> – Get one recipe  
- PATCH /recipes/<id> – Update recipe  
- DELETE /recipes/<id> – Delete recipe  

### Ingredient

- POST /ingredients – Create an ingredient  
- GET /ingredients – Get all ingredients  
- GET /ingredients/<id> – Get one ingredient  
- PATCH /ingredients/<id> – Update ingredient  
- DELETE /ingredients/<id> – Delete ingredient  

### Category

- POST /categories – Create a category  
- GET /categories – Get all categories  
- GET /categories/<id> – Get one category  
- PATCH /categories/<id> – Update category  
- DELETE /categories/<id> – Delete category

### Relationships
- A User can have many Recipes.

- A Recipe has many Ingredients.

- A Recipe can belong to many Categories, and vice versa (many-to-many).