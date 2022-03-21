import json
from spartan import Spartans

# def create_id(spartans_dict):
#     if spartans_dict:
#         current_id = int(max(spartans_dict.keys())) + 1
#         return str(current_id)
#     return "1"

def is_valid(api_data):
    if len(api_data["first_name"]) <= 2:
        return False
    if len(api_data["last_name"]) <= 2:
        return False
    if 1900 > int(api_data["birth_year"]) or int(api_data["birth_year"]) > 2004:
        return False
    if int(api_data["birth_month"]) <=0   or int(api_data["birth_month"]) > 12:
        return False
    if int(api_data["birth_day"]) <= 0 or int(api_data["birth_day"]) > 31:
        return False
    return True
    
def add(spartans_dict, api_data): # spartan is a dict (json data sent through postman)
    # spartan_id = create_id(spartans_dict)
    if is_valid(api_data):
        person = Spartans(
            api_data["spartan_id"],
            api_data["first_name"],
            api_data["last_name"],
            api_data["birth_year"],
            api_data["birth_month"],
            api_data["birth_day"],
            api_data["course"],
            api_data["stream"]
            )
        spartans_dict[api_data["spartan_id"]] = person
        print(spartans_dict)
        return spartans_dict
    else:
        return {}

def list(spartans_dict):
    spartans_json = {}
    for k,v in spartans_dict.items():
        spartans_json[k] = v.__dict__
    
    with open("spartanslog.txt", "at") as file_var:
        file_var.write("spartans list checked" + "\n")
        file_var.close()

    return json.dumps(spartans_json)

def remove(spartans_dict, spartan_id):
    spartans_dict.pop(spartan_id)
    print(spartans_dict)

    with open("spartanslog.txt", "at") as file_var:
        file_var.write("spartans removed" + "\n")
        file_var.close()
