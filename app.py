from src.search import *
from src.auth import *
import json


def response(request):
    response = {
        'code': '',
        'permission': '',
        'number-search-results': '',
        'search-keyword': '',
        'search-data': ''
    }
    # Load dummy userdatabase
    database = load_dummy_user_database('src/database.pickle')
    # Authentication & authorization
    permission = get_user_role(request['username'], request['password'], database)
    if check_login_data(request['username'], request['password'], database):
        response['code'] = "200: Sucessful authentication."
        # Search
        search_results = google_search(keyword=request['keyword'], nr_results=request['nr_results'])
        if permission == 'full':
            response['search-data'] = create_result_dict(search_results, get_all=True)
        elif permission == 'limited':
            response['search-data'] = create_result_dict(search_results, get_all=False)
    else:
        response['code'] = "401: Unsuccessful authentication."
    response['permission'] = permission
    response['search-keyword'] = request['keyword']
    response['number-search-results'] = request['nr_results']
    return response


def to_json(d):
    """
    Dump data into json format.

    :param d: Data as dictionary.
    """
    return json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False)


def to_json_file(d, file='response.json'):
    """
    Dump data into json output file.

    :param d: Data as dictionary.
    :param file: Export file name.
    """
    with open(file, 'w', encoding='utf_8_sig') as f:
        json.dump(d, f, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Request body
    payload = {
        'username': 'vhoang',
        'password': 'bar',
        'keyword': 'bosch',
        'nr_results': 10}

    # Output as json
    # r = to_json(response(payload))

    # Output to file
    to_json_file(response(payload))
