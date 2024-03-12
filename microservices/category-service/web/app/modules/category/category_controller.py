

from flask import Blueprint, jsonify

bp = Blueprint("category", __name__)

        
@bp.get("/api/category")
def get_category():
    return jsonify({"category": "This is a category", "id": 1})

# @bp.post("/add/category")
# def get_category():
#     category_data = request.json
#     if category_data is None:
#         return jsonify({"not"})      

#     message = json.dumps(category_data['category'])  
    
#     print("category_data", message)
#     publish_message('movie_queue', message)
#     return jsonify({"message": "Category published to movie service"}), 200



