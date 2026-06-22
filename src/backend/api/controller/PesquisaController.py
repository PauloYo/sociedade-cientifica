from src.backend.api.database.connect import client
from src.utils.toJson import toJson

class PesquisaController:
    def __init__(self):
        self.db = client['db'] # Conectando ao banco sangue
        self.colecao = self.db['sociedade-cientifica'] 

    def listar_todos(self):
        itens = self.colecao.find(
            {},
            { "_id": 0, "codArea": 1, "nomArea": 1, "pesquisa": 1 }
        ).sort({ "nomArea": 1, "pesquisa.nomPesq": 1 })

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

    def busca_doc_por_nome_desc_pesquisa(self, nome):
        itens = self.colecao.find(
            { 
                "$or": [
                    { "pesquisa.nomPesq": { "$regex": nome, "$options": "i" }},
                    { "pesquisa.dscPesq": { "$regex": nome, "$options": "i" }}
                ]
            }
        ).sort({ "pesquisa.nomPesq": 1 })
        return toJson(itens)

    def busca_doc_por_nome_email_crdn_pesquisa(self, nome):
        itens = self.colecao.find(
            { 
                "$or": [
                    { "pesquisa.crdn.nomCrdn": { "$regex": nome, "$options": "i" }},
                    { "pesquisa.crdn.dscEmailCrdn": { "$regex": nome, "$options": "i" }}
                ]
            }
        ).sort({ "pesquisa.nomCrdn": 1 })
        return toJson(itens)

    def busca_doc_por_instituicao_crdn_pesquisa(self, inst):
        itens = self.colecao.find(
            { 
                "$or": [
                    { "pesquisa.crdn.nomInstCrdn": { "$regex": inst, "$options": "i" }},
                ]
            }
        ).sort({ "pesquisa.nomPesq": 1 })
        return toJson(itens)