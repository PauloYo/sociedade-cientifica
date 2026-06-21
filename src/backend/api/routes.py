from fastapi import APIRouter

from src.backend.api.controller.AreaController import AreaController
from src.backend.api.controller.DocumentoController import DocumentoController
from src.backend.api.controller.PesquisaController import PesquisaController
from src.backend.api.controller.PublicacaoController import PublicacaoController
from src.backend.api.controller.SoftwareController import SoftwareController
from src.backend.api.utils.serializer import parse_mongo

router = APIRouter()

# Post

@router.post("/area")
def criar_area(item):
    # TODO
    return None

@router.post("/pesquisa")
def criar_pesquisa(item):
    # TODO
    return None

@router.post("/teses")
def criar_teses(item):
    # TODO
    return None

@router.post("/livros")
def criar_livros(item):
    # TODO
    return None

@router.post("/artigos")
def criar_artigos(item):
    # TODO
    return None

@router.post("/softwares-tutoriais")
def criar_softwares_tutoriais(item):
    # TODO
    return None

# Listagem

@router.get("/documentos")
def listar_documentos():
    docController = DocumentoController()
    lista = docController.listar_todos()
    return { "status": "ok", "response": parse_mongo(lista) }

@router.get("/pesquisas")
def listar_pesquisas():
    pesqController = PesquisaController()
    lista = pesqController.listar_todos()
    return { "status": "ok", "response": parse_mongo(lista) }

@router.get("/areas")
def listar_areas():
    areaController = AreaController()
    lista = areaController.listar_todos()
    return { "status": "ok", "response": parse_mongo(lista) }

@router.get("/teses")
def listar_teses():
    # TODO
    return None

@router.get("/livros")
def listar_livros():
    # TODO
    return None

@router.get("/artigos")
def listar_artigos():
    # TODO
    return None

@router.get("/softwares-tutoriais")
def listar_softwares_tutoriais():
    softwareController = SoftwareController()
    lista = softwareController.listar_todos()
    return { "status": "ok", "response": parse_mongo(lista) }

# Listagem - Filtro
@router.get("/documento/{idString}")
def busca_doc(idString):
    docController = DocumentoController()
    item = docController.busca_doc_por_id(idString)

    return { "dados": item }


@router.get("/documentos/{busca}")
def busca_geral(busca):

    areaController = AreaController()
    pesqController = PesquisaController()
    publController = PublicacaoController()
    softwareController = SoftwareController()

    areas = areaController.busca_doc_por_nome_area(busca)

    pesqsNome = pesqController.busca_doc_por_nome_desc_pesquisa(busca)
    pesqsEmail = pesqController.busca_doc_por_nome_email_crdn_pesquisa(busca)
    pesqsInst = pesqController.busca_doc_por_instituicao_crdn_pesquisa(busca)

    publsTitulo = publController.busca_doc_por_titulo_publicacao(busca)
    publsAutor = publController.busca_doc_por_nome_autor_publicacao(busca)

    softs = softwareController.busca_doc_por_nome_desc_software(busca)

    busca_geral = areas + pesqsNome + pesqsEmail + pesqsInst + publsTitulo + publsAutor + softs

    # Remove duplicados mantendo apenas um documento por ID único
    # vistos = set()
    # busca_geral_unica = []

    # for doc in [areas, pesqsNome, pesqsEmail, pesqsInst, publsTitulo, publsAutor, softs]:
    #     print(doc)
    #     # Se o documento tiver um _id e ele ainda não foi adicionado
    #     if doc:
    #         if doc.get("_id") not in vistos:
    #             print(doc.get("_id"))
    #             print(doc["_id"])
    #             vistos.add(doc["_id"])
    #             busca_geral_unica.append(doc)

    # return {
    #     # "response": json_util.dumps(busca_geral),
    #     "areas": areas,
    #     "pesqsNome": pesqsNome,
    #     "pesqsEmail": pesqsEmail,
    #     "pesqsInst": pesqsInst,
    #     "publsTitulo": publsTitulo,
    #     "publsAutor": publsAutor,
    #     "softs": softs
    # }
    return { "dados": busca_geral }

@router.get("/pesquisas/{area}")
def filtrar_pesquisas_area(area):
    # TODO
    return None

@router.get("/teses/{area}")
def filtrar_teses_area(area):
    # TODO
    return None

@router.get("/livros/{area}")
def filtrar_livros_area(area):
    # TODO
    return None

@router.get("/artigos/{area}")
def filtrar_artigos_area(area):
    # TODO
    return None

@router.get("/softwares-tutoriais/{area}")
def filtrar_softwares_tutoriais_area(area):
    # TODO
    return None
    
# Consultas - ID

@router.get("/area/{id}")
def buscar_area_id(id):
    
    return None

@router.get("/area/{nome}")
def buscar_area_nome(nome):
    # TODO
    return None

@router.get("/pesquisas/{id}")
def buscar_pesquisa(id):
    # TODO
    return None

@router.get("/teses/{id}")
def buscar_tese(id):
    # TODO
    return None

@router.get("/livros/{id}")
def buscar_livro(id):
    # TODO
    return None

@router.get("/artigos/{id}")
def buscar_artigo(id):
    # TODO
    return None

@router.get("/softwares-tutoriais/{id}")
def buscar_softwares_tutoriais(id):
    # TODO
    return None

