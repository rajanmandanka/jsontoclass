
# covert json into object

import json

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace


class JsonObject:
    """
    :input json file or json data 
    :output: class object
    """
    def __init__(self, file_path=None, json_data=None) -> None:
        self.file_path = file_path  # "pipeline/facerec/properties.json"
        self.data = json_data
        
    def get_json(self):
        # Read json file and set in class data
        if self.file_path:
            with open(self.file_path, "r") as json_file:
                self.data = json.loads(json_file.read())
        return self.data


    def get_obj(self):
        if not self.data:
            self.get_json()
            
        # convert json to string
        str_json = json.dumps(self.data)
        
        # convert string to object
        obj = json.loads(str_json, object_hook=lambda d: Namespace(**d))

        return obj
        
