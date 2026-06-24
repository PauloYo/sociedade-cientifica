from fastapi import APIRouter

from src.backend.api.controller.AreaController import AreaController
from src.backend.api.controller.DocumentoController import DocumentoController
from src.backend.api.controller.PesquisaController import PesquisaController
from src.backend.api.controller.PublicacaoController import PublicacaoController
from src.backend.api.controller.SoftwareController import SoftwareController
from src.backend.api.schemas import NovaPesquisa, NovaPublicacao, NovoSoftware, NovaArea
from src.backend.api.utils.serializer import parse_mongo

router = APIRouter()


# --- POST (Create) ---

@router.post("/area")
def criar_area(dados: NovaArea):
    ctrl = DocumentoController()
    id_ = ctrl.criar_documento(dados.model_dump())
    return {"status": "ok", "id": id_}


@router.post("/documento")
def criar_documento(dados: dict):
    ctrl = DocumentoController()
    id_ = ctrl.criar_documento(dados)
    return {"status": "ok", "id": id_}


@router.post("/pesquisa")
def criar_pesquisa(dados: NovaPesquisa):
    ctrl = DocumentoController()
    ok = ctrl.adicionar_pesquisa(dados.model_dump())
    return {"status": "ok" if ok else "erro"}


@router.post("/publicacao")
def criar_publicacao(dados: NovaPublicacao):
    ctrl = DocumentoController()
    ok = ctrl.adicionar_publicacao(dados.model_dump())
    return {"status": "ok" if ok else "erro"}


@router.post("/softwares-tutoriais")
def criar_software(dados: NovoSoftware):
    ctrl = DocumentoController()
    ok = ctrl.adicionar_software(dados.model_dump())
    return {"status": "ok" if ok else "erro"}


# --- GET (List) ---

@router.get("/documentos")
def listar_documentos():
    docController = DocumentoController()
    lista = docController.listar_todos()
    return {"status": "ok", "response": parse_mongo(lista)}


@router.get("/pesquisas")
def listar_pesquisas():
    pesqController = PesquisaController()
    lista = pesqController.listar_todos()
    return {"status": "ok", "response": parse_mongo(lista)}


@router.get("/areas")
def listar_areas():
    areaController = AreaController()
    lista = areaController.listar_todos()
    return {"status": "ok", "response": parse_mongo(lista)}


@router.get("/softwares-tutoriais")
def listar_softwares_tutoriais():
    softwareController = SoftwareController()
    lista = softwareController.listar_todos()
    return {"status": "ok", "response": parse_mongo(lista)}


# --- GET (Detail / Search) ---

@router.get("/documento/{idString}")
def busca_doc(idString: str):
    docController = DocumentoController()
    item = docController.busca_doc_por_id(idString)
    return {"dados": parse_mongo(item)}

@router.get("/documentos/{busca}")
def busca_geral(busca):
    docController = DocumentoController()
    busca_geral = docController.busca_geral_por_texto(busca)
    return { "status": "ok", "dados": parse_mongo(busca_geral) }

@router.get("/area/{id}")
def buscar_area_id(id: str):
    areaController = AreaController()
    item = areaController.busca_id(id)
    return {"status": "ok", "response": parse_mongo(item) if item else None}
