from pydantic import BaseModel


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


class NovaPublicacao(BaseModel):
    codArea: str = ""
    nomTitPubl: str = ""
    numAnoPubl: str = ""
    dscTipoPubl: str = "artigo"
    autrs: list[dict] = []
    artg: dict = {}
    tese: dict = {}
    livr: dict = {}


class NovoSoftware(BaseModel):
    codArea: str = ""
    nomSoft: str = ""
    dscSoft: str = ""
    nomRespSoft: str = ""
    dscEquipSoft: str = ""
    dscUrlSoft: str = ""
    arqvs: list[dict] = []
