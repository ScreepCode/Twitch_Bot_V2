import json

FILENAME = "libs/data/data.json"


def load_json(filename=FILENAME):
    with open(filename, encoding="UTF-8") as json_file:
        data = json.load(json_file)
        return data


def write_json(json_data, filename=FILENAME):
    json_string = json.dumps(json_data, indent=4, ensure_ascii=False)
    with open(filename, 'w', encoding="UTF-8") as outfile:
        outfile.write(json_string)


def update_json(key, new_data):
    data = load_json()
    data[key] = new_data
    write_json(data)


def get_relevant_information(topic):
    data = load_json()
    return data[topic]
