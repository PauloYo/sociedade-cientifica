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

    def busca_publicacao_por_id(self, cod_publ):
        item = self.colecao.find_one(
            {"publicacao.codPubl": cod_publ},
            {"_id": 0, "codArea": 1, "nomArea": 1, "publicacao.$": 1}
        )
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

    def atualizar_publicacao(self, cod_publ, dados):
        update_fields = {}

        for campo in [
            "nomTitPubl",
            "numAnoPubl",
            "dscTipoPubl",
            "autrs",
            "artg",
            "tese",
            "livr"
        ]:
            if campo in dados:
                update_fields[f"publicacao.$[p].{campo}"] = dados[campo]

        if not update_fields:
            return {"matched": 0, "modified": 0, "message": "Nenhum campo para atualizar"}

        resultado = self.colecao.update_one(
            {"publicacao.codPubl": cod_publ},
            {"$set": update_fields},
            array_filters=[{"p.codPubl": cod_publ}]
        )

        return {
            "matched": resultado.matched_count,
            "modified": resultado.modified_count
        }

    def excluir_publicacao(self, cod_publ):
        resultado = self.colecao.update_one(
            {"publicacao.codPubl": cod_publ},
            {"$pull": {"publicacao": {"codPubl": cod_publ}}}
        )
        return {
            "matched": resultado.matched_count,
            "modified": resultado.modified_count
        }
