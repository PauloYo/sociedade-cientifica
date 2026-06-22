import json
from bson import json_util


# Converte saída do MongoDB (cursor ou string JSON via toJson) em dicts Python,
# resolvendo ObjectId, datetime e outros tipos BSON.
def parse_mongo(cursor_or_list):
    if isinstance(cursor_or_list, str):
        return json.loads(cursor_or_list)
    return json.loads(json_util.dumps(list(cursor_or_list), ensure_ascii=False))
