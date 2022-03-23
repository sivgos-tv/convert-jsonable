import json
from typing import List, Dict, Union

def convert_to_jsonable_type(x):
    try:
        y = float(x)
        if int(y) == y:
            return int(y)
        return y
    except:
        return str(x)
        
def convert_jsonable(data: Union[Dict, List[Dict]]):
    if isinstance(data, list):
        for i in range(len(data)):
            if not (isinstance(data[i], dict) or isinstance(data[i], list)):
                raise 'Only supported list items : dict'
            data[i] = convert_jsonable(data)
    for key in data.keys():
        if isinstance(data[key], dict):
            data[key] = convert_jsonable(data[key])
        elif isinstance(data[key], list):
            for i in range(len(data[key])):
                if isinstance(data[key][i], dict) or sinstance(data[key][i], list):
                    data[key][i] = convert_jsonable(data[key][i])
                else:
                    data[key][i] = convert_to_jsonable_type(data[key][i])
        else:
            data[key] = convert_to_jsonable_type(data[key])
    return data
