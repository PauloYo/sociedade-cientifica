from pydantic import BaseModel
from typing import Optional


class CoordenadorEndereco(BaseModel):
    dscLogradEndr: str = ""
    numLogradEndr: str = ""
    nomBairroEndr: str = ""
    nomCidEndr: str = ""
    sglUfEndr: str = ""
    numCepEndr: str = ""


class Coordenador(BaseModel):
    nomCrdn: str = ""
    dscEmailCrdn: str = ""
    nomInstCrdn: str = ""
    endr: CoordenadorEndereco = CoordenadorEndereco()


class NovaPesquisa(BaseModel):
    codArea: str
    nomPesq: str
    dscPesq: str = ""
    datInicPesq: str = ""
    datFimPrevPesq: str = ""
    datFimEfetPesq: str = ""
    crdn: Coordenador = Coordenador()


class ArtigoSub(BaseModel):
    nomPeriodArtg: str = ""
    numVolumeArtg: str = ""
    numEdicArtg: str = ""


class TeseSub(BaseModel):
    dscGrauTese: str = ""
    nomInstTese: str = ""


class LivroSub(BaseModel):
    edtr: dict = {}
    locPb: dict = {}


class Autor(BaseModel):
    nomAutr: str


class NovaPublicacao(BaseModel):
    codArea: str
    nomTitPubl: str
    numAnoPubl: str = ""
    dscTipoPubl: str = "artigo"
    autrs: list[Autor] = []
    artg: Optional[ArtigoSub] = None
    tese: Optional[TeseSub] = None
    livr: Optional[LivroSub] = None


class NovoSoftware(BaseModel):
    codArea: str
    nomSoft: str
    dscSoft: str = ""
    nomRespSoft: str = ""
    dscEquipSoft: str = ""
    dscUrlSoft: str = ""
    arqvs: list[dict] = []
