import json
from spartan import Spartans

def create_id(spartans_dict):
    if spartans_dict:
        current_id = int(max(spartans_dict.keys())) + 1
        return str(current_id)
    return "1"

def add(spartans_dict, spartan):
    spartan_id = create_id(spartans_dict)
    person = Spartans(
        spartan_id,
        spartan["first_name"],
        spartan["last_name"],
        spartan["birth_year"],
        spartan["birth_month"],
        spartan["birth_day"],
        spartan["course"],
        spartan["stream"]
        )
    spartans_dict[spartan_id] = person
    print(spartans_dict)
    return spartans_dict

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
