from pydantic import BaseModel
from typing import Optional, Any, Dict

class NovaPesquisa(BaseModel):
    codArea: str = ""
    nomPesq: str = ""
    dscPesq: str = ""
    datInicPesq: str = ""
    datFimPrevPesq: str = ""
    datFimEfetPesq: str = ""
    nomCrdn: str = ""
    dscEmailCrdn: str = ""
    nomInstCrdn: str = ""
    dscLogradEndr: str = ""
    numLogradEndr: str = ""
    nomBairroEndr: str = ""
    nomCidEndr: str = ""
    sglUfEndr: str = ""
    numCepEndr: str = ""

class PesquisaUpdate(BaseModel):
    nomPesq: Optional[str] = None
    dscPesq: Optional[str] = None
    datInicPesq: Optional[str] = None
    datFimPrevPesq: Optional[str] = None
    datFimEfetPesq: Optional[str] = None
    crdn: Optional[Dict[str, Any]] = None

class NovaPublicacao(BaseModel):
    codArea: str = ""
    nomTitPubl: str = ""
    numAnoPubl: str = ""
    dscTipoPubl: str = "artigo"
    autrs: list[dict] = []
    artg: dict = {}
    tese: dict = {}
    livr: dict = {}


class NovaArea(BaseModel):
    nomArea: str = ""


class NovoSoftware(BaseModel):
    codArea: str = ""
    nomSoft: str = ""
    dscSoft: str = ""
    nomRespSoft: str = ""
    dscEquipSoft: str = ""
    dscUrlSoft: str = ""
    arqvs: list[dict] = []
