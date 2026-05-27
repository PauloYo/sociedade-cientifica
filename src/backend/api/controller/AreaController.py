from src.backend.api.database.connect import client

class AreaController:
    def __init__(self):
        self.db = client['db'] # Conectando ao banco sangue
        self.colecao = self.db['sociedadeCientifica'] 

    def criar(self, nome):

        new_item = {
            "nomArea": nome
            "pesquisa": []
            "publicacao": []
            "software": []
        }

        self.colecao.insert_one(new_item)
        
        return

    def busca_id(self, id):
        item = self.colecao.find_one({'codArea': id}, {
            'codArea':0,
            'nomArea':1,
            'pesquisa':1,
            "publicacao": 1,
            "software": 1
        })
        return item
