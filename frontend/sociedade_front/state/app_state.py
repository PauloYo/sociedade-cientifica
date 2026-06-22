import reflex as rx

from ..utils.api import get


class AppState(rx.State):
    areas_count: int = 0
    pesquisas_count: int = 0
    publicacoes_count: int = 0
    softwares_count: int = 0
    recent_pesquisas: list[dict] = []
    loading: bool = False
    loading_areas: bool = False
    loading_pesquisas: bool = False
    loading_publicacoes: bool = False
    loading_softwares: bool = False

    async def load_dashboard(self):
        self.loading = True
        yield

        try:
            areas = await get("/areas")
            self.areas_count = len(areas.get("response", []))

            pesquisas = await get("/pesquisas")
            all_pesquisas = []
            for doc in pesquisas.get("response", []):
                all_pesquisas.extend(doc.get("pesquisa", []))
            self.pesquisas_count = len(all_pesquisas)
            self.recent_pesquisas = all_pesquisas[:5]

            documentos = await get("/documentos")
            total_publ = sum(
                len(doc.get("publicacao", []))
                for doc in documentos.get("response", [])
            )
            self.publicacoes_count = total_publ

            softwares = await get("/softwares-tutoriais")
            total_soft = sum(
                len(doc.get("software", []))
                for doc in softwares.get("response", [])
            )
            self.softwares_count = total_soft
        except Exception as e:
            print(f"Erro ao carregar dashboard: {e}")

        self.loading = False
        yield

    async def load_areas(self):
        self.loading_areas = True
        yield
        try:
            await get("/areas")
        except Exception as e:
            print(f"Erro ao carregar áreas: {e}")
        self.loading_areas = False
        yield

    async def load_pesquisas(self):
        self.loading_pesquisas = True
        yield
        try:
            await get("/pesquisas")
        except Exception as e:
            print(f"Erro ao carregar pesquisas: {e}")
        self.loading_pesquisas = False
        yield

    async def load_publicacoes(self):
        self.loading_publicacoes = True
        yield
        try:
            await get("/documentos")
        except Exception as e:
            print(f"Erro ao carregar publicações: {e}")
        self.loading_publicacoes = False
        yield

    async def load_softwares(self):
        self.loading_softwares = True
        yield
        try:
            await get("/softwares-tutoriais")
        except Exception as e:
            print(f"Erro ao carregar softwares: {e}")
        self.loading_softwares = False
        yield
