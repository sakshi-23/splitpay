from flask import Blueprint,request
import json
mod_data = Blueprint('data', __name__)


@mod_data.route('/get-all-doctors')
def get_doctors():
    query = {}
    search_params = request.args.get("search_params")


@mod_data.route("/get-word-cloud/<int:num_words>/<int:only_entities>", methods=[ "POST"])
def get_word_cloud(num_words, only_entities):
    query = request.json["params"] if "params" in request.json and not request.json["params"] == None  else {}
