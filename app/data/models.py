from flask import Blueprint,request
import json
mod_data = Blueprint('data', __name__)
from app.data.dbUtils import DBUtils


@mod_data.route('/get-all-doctors')
def get_doctors():
    query = {}
    search_params = request.args.get("search_params")
    collection = DBUtils().get_collection_obj('doximity')
    query_results = collection.find(query).limit(10)
    return json.dumps({"he":"ss"})


@mod_data.route("/get-word-cloud/<int:num_words>/<int:only_entities>", methods=[ "POST"])
def get_word_cloud(num_words, only_entities):
    query = request.json["params"] if "params" in request.json and not request.json["params"] == None  else {}
