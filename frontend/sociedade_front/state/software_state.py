import reflex as rx

from ..utils.api import get


class SoftwareState(rx.State):
    softwares: list[dict] = []
    filtered_softwares: list[dict] = []
    areas: list[dict] = []
    filter_area: str = ""
    loading: bool = False
    selected: dict | None = None
    show_modal: bool = False

    @rx.var
    def area_names(self) -> list[str]:
        return [a.get("nomArea", "") for a in self.areas]

    async def load_softwares(self):
        self.loading = True
        yield
        try:
            resp = await get("/softwares-tutoriais")
            raw = resp.get("response", [])
            all_soft = []
            for doc in raw:
                area_nome = doc.get("nomArea", "")
                for s in doc.get("software", []):
                    s["_area_nome"] = area_nome
                    s["_arquivos_str"] = ", ".join(
                        a.get("nomArqv", "")
                        for a in (s.get("arqvs", []) if isinstance(s.get("arqvs"), list) else [])
                    )
                    all_soft.append(s)
            self.softwares = all_soft
            self._apply_filters()

            area_resp = await get("/areas")
            self.areas = area_resp.get("response", [])
        except Exception as e:
            print(f"Erro ao carregar softwares: {e}")
            self.softwares = []
            self.filtered_softwares = []
        self.loading = False
        yield

    def filter_by_area(self, area_nome: str):
        self.filter_area = area_nome
        self._apply_filters()

    def open_detail(self, idx: int):
        items = self.filtered_softwares
        if 0 <= idx < len(items):
            item = items[idx]
            cont = item.get("cont", {}) or {}
            endr = cont.get("endr", {}) or {}
            item["_endr_lograd"] = endr.get("dscLogradEndr", "")
            item["_endr_num"] = endr.get("numLogradEndr", "")
            item["_endr_cid"] = endr.get("nomCidEndr", "")
            item["_endr_uf"] = endr.get("sglUfEndr", "")
            self.selected = item
            self.show_modal = True

    def close_detail(self):
        self.show_modal = False
        self.selected = None

    def _apply_filters(self):
        items = self.softwares
        if self.filter_area:
            items = [s for s in items if s.get("_area_nome") == self.filter_area]
        self.filtered_softwares = items
