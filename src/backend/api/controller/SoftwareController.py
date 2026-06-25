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

    def busca_software_por_id(self, cod_soft):
        item = self.colecao.find_one(
            {"software.codSoft": cod_soft},
            {"_id": 0, "codArea": 1, "nomArea": 1, "software.$": 1}
        )
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

    def atualizar_software(self, cod_soft, dados):
        update_fields = {}

        for campo in [
            "nomSoft",
            "dscSoft",
            "nomRespSoft",
            "dscEquipSoft",
            "dscUrlSoft",
            "arqvs"
        ]:
            if campo in dados:
                update_fields[f"software.$[s].{campo}"] = dados[campo]

        if not update_fields:
            return {"matched": 0, "modified": 0, "message": "Nenhum campo para atualizar"}

        resultado = self.colecao.update_one(
            {"software.codSoft": cod_soft},
            {"$set": update_fields},
            array_filters=[{"s.codSoft": cod_soft}]
        )

        return {
            "matched": resultado.matched_count,
            "modified": resultado.modified_count
        }

    def excluir_software(self, cod_soft):
        resultado = self.colecao.update_one(
            {"software.codSoft": cod_soft},
            {"$pull": {"software": {"codSoft": cod_soft}}}
        )
        return {
            "matched": resultado.matched_count,
            "modified": resultado.modified_count
        }
