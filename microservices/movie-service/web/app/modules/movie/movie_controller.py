

from app.modules.utils import RpcClient
from flask import Blueprint, jsonify


bp = Blueprint("movie", __name__)

movie = {
    "name": "Duna",
    "category_id": 1,
}


def process_message_async(category_id):
    rpc_client = RpcClient()
    try:
        category_info = rpc_client.call(category_id)
        # Handle category_info, e.g., storing it for later retrieval
        return category_info
    finally:
        rpc_client.close()

import requests
@bp.get("/get/movie")
def get_movie():
    category_id = movie["category_id"]
    # category_info = Thread(target=process_message_async, args=(category_id,)).start()
    # rpc_client = RpcClient()             
    # try:
    #     category_info = rpc_client.call(category_id)
    #     movie["category"] = category_info
    # finally:
    #     rpc_client.close() 
    category_info = requests.get(url="http://docker-category:91/api/category")
    movie["category"] = category_info.json()
    return jsonify({"movie": movie})