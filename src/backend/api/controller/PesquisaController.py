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
    
    def atualizar_pesquisa(self, cod_area, cod_pesq, dados):
        update_fields = {}

        if "nomPesq" in dados:
            update_fields["pesquisa.$[p].nomPesq"] = dados["nomPesq"]

        if "dscPesq" in dados:
            update_fields["pesquisa.$[p].dscPesq"] = dados["dscPesq"]

        if "datInicPesq" in dados:
            update_fields["pesquisa.$[p].datInicPesq"] = dados["datInicPesq"]

        if "datFimPrevPesq" in dados:
            update_fields["pesquisa.$[p].datFimPrevPesq"] = dados["datFimPrevPesq"]

        if "datFimEfetPesq" in dados:
            update_fields["pesquisa.$[p].datFimEfetPesq"] = dados["datFimEfetPesq"]

        if "crdn" in dados:
            crdn = dados["crdn"]

            if "nomCrdn" in crdn:
                update_fields["pesquisa.$[p].crdn.nomCrdn"] = crdn["nomCrdn"]

            if "dscEmailCrdn" in crdn:
                update_fields["pesquisa.$[p].crdn.dscEmailCrdn"] = crdn["dscEmailCrdn"]

            if "nomInstCrdn" in crdn:
                update_fields["pesquisa.$[p].crdn.nomInstCrdn"] = crdn["nomInstCrdn"]

            if "endr" in crdn:
                endr = crdn["endr"]

                for campo in [
                    "dscLogradEndr",
                    "numLogradEndr",
                    "nomBairroEndr",
                    "nomCidEndr",
                    "sglUfEndr",
                    "numCepEndr"
                ]:
                    if campo in endr:
                        update_fields[f"pesquisa.$[p].crdn.endr.{campo}"] = endr[campo]

        if not update_fields:
            return {"message": "Nenhum campo para atualizar"}

        resultado = self.colecao.update_one(
            {
                "codArea": cod_area
            },
            {
                "$set": update_fields
            },
            array_filters=[
                {
                    "p.codPesq": cod_pesq
                }
            ]
        )

        return {
            "matched": resultado.matched_count,
            "modified": resultado.modified_count
        }