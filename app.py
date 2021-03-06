from textwrap import indent
from flask import Flask, request
import json
from management import add, remove, list, load_spartans

app = Flask(__name__)
spartans_file = 'spartans.json'
spartans_dict = {}
load_spartans(spartans_dict, spartans_file)
# Save file in json format in data.json
# 
@app.route('/')
# curl -X GET "http://localhost:5000/"
def home_page():
    return "How to use API"

@app.route('/spartan')
# curl -X GET "http://localhost:5000/spartan"
def spartans():
    # with open(spartans_file) as file:
    #     data = json.load(file)
    return list(spartans_dict)

@app.route('/spartan/add', methods=['POST'])
# curl -X POST "http://localhost:5000/spartan/add" -H 'Content-Type: application/json' -d '{"spartan_id": 100, "first_name": "John", "last_name": "Smith", "birth_year": 2000, "birth_month": "3", "birth_day": 1, "course": "dev", "stream": "tech"}'
def add_spartan():
    api_data = request.json
    result = add(spartans_dict, api_data)

    # with open(spartans_file) as file:
    #     spartans = json.load(file)
    # spartans.update(spartan)

    with open(spartans_file, 'w') as file:
        file.write(list(spartans_dict))

    # return list(spartans_dict)
    return f'Added Spartan with id: {api_data["spartan_id"]}'

@app.route('/spartan/remove', methods=['POST'])
# curl -X POST "http://localhost:5000/spartan/remove?id=2"
def remove_spartan():
    spartan_id = request.args.get('id')
    print(spartan_id)
    # with open(spartans_file) as file:
    #     spartans = json.load(file)
    print(spartans_dict)
    if spartan_id in spartans_dict:
        spartans_dict.pop(spartan_id)

        with open(spartans_file, 'w') as file:
            file.write(list(spartans_dict))

        # return list(spartans_dict)
        return f'Removed Spartan with id: {spartan_id}'
    return f'No Spartan with ID: {spartan_id}'

@app.route('/spartan/<spartan_id>')
# curl -X GET "http://localhost:5000/spartan/2"
def get(spartan_id):
    if spartan_id in spartans_dict:
        spartans_dict[spartan_id].__dict__
        return json.dumps(spartans_dict[spartan_id].__dict__)
    return f'No Spartan with ID: {spartan_id}'




if __name__ == '__main__':
    app.run(port=5000, debug=True)
