from src.backend.api.database.connect import client
from src.utils.toJson import toJson

class SoftwareController:
    def __init__(self):
        self.db = client['db'] # Conectando ao banco sangue
        self.colecao = self.db['sociedade-cientifica'] 

    def listar_todos(self):
        itens = self.colecao.find(
            {},
            { "_id": 0, "codArea": 1, "nomArea": 1, "software": 1 }
        ).sort({ "nomArea": 1, "software.nomSoft": 1 })

        return toJson(itens)

    def busca_id(self, id):
        item = self.colecao.find_one({'codArea': id}, {
            'codArea':0,
            'nomArea':1,
            'pesquisa':1,
            "publicacao": 1,
            "software": 1
        })
        return toJson(item)

    def busca_doc_por_nome_desc_software(self, nome):
        itens = self.colecao.find(
            { 
                "$or": [
                    { "software.nomSoft": { "$regex": nome, "$options": "i" }},
                    { "software.dscSoft": { "$regex": nome, "$options": "i" }}
                ]
            }
        ).sort({ "software.nomSoft": 1 })
        return toJson(itens)
