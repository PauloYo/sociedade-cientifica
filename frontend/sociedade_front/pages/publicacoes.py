import reflex as rx

from ..components.layout import page_wrapper
from ..state.publicacao_state import PublicacaoState
from ..styles import PAGE_HEADING


def _artigo_linha(pub: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(pub.get("nomTitPubl", "")),
        rx.table.cell(pub.get("numAnoPubl", "")),
        rx.table.cell(pub.get("_periodico", "")),
        rx.table.cell(pub.get("_volume", "")),
        rx.table.cell(pub.get("_edicao", "")),
        rx.table.cell(pub.get("_autores_str", "")),
    )


def _tese_linha(pub: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(pub.get("nomTitPubl", "")),
        rx.table.cell(pub.get("numAnoPubl", "")),
        rx.table.cell(pub.get("_grau", "")),
        rx.table.cell(pub.get("_instituicao", "")),
        rx.table.cell(pub.get("_autores_str", "")),
    )


def _livro_linha(pub: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(pub.get("nomTitPubl", "")),
        rx.table.cell(pub.get("numAnoPubl", "")),
        rx.table.cell(pub.get("_editora", "")),
        rx.table.cell(pub.get("_area_nome", "")),
        rx.table.cell(pub.get("_autores_str", "")),
    )


def _todas_linha(pub: dict) -> rx.Component:
    return rx.table.row(
        rx.table.cell(pub.get("nomTitPubl", "")),
        rx.table.cell(pub.get("numAnoPubl", "")),
        rx.table.cell(pub.get("dscTipoPubl", "")),
        rx.table.cell(pub.get("_area_nome", "")),
        rx.table.cell(pub.get("_autores_str", "")),
    )


def publicacoes_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="publicacoes",
        children=[
            rx.hstack(
                rx.heading("Publicações", **PAGE_HEADING),
                rx.spacer(),
                rx.select(
                    PublicacaoState.area_names,
                    placeholder="Filtrar por área",
                    value=PublicacaoState.filter_area,
                    on_change=PublicacaoState.filter_by_area,
                    width="200px",
                ),
                rx.link(rx.button("+ Nova Publicação", color_scheme="blue"), href="/publicacoes/nova"),
                width="100%",
                wrap="wrap",
                spacing="3",
            ),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Todas", value="todas"),
                    rx.tabs.trigger("Artigos", value="artigo"),
                    rx.tabs.trigger("Teses", value="tese"),
                    rx.tabs.trigger("Livros", value="livro"),
                ),
                rx.tabs.content(
                    rx.cond(
                        PublicacaoState.loading,
                        rx.text("Carregando...", color_scheme="gray", size="3"),
                        rx.cond(
                            PublicacaoState.filtered_publicacoes,
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell("Título"),
                                        rx.table.column_header_cell("Ano"),
                                        rx.table.column_header_cell("Tipo"),
                                        rx.table.column_header_cell("Área"),
                                        rx.table.column_header_cell("Autores"),
                                    ),
                                ),
                                rx.table.body(
                                    rx.foreach(PublicacaoState.filtered_publicacoes, _todas_linha),
                                ),
                                variant="surface", width="100%",
                            ),
                            rx.text("Nenhuma publicação encontrada.", color_scheme="gray", size="3"),
                        ),
                    ),
                    value="todas",
                ),
                rx.tabs.content(
                    rx.cond(
                        PublicacaoState.loading,
                        rx.text("Carregando...", color_scheme="gray", size="3"),
                        rx.cond(
                            PublicacaoState.filtered_publicacoes,
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell("Título"),
                                        rx.table.column_header_cell("Ano"),
                                        rx.table.column_header_cell("Periódico"),
                                        rx.table.column_header_cell("Volume"),
                                        rx.table.column_header_cell("Edição"),
                                        rx.table.column_header_cell("Autores"),
                                    ),
                                ),
                                rx.table.body(
                                    rx.foreach(PublicacaoState.filtered_publicacoes, _artigo_linha),
                                ),
                                variant="surface", width="100%",
                            ),
                            rx.text("Nenhum artigo encontrado.", color_scheme="gray", size="3"),
                        ),
                    ),
                    value="artigo",
                ),
                rx.tabs.content(
                    rx.cond(
                        PublicacaoState.loading,
                        rx.text("Carregando...", color_scheme="gray", size="3"),
                        rx.cond(
                            PublicacaoState.filtered_publicacoes,
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell("Título"),
                                        rx.table.column_header_cell("Ano"),
                                        rx.table.column_header_cell("Grau"),
                                        rx.table.column_header_cell("Instituição"),
                                        rx.table.column_header_cell("Autores"),
                                    ),
                                ),
                                rx.table.body(
                                    rx.foreach(PublicacaoState.filtered_publicacoes, _tese_linha),
                                ),
                                variant="surface", width="100%",
                            ),
                            rx.text("Nenhuma tese encontrada.", color_scheme="gray", size="3"),
                        ),
                    ),
                    value="tese",
                ),
                rx.tabs.content(
                    rx.cond(
                        PublicacaoState.loading,
                        rx.text("Carregando...", color_scheme="gray", size="3"),
                        rx.cond(
                            PublicacaoState.filtered_publicacoes,
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell("Título"),
                                        rx.table.column_header_cell("Ano"),
                                        rx.table.column_header_cell("Editora"),
                                        rx.table.column_header_cell("Área"),
                                        rx.table.column_header_cell("Autores"),
                                    ),
                                ),
                                rx.table.body(
                                    rx.foreach(PublicacaoState.filtered_publicacoes, _livro_linha),
                                ),
                                variant="surface", width="100%",
                            ),
                            rx.text("Nenhum livro encontrado.", color_scheme="gray", size="3"),
                        ),
                    ),
                    value="livro",
                ),
                default_value="todas",
                on_change=PublicacaoState.set_tab,
                value=PublicacaoState.active_tab,
                width="100%",
            ),
        ],
    )
