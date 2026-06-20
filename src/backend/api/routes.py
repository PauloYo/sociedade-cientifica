from fastapi import APIRouter
from bson import json_util

from src.backend.api.controller.AreaController import AreaController
from src.backend.api.controller.PesquisaController import PesquisaController
from src.backend.api.controller.DocumentoController import DocumentoController
from src.backend.api.controller.SoftwareController import SoftwareController

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
def listar_todos():
    docController = DocumentoController()
    lista = docController.listar_todos()
    return { "status": "ok", "response": json_util.dumps(lista, ensure_ascii=False) }

@router.get("/pesquisas")
def listar_area():
    pesqController = PesquisaController()
    lista = pesqController.listar_todos()
    return { "status": "ok", "response": json_util.dumps(lista, ensure_ascii=False) }

@router.get("/areas")
def listar_area():
    areaController = AreaController()
    lista = areaController.listar_todos()
    return { "status": "ok", "response": json_util.dumps(lista, ensure_ascii=False) }

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
    return { "status": "ok", "response": json_utils.dump(lista, ensure_ascii=False) }

# Listagem - Filtro

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

