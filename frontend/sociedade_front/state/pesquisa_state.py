import reflex as rx

from ..utils.api import get


class PesquisaState(rx.State):
    pesquisas: list[dict] = []
    filtered_pesquisas: list[dict] = []
    areas: list[dict] = []
    filter_area: str = ""
    loading: bool = False

    @rx.var
    def area_names(self) -> list[str]:
        return [a.get("nomArea", "") for a in self.areas]

    async def load_pesquisas(self):
        self.loading = True
        yield
        try:
            resp = await get("/pesquisas")
            raw = resp.get("response", [])
            all_pesquisas = []
            for doc in raw:
                for p in doc.get("pesquisa", []):
                    p["_area_nome"] = doc.get("nomArea", "")
                    p["_area_cod"] = doc.get("codArea", "")
                    all_pesquisas.append(p)
            self.pesquisas = all_pesquisas
            self.filtered_pesquisas = all_pesquisas

            area_resp = await get("/areas")
            self.areas = area_resp.get("response", [])
        except Exception as e:
            print(f"Erro ao carregar pesquisas: {e}")
            self.pesquisas = []
            self.filtered_pesquisas = []
        self.loading = False
        yield

    def filter_by_area(self, area_nome: str):
        self.filter_area = area_nome
        if not area_nome:
            self.filtered_pesquisas = self.pesquisas
        else:
            self.filtered_pesquisas = [
                p for p in self.pesquisas
                if p.get("_area_nome") == area_nome
            ]
