import json
from bson import json_util


# Converte cursor do MongoDB em lista de dicts Python via bson.json_util,
# resolvendo ObjectId, datetime e outros tipos BSON não serializáveis por json padrão.
def parse_mongo(cursor_or_list):
    return json.loads(json_util.dumps(list(cursor_or_list), ensure_ascii=False))
