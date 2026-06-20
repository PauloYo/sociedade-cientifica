from src.backend.api.database.connect import client

class SoftwareController:
    def __init__(self):
        self.db = client['db'] # Conectando ao banco sangue
        self.colecao = self.db['sociedade-cientifica'] 

    def listar_todos(self):
        # Ordenando por Nome da pesquisa ASC
        itens = self.colecao.find({},{ "_id": 0, "software": 1}).sort({ "software.nomSoft": 1})

        return itens

    def busca_id(self, id):
        item = self.colecao.find_one({'codArea': id}, {
            'codArea':0,
            'nomArea':1,
            'pesquisa':1,
            "publicacao": 1,
            "software": 1
        })
        return item
