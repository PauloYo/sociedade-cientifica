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


class AreaUpdate(BaseModel):
    nomArea: Optional[str] = None

class NovaPublicacao(BaseModel):
    codArea: str = ""
    nomTitPubl: str = ""
    numAnoPubl: str = ""
    dscTipoPubl: str = "artigo"
    autrs: list[dict] = []
    artg: dict = {}
    tese: dict = {}
    livr: dict = {}


class PublicacaoUpdate(BaseModel):
    nomTitPubl: Optional[str] = None
    numAnoPubl: Optional[str] = None
    dscTipoPubl: Optional[str] = None
    autrs: Optional[list[dict]] = None
    artg: Optional[dict] = None
    tese: Optional[dict] = None
    livr: Optional[dict] = None


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


class SoftwareUpdate(BaseModel):
    nomSoft: Optional[str] = None
    dscSoft: Optional[str] = None
    nomRespSoft: Optional[str] = None
    dscEquipSoft: Optional[str] = None
    dscUrlSoft: Optional[str] = None
    arqvs: Optional[list[dict]] = None
