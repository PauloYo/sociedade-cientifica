from src.backend.api.database.connect import client
from src.utils.toJson import toJson

class AreaController:
    def __init__(self):
        self.db = client['db'] # Conectando ao banco sangue
        self.colecao = self.db['sociedade-cientifica'] 

    def listar_todos(self):
        # Ordenando por Nome da pesquisa ASC
        itens = self.colecao.find(
            {},
            { "_id": 0, "codArea": 1, "nomArea": 1 }
        ).sort({ "nomArea": 1 })

        return toJson(itens)

    def busca_id(self, id):
        
        item = self.colecao.find_one({'codArea': id}, {
            'codArea':1,
            'nomArea':1,
            'pesquisa':1,
            "publicacao": 1,
            "software": 1
        })
        return toJson(item)

    def busca_doc_por_nome_area(self, nome):
        print("area: " + nome)
        itens = self.colecao.find(
            { 
                "$or": [
                    { "nomArea": { "$regex": nome, "$options": "i" }},
                ]
            }
        ).sort({ "nomArea": 1 })

        return toJson(itens)