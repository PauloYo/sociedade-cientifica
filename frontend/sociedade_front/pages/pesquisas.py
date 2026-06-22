import reflex as rx

from ..components.layout import page_wrapper
from ..components.modal_detail import pesquisa_modal
from ..state.pesquisa_state import PesquisaState
from ..styles import PAGE_HEADING


class PagePesquisaState(rx.State):
    show_modal: bool = False
    selected: dict = {}

    def open_detail(self, idx: int):
        items = PesquisaState.filtered_pesquisas
        if 0 <= idx < len(items):
            self.selected = items[idx]
            self.show_modal = True

    def close_detail(self):
        self.show_modal = False
        self.selected = {}


def _linha(p: dict, idx: int) -> rx.Component:
    return rx.table.row(
        rx.table.cell(p.get("nomPesq", "")),
        rx.table.cell(p.get("_area_nome", "")),
        rx.table.cell(
            p.get("crdn", {}).get("nomCrdn", "") if isinstance(p.get("crdn"), dict) else "",
        ),
        rx.table.cell(p.get("datInicPesq", "")),
        rx.table.cell(
            rx.button("Ver", size="1", color_scheme="blue", variant="soft",
                      on_click=PagePesquisaState.open_detail(idx)),
        ),
    )


def pesquisas_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="pesquisas",
        children=[
            rx.hstack(
                rx.heading("Pesquisas", **PAGE_HEADING),
                rx.spacer(),
                    rx.select(
                        PesquisaState.area_names,
                        placeholder="Filtrar por área",
                    value=PesquisaState.filter_area,
                    on_change=PesquisaState.filter_by_area,
                    width="200px",
                ),
                rx.button("+ Nova Pesquisa", color_scheme="blue"),
                width="100%",
                wrap="wrap",
                spacing="3",
            ),
            rx.cond(
                PesquisaState.loading,
                rx.text("Carregando...", color_scheme="gray", size="3"),
                rx.cond(
                    PesquisaState.filtered_pesquisas,
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Nome"),
                                rx.table.column_header_cell("Área"),
                                rx.table.column_header_cell("Coordenador"),
                                rx.table.column_header_cell("Início"),
                                rx.table.column_header_cell(""),
                            ),
                        ),
                        rx.table.body(
                            rx.foreach(
                                PesquisaState.filtered_pesquisas,
                                lambda p, i: _linha(p, i),
                            ),
                        ),
                        variant="surface", width="100%",
                    ),
                    rx.text("Nenhuma pesquisa encontrada.", color_scheme="gray", size="3"),
                ),
            ),
            pesquisa_modal(PagePesquisaState.selected, PagePesquisaState.show_modal,
                          PagePesquisaState.close_detail),
        ],
    )
