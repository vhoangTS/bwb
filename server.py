from flask import Flask, request, jsonify
from src.search import *
from src.auth import *


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello World! Flask server is up and running!'})


@app.route("/search-request", methods=['GET', 'POST'])
def search_with_payload():
    if request.is_json:
        payload = request.get_json()
        # Load dummy userdatabase
        database = load_dummy_user_database('src/database.pickle')
        # Authentication & authorization
        permission = get_user_role(payload['username'], payload['password'], database)
        r = {
            'permission': permission,
            'number-search-results': payload['nr_results'],
            'search-keyword': payload['keyword'],
            'search-data': ''
        }
        if check_login_data(payload['username'], payload['password'], database):
            # Search
            search_results = google_search(keyword=payload['keyword'], nr_results=payload['nr_results'])
            if permission == 'full':
                r['search-data'] = create_result_dict(search_results, get_all=True)
            elif permission == 'limited':
                r['search-data'] = create_result_dict(search_results, get_all=False)
            return r, 200
        else:
            r['code'] = "401: Unsuccessful authentication."
            return r, 401
    else:
        return {"error": "Wrong request format, must be JSON"}, 415


if __name__ == '__main__':
    app.run(debug=True)
