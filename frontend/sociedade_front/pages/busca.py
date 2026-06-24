import reflex as rx

from ..components.layout import page_wrapper
from ..state.search_state import SearchState
from ..styles import PAGE_HEADING


def _result_row(item: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(rx.badge(item.get("tipo", ""), variant="soft", size="1")),
        rx.table.cell(item.get("titulo", "")),
        rx.table.cell(item.get("subtitulo", "")),
        rx.table.cell(item.get("area", "")),
        rx.table.cell(
            rx.link("Ver", href=item.get("link", "#"), size="1", color_scheme="blue"),
        ),
    )


def busca_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_items=[("Busca", None)],
        children=[
            rx.hstack(
                rx.heading("Busca Global", **PAGE_HEADING),
                rx.spacer(),
                width="100%",
            ),
            rx.hstack(
                rx.input(
                    placeholder="Buscar pesquisas, publicações, softwares...",
                    value=SearchState.query,
                    on_change=SearchState.set_query,
                    width="100%",
                ),
                rx.button("Buscar", color_scheme="blue",
                          on_click=SearchState.search),
                width="100%",
                spacing="3",
            ),
            rx.cond(
                SearchState.loading,
                rx.text("Buscando...", color_scheme="gray", size="3"),
                rx.cond(
                    SearchState.results,
                    rx.vstack(
                        rx.text("Resultados encontrados",
                                size="2", color_scheme="gray"),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("Tipo"),
                                    rx.table.column_header_cell("Nome"),
                                    rx.table.column_header_cell("Detalhe"),
                                    rx.table.column_header_cell("Área"),
                                    rx.table.column_header_cell(""),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(SearchState.results, _result_row),
                            ),
                            variant="surface", width="100%",
                        ),
                        spacing="4", width="100%", margin_top="1rem",
                    ),
                    rx.cond(
                        SearchState.query,
                        rx.text("Nenhum resultado encontrado.", color_scheme="gray",
                                size="3", margin_top="2rem"),
                    ),
                ),
            ),
        ],
    )
