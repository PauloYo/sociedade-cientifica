from src.backend.api.database.connect import client
from bson.objectid import ObjectId
from src.utils.toJson import toJson

class DocumentoController:
    def __init__(self):
        self.db = client['db'] # Conectando ao banco sangue
        self.colecao = self.db['sociedade-cientifica'] 

    def criar(self, dados):

        nova_pesquisa = {
            "codArea": gerar_cod(),
            "nomArea": dados['nomArea'],
            "pesquisa": [
                {
                    "codPesq": gerar_cod(),
                    "nomPesq": dados['nomPesq'],
                    "dscPesq": dados['dscPesq'],
                    "datInicPesq": dados['datInicPesq'],
                    "datFimPrevPesq": dados['datFimPrevPesq'],
                    "datFimEfetPesq": dados['datFimEfetPesq'],
                    "crdn": {
                        "nomCrdn": dados['nomCrdn'],
                        "dscEmailCrdn": dados['dscEmailCrdn'],
                        "nomInstCrdn": dados['nomInstCrdn'],
                        "endr": {
                            "dscLogradEndr": dados['dscLogradEndr'],
                            "numLogradEndr": dados['numLogradEndr'],
                            "nomBairroEndr": dados['nomBairroEndr'],
                            "nomCidEndr": dados['nomCidEndr'],
                            "sglUfEndr": dados['sglUfEndr'],
                            "numCepEndr": dados['numCepEndr']
                        }
                    }
                }
            ],
            "publicacao": [
                {
                    "codPubl": gerar_cod(), # Recomendado usar a sua função para gerar IDs únicos aqui também
                    "nomTitPubl": dados['nomTitPubl1'], # Diferenciados por índice caso venham múltiplos no mesmo formulário
                    "numAnoPubl": dados['numAnoPubl1'],
                    "dscTipoPubl": dados['dscTipoPubl1'], # Ex: "artigo"
                    "autrs": [
                        { "nomAutr": dados['nomAutr1'] }
                    ],
                    "artg": {
                        "nomPeriodArtg": dados['nomPeriodArtg'],
                        "numVolumeArtg": dados['numVolumeArtg'],
                        "numEdicArtg": dados['numEdicArtg']
                    }
                },
                {
                    "codPubl": gerar_cod(),
                    "nomTitPubl": dados['nomTitPubl2'],
                    "numAnoPubl": dados['numAnoPubl2'],
                    "dscTipoPubl": dados['dscTipoPubl2'], # Ex: "tese"
                    "autrs": [
                        { "nomAutr": dados['nomAutr2'] }
                    ],
                    "tese": {
                        "dscGrauTese": dados['dscGrauTese'],
                        "nomInstTese": dados['nomInstTese']
                    }
                }
            ],
            "software": [
                {
                    "codSoft": gerar_cod(),
                    "nomSoft": dados['nomSoft'],
                    "dscSoft": dados['dscSoft'],
                    "nomRespSoft": dados['nomRespSoft'],
                    "cont": {
                        "endr": {
                            "dscLogradEndr": dados['dscLogradEndrSoft'],
                            "numLogradEndr": dados['numLogradEndrSoft'],
                            "nomCidEndr": dados['nomCidEndrSoft'],
                            "sglUfEndr": dados['sglUfEndrSoft']
                        }
                    },
                    "dscEquipSoft": dados['dscEquipSoft'],
                    "dscUrlSoft": dados['dscUrlSoft'],
                    "arqvs": [
                        {
                            "nomArqv": dados['nomArqv'],
                            "dscCaminArqv": dados['dscCaminArqv']
                        }
                    ]
                }
            ]
        }

        self.colecao.insert_one(new_item)
        
        return

    def listar_todos(self):
        # Ordenando por Nome da pesquisa ASC
        itens = self.colecao.find({}).sort({ "pesquisa.nomPesq": 1 })

        return toJson(itens)

    def busca_doc_por_id(self, id_string):
        item = self.colecao.find_one({"_id": ObjectId(id_string)})
        return toJson(item)
