import reflex as rx

from ..utils.api import get


class PublicacaoState(rx.State):
    publicacoes: list[dict] = []
    filtered_publicacoes: list[dict] = []
    active_tab: str = "todas"
    areas: list[dict] = []
    filter_area: str = ""
    loading: bool = False

    @rx.var
    def area_names(self) -> list[str]:
        return [a.get("nomArea", "") for a in self.areas]

    async def load_publicacoes(self):
        self.loading = True
        yield
        try:
            resp = await get("/documentos")
            raw = resp.get("response", [])
            all_publ = []
            for doc in raw:
                area_nome = doc.get("nomArea", "")
                for pub in doc.get("publicacao", []):
                    pub["_area_nome"] = area_nome
                    all_publ.append(pub)
            self.publicacoes = all_publ
            self._apply_filters()

            area_resp = await get("/areas")
            self.areas = area_resp.get("response", [])
        except Exception as e:
            print(f"Erro ao carregar publicações: {e}")
            self.publicacoes = []
            self.filtered_publicacoes = []
        self.loading = False
        yield

    def set_tab(self, tab: str):
        self.active_tab = tab
        self._apply_filters()

    def filter_by_area(self, area_nome: str):
        self.filter_area = area_nome
        self._apply_filters()

    def _apply_filters(self):
        items = self.publicacoes
        if self.filter_area:
            items = [p for p in items if p.get("_area_nome") == self.filter_area]
        if self.active_tab != "todas":
            items = [p for p in items if p.get("dscTipoPubl") == self.active_tab]
        for p in items:
            autrs = p.get("autrs", [])
            p["_autores_str"] = ", ".join(
                a.get("nomAutr", "") for a in (autrs if isinstance(autrs, list) else [])
            )
            artg = p.get("artg", {}) or {}
            p["_periodico"] = artg.get("nomPeriodArtg", "")
            p["_volume"] = artg.get("numVolumeArtg", "")
            p["_edicao"] = artg.get("numEdicArtg", "")
            tese = p.get("tese", {}) or {}
            p["_grau"] = tese.get("dscGrauTese", "")
            p["_instituicao"] = tese.get("nomInstTese", "")
            livr = p.get("livr", {}) or {}
            edtr = livr.get("edtr", {}) or {}
            p["_editora"] = edtr.get("nomEdtr", "")
        self.filtered_publicacoes = items
