from fastapi import APIRouter

from src.backend.api.controller.AreaController import AreaController
from src.backend.api.controller.DocumentoController import DocumentoController
from src.backend.api.controller.PesquisaController import PesquisaController
from src.backend.api.controller.PublicacaoController import PublicacaoController
from src.backend.api.controller.SoftwareController import SoftwareController
from src.backend.api.schemas import (
    AreaUpdate,
    NovaArea,
    NovaPesquisa,
    NovaPublicacao,
    NovoSoftware,
    PesquisaUpdate,
    PublicacaoUpdate,
    SoftwareUpdate,
)
from src.backend.api.utils.serializer import parse_mongo

router = APIRouter()


# --- POST (Create) ---

@router.post("/area")
def criar_area(dados: NovaArea):
    data = dados.model_dump()
    if (data.get("nomArea") == ""): return {"status": "error", "msg": "Dados inválidos"}
    ctrl = DocumentoController()
    id_ = ctrl.criar_documento(data)
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
@router.post("/software")
@router.post("/softwares")
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

@router.get("/publicacoes")
def listar_publicacoes():
    publController = PublicacaoController()
    result = publController.listar_todos()
    return {"status": "ok", "response": parse_mongo(result)}


@router.get("/areas")
def listar_areas():
    areaController = AreaController()
    lista = areaController.listar_todos()
    return {"status": "ok", "response": parse_mongo(lista)}


@router.get("/softwares-tutoriais")
@router.get("/software")
@router.get("/softwares")
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

@router.get("/pesquisa/{id}")
def buscar_pesquisa_id(id: str):
    pesqController = PesquisaController()
    item = pesqController.busca_pesquisa_por_id(id)
    return {"status": "ok", "response": parse_mongo(item) if item else None}

@router.get("/publicacao/{id}")
def buscar_publicacao_id(id: str):
    publController = PublicacaoController()
    item = publController.busca_publicacao_por_id(id)
    return {"status": "ok", "response": parse_mongo(item) if item else None}

@router.get("/softwares-tutoriais/{id}")
@router.get("/software/{id}")
@router.get("/softwares/{id}")
def buscar_software_id(id: str):
    softwareController = SoftwareController()
    item = softwareController.busca_software_por_id(id)
    return {"status": "ok", "response": parse_mongo(item) if item else None}

@router.put("/area/{id}")
@router.patch("/area/{id}")
def atualizar_area(id: str, dados: AreaUpdate):
    areaController = AreaController()
    resultado = areaController.atualizar_area(
        id=id,
        dados=dados.model_dump(exclude_none=True)
    )

    if resultado["matched"] == 0:
        return {"status": "error", "msg": "Área não encontrada ou nenhum campo enviado"}

    return {"status": "ok", "resultado": resultado}

@router.put("/pesquisa/{cod_area}/{cod_pesq}")
def atualizar_pesquisa(cod_area: str, cod_pesq: str, dados: PesquisaUpdate):
    try:
        pesqController = PesquisaController()
        resultado = pesqController.atualizar_pesquisa(
            cod_area=cod_area,
            cod_pesq=cod_pesq,
            dados=dados.dict(exclude_none=True)
        )

        if resultado["matched"] == 0:
            return {"status": "error", "msg": "Pesquisa não encontrada"}

        return {
            "message": "Pesquisa atualizada com sucesso",
            "resultado": resultado
        }

    except Exception as e:
        return {"status": "error", "msg": "Erro interno [500]"}

@router.put("/pesquisa/{id}")
@router.patch("/pesquisa/{id}")
def atualizar_pesquisa_id(id: str, dados: PesquisaUpdate):
    pesqController = PesquisaController()
    resultado = pesqController.atualizar_pesquisa_por_id(
        cod_pesq=id,
        dados=dados.model_dump(exclude_none=True)
    )

    if resultado["matched"] == 0:
        return {"status": "error", "msg": "Pesquisa não encontrada ou nenhum campo enviado"}

    return {"status": "ok", "resultado": resultado}

@router.put("/publicacao/{id}")
@router.patch("/publicacao/{id}")
def atualizar_publicacao_id(id: str, dados: PublicacaoUpdate):
    publController = PublicacaoController()
    resultado = publController.atualizar_publicacao(
        cod_publ=id,
        dados=dados.model_dump(exclude_none=True)
    )

    if resultado["matched"] == 0:
        return {"status": "error", "msg": "Publicação não encontrada ou nenhum campo enviado"}

    return {"status": "ok", "resultado": resultado}

@router.put("/softwares-tutoriais/{id}")
@router.patch("/softwares-tutoriais/{id}")
@router.put("/software/{id}")
@router.patch("/software/{id}")
@router.put("/softwares/{id}")
@router.patch("/softwares/{id}")
def atualizar_software_id(id: str, dados: SoftwareUpdate):
    softwareController = SoftwareController()
    resultado = softwareController.atualizar_software(
        cod_soft=id,
        dados=dados.model_dump(exclude_none=True)
    )

    if resultado["matched"] == 0:
        return {"status": "error", "msg": "Software não encontrado ou nenhum campo enviado"}

    return {"status": "ok", "resultado": resultado}
    
# --- DELETE (Remove) ---

@router.delete("/area/{id}")
def excluir_area(id: str):
    areaController = AreaController()
    resultado = areaController.excluir_area(id)

    if resultado["deleted"] == 0:
        return {"status": "error", "msg": "Área não encontrada"}

    return {"status": "ok", "resultado": resultado}

@router.delete("/pesquisa/{id}")
def excluir_pesquisa(id: str):
    pesqController = PesquisaController()
    resultado = pesqController.excluir_pesquisa(id)

    if resultado["matched"] == 0:
        return {"status": "error", "msg": "Pesquisa não encontrada"}

    return {"status": "ok", "resultado": resultado}

@router.delete("/publicacao/{id}")
def excluir_publicacao(id: str):
    publController = PublicacaoController()
    resultado = publController.excluir_publicacao(id)

    if resultado["matched"] == 0:
        return {"status": "error", "msg": "Publicação não encontrada"}

    return {"status": "ok", "resultado": resultado}

@router.delete("/softwares-tutoriais/{id}")
@router.delete("/software/{id}")
@router.delete("/softwares/{id}")
def excluir_software(id: str):
    softwareController = SoftwareController()
    resultado = softwareController.excluir_software(id)

    if resultado["matched"] == 0:
        return {"status": "error", "msg": "Software não encontrado"}

    return {"status": "ok", "resultado": resultado}

