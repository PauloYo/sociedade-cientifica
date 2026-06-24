import uuid
from datetime import datetime

from bson.objectid import ObjectId
from pymongo import ReturnDocument

from src.backend.api.database.connect import client
from src.utils.toJson import toJson


def _cod():
    return str(uuid.uuid4())[:8]


class DocumentoController:
    def __init__(self):
        self.db = client["db"]
        self.colecao = self.db["sociedade-cientifica"]

    def criar_documento(self, dados: dict) -> str:
        doc = {
            "codArea": _cod(),
            "nomArea": dados.get("nomArea", "Nova Área"),
            "pesquisa": [],
            "publicacao": [],
            "software": [],
            "created_at": datetime.now().isoformat(),
        }
        result = self.colecao.insert_one(doc)
        return str(result.inserted_id)

    def adicionar_pesquisa(self, dados: dict) -> bool:
        item = {
            "codPesq": _cod(),
            "nomPesq": dados.get("nomPesq", ""),
            "dscPesq": dados.get("dscPesq", ""),
            "datInicPesq": dados.get("datInicPesq", ""),
            "datFimPrevPesq": dados.get("datFimPrevPesq", ""),
            "datFimEfetPesq": dados.get("datFimEfetPesq", ""),
            "crdn": {
                "nomCrdn": dados.get("nomCrdn", ""),
                "dscEmailCrdn": dados.get("dscEmailCrdn", ""),
                "nomInstCrdn": dados.get("nomInstCrdn", ""),
                "endr": {
                    "dscLogradEndr": dados.get("dscLogradEndr", ""),
                    "numLogradEndr": dados.get("numLogradEndr", ""),
                    "nomBairroEndr": dados.get("nomBairroEndr", ""),
                    "nomCidEndr": dados.get("nomCidEndr", ""),
                    "sglUfEndr": dados.get("sglUfEndr", ""),
                    "numCepEndr": dados.get("numCepEndr", ""),
                },
            },
        }
        result = self.colecao.update_one(
            {"codArea": dados.get("codArea")},
            {"$push": {"pesquisa": item}},
        )
        return result.modified_count > 0

    def adicionar_publicacao(self, dados: dict) -> bool:
        pub = {
            "codPubl": _cod(),
            "nomTitPubl": dados.get("nomTitPubl", ""),
            "numAnoPubl": dados.get("numAnoPubl", ""),
            "dscTipoPubl": dados.get("dscTipoPubl", "artigo"),
            "autrs": dados.get("autrs", []),
        }
        tipo = dados.get("dscTipoPubl", "artigo")
        if tipo == "artigo":
            pub["artg"] = dados.get("artg", {})
        elif tipo == "tese":
            pub["tese"] = dados.get("tese", {})
        elif tipo == "livro":
            pub["livr"] = dados.get("livr", {})

        result = self.colecao.update_one(
            {"codArea": dados.get("codArea")},
            {"$push": {"publicacao": pub}},
        )
        return result.modified_count > 0

    def adicionar_software(self, dados: dict) -> bool:
        item = {
            "codSoft": _cod(),
            "nomSoft": dados.get("nomSoft", ""),
            "dscSoft": dados.get("dscSoft", ""),
            "nomRespSoft": dados.get("nomRespSoft", ""),
            "dscEquipSoft": dados.get("dscEquipSoft", ""),
            "dscUrlSoft": dados.get("dscUrlSoft", ""),
            "arqvs": dados.get("arqvs", []),
        }
        result = self.colecao.update_one(
            {"codArea": dados.get("codArea")},
            {"$push": {"software": item}},
        )
        return result.modified_count > 0

    def listar_todos(self):
        itens = self.colecao.find({}).sort({"pesquisa.nomPesq": 1})
        return toJson(itens)

    def busca_doc_por_id(self, id_string):
        item = self.colecao.find_one({"_id": ObjectId(id_string)})
        return toJson(item)

    def busca_geral_por_texto(self, texto):
        item = self.colecao.find(
            { 
                "$or": [
                    { "nomArea": { "$regex": texto, "$options": "i" }},
                    { "pesquisa.nomPesq": { "$regex": texto, "$options": "i" }},
                    { "pesquisa.dscPesq": { "$regex": texto, "$options": "i" }},
                    { "pesquisa.crdn.nomCrdn": { "$regex": texto, "$options": "i" }},
                    { "pesquisa.crdn.nomInstCrdn": { "$regex": texto, "$options": "i" }},
                    { "pesquisa.crdn.dscEmailCrdn": { "$regex": texto, "$options": "i" }},
                    { "publicacao.nomTitPubl": { "$regex": texto, "$options": "i" }},
                    { "publicacao.autrs.nomAutr": { "$regex": texto, "$options": "i" }},
                    { "software.nomSoft": { "$regex": texto, "$options": "i" }},
                    { "software.dscSoft": { "$regex": texto, "$options": "i" }}
                ]
            }
        )
        return toJson(item)