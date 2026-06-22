import reflex as rx

from ..utils.api import get


class AreaState(rx.State):
    areas: list[dict] = []
    selected_area: dict | None = None
    loading: bool = False

    async def load_areas(self):
        self.loading = True
        yield
        try:
            resp = await get("/areas")
            self.areas = resp.get("response", [])
        except Exception as e:
            print(f"Erro ao carregar áreas: {e}")
            self.areas = []
        self.loading = False
        yield

    async def load_area_detail(self, area_id: str):
        self.loading = True
        yield
        try:
            resp = await get(f"/area/{area_id}")
            self.selected_area = resp.get("response")
        except Exception as e:
            print(f"Erro ao carregar área {area_id}: {e}")
            self.selected_area = None
        self.loading = False
        yield
