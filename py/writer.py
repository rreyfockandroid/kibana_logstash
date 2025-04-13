import os
import json

STORE = '/home/grzegorz/Projects/kibana_logstash/data/'

def write_to_file_as_jsons(filename: str, data: list[dict]):
    print(os.path.join(STORE, filename))
    with open(os.path.join(STORE, filename), "w") as file:
        for d in data:
            row = json.dumps(d)
            file.write(row)
            file.write('\n')