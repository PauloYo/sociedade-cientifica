from fastapi import APIRouter
from controller.AreaController import AreaController

doadorController = DoadorController()

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

@router.get("/area")
def listar_area():
    # TODO
    return None

@router.get("/pesquisas")
def listar_pesquisas():
    # TODO
    return None 

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
    # TODO
    return None

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

