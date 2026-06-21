from bson import json_util

def toJson(items):
    return json_util.dumps(items, ensure_ascii=False)