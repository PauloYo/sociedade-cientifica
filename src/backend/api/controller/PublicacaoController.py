from src.backend.api.database.connect import client
from src.utils.toJson import toJson

class PublicacaoController:
    def __init__(self):
        self.db = client['db'] # Conectando ao banco sangue
        self.colecao = self.db['sociedade-cientifica'] 

    def listar_todos(self):
        # Ordenando por Nome da pesquisa ASC
        itens = self.colecao.find(
            {},
            { "_id": 0, "publicacao": 1 }
        ).sort({ "publicacao.nomTitPubl": 1 })

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

    def busca_doc_por_titulo_publicacao(self, titulo):
        itens = self.colecao.find(
            { 
                "$or": [
                    { "publicacao.nomTitPubl": { "$regex": titulo, "$options": "i" }},
                ]
            }
        ).sort({ "publicacao.nomTitlPubl": 1 })
        return toJson(itens)

    def busca_doc_por_nome_autor_publicacao(self, nome):
        itens = self.colecao.find(
            { 
                "$or": [
                    { "publicacao.autrs.nomAutr": { "$regex": nome, "$options": "i" }},
                ]
            }
        ).sort({ "publicacao.nomTitlPubl": 1 })
        return toJson(itens)
