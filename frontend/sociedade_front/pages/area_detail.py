import reflex as rx

from ..components.layout import page_wrapper
from ..utils.api import get
from ..styles import PAGE_HEADING


class AreaDetailState(rx.State):
    area: dict | None = None
    loading: bool = False

    @rx.var
    def pesquisas(self) -> list[dict]:
        return (self.area or {}).get("pesquisa", [])

    @rx.var
    def publicacoes(self) -> list[dict]:
        return (self.area or {}).get("publicacao", [])

    @rx.var
    def softwares(self) -> list[dict]:
        return (self.area or {}).get("software", [])

    async def load_area(self):
        aid = self.router.page.params.get("area_id", "")
        if not aid:
            return
        self.loading = True
        yield
        try:
            resp = await get(f"/area/{aid}")
            self.area = resp.get("response")
        except Exception as e:
            print(f"Erro: {e}")
            self.area = None
        self.loading = False
        yield


def _pesquisa_row(p: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(p.get("nomPesq", "")),
        rx.table.cell(p.get("crdn", {}).get("nomCrdn", "") if isinstance(p.get("crdn"), dict) else ""),
        rx.table.cell(p.get("datInicPesq", "")),
        rx.table.cell(p.get("datFimPrevPesq", "")),
    )


def area_detail_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="areas",
        children=[
            rx.cond(
                AreaDetailState.loading,
                rx.text("Carregando...", color_scheme="gray", size="3"),
                rx.cond(
                    AreaDetailState.area,
                    rx.vstack(
                        rx.heading(AreaDetailState.area.get("nomArea", ""), **PAGE_HEADING),
                        rx.text("Documento completo da área com dados embutidos.",
                                size="2", color_scheme="gray"),
                        rx.divider(),
                        rx.heading("Pesquisas", size="5"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("Nome"),
                                    rx.table.column_header_cell("Coordenador"),
                                    rx.table.column_header_cell("Início"),
                                    rx.table.column_header_cell("Fim Previsto"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(AreaDetailState.pesquisas, _pesquisa_row),
                            ),
                            variant="surface", width="100%",
                        ),
                        rx.heading("Publicações", size="5", margin_top="2rem"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("Título"),
                                    rx.table.column_header_cell("Ano"),
                                    rx.table.column_header_cell("Tipo"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    AreaDetailState.publicacoes,
                                    lambda pub: rx.table.row(
                                        rx.table.cell(pub.get("nomTitPubl", "")),
                                        rx.table.cell(pub.get("numAnoPubl", "")),
                                        rx.table.cell(pub.get("dscTipoPubl", "")),
                                    ),
                                ),
                            ),
                            variant="surface", width="100%",
                        ),
                        rx.heading("Softwares", size="5", margin_top="2rem"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("Nome"),
                                    rx.table.column_header_cell("Responsável"),
                                    rx.table.column_header_cell("Equipamento"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    AreaDetailState.softwares,
                                    lambda s: rx.table.row(
                                        rx.table.cell(s.get("nomSoft", "")),
                                        rx.table.cell(s.get("nomRespSoft", "")),
                                        rx.table.cell(s.get("dscEquipSoft", "")),
                                    ),
                                ),
                            ),
                            variant="surface", width="100%",
                        ),
                        spacing="4", width="100%",
                    ),
                    rx.text("Área não encontrada.", color_scheme="gray", size="3"),
                ),
            ),
        ],
    )
