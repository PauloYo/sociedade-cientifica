import reflex as rx

from ..components.layout import page_wrapper
from ..state.software_state import SoftwareState
from ..styles import PAGE_HEADING


def _software_card(s: dict, idx: int) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(s.get("nomSoft", ""), size="4"),
            rx.text(s.get("dscSoft", ""), size="2", color_scheme="gray",
                    no_of_lines=3),
            rx.hstack(
                rx.badge(s.get("_area_nome", ""), variant="soft", size="1"),
                rx.spacer(),
                rx.badge(s.get("dscEquipSoft", ""), variant="soft", size="1",
                         color_scheme="green"),
                width="100%",
            ),
            rx.hstack(
                rx.text("Responsável:", weight="bold", size="1"),
                rx.text(s.get("nomRespSoft", "-"), size="1"),
                width="100%",
            ),
            rx.button("Ver detalhes", size="1", variant="soft", color_scheme="blue",
                      on_click=SoftwareState.open_detail(idx)),
            spacing="2",
            align="start",
            width="100%",
            height="100%",
        ),
        width="100%",
        height="100%",
    )


def _software_modal() -> rx.Component:
    s = SoftwareState.selected
    return rx.cond(
        SoftwareState.show_modal,
        rx.box(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.heading(s.get("nomSoft", "Detalhes"), size="5"),
                        rx.spacer(),
                        rx.button("✕", on_click=SoftwareState.close_detail,
                                  variant="ghost", size="1"),
                        width="100%",
                    ),
                    rx.text(s.get("dscSoft", ""), size="2", color_scheme="gray"),
                    rx.divider(),
                    rx.hstack(rx.text("Área", weight="bold", size="3"),
                              rx.text(s.get("_area_nome", "-"), size="3"),
                              width="100%"),
                    rx.hstack(rx.text("Responsável", weight="bold", size="3"),
                              rx.text(s.get("nomRespSoft", "-"), size="3"),
                              width="100%"),
                    rx.hstack(rx.text("Equipamento", weight="bold", size="3"),
                              rx.text(s.get("dscEquipSoft", "-"), size="3"),
                              width="100%"),
                    rx.cond(
                        s.get("_endr_lograd"),
                        rx.box(
                            rx.text("Endereço (embutido)", weight="bold", size="3"),
                            rx.text(
                                f"{s.get('_endr_lograd', '')}, "
                                f"{s.get('_endr_num', '')} - "
                                f"{s.get('_endr_cid', '')}/{s.get('_endr_uf', '')}",
                                size="2", color_scheme="gray",
                            ),
                            width="100%",
                        ),
                    ),
                    rx.divider(),
                    rx.text("Arquivos", weight="bold", size="3"),
                    rx.text(s.get("_arquivos_str", ""), size="1"),
                    rx.cond(
                        s.get("dscUrlSoft"),
                        rx.link("Acessar software", href=s.get("dscUrlSoft", "#"),
                                is_external=True, size="2", color_scheme="blue"),
                    ),
                    rx.button("Fechar", on_click=SoftwareState.close_detail,
                              color_scheme="gray", margin_top="1rem"),
                    spacing="3",
                    align="start",
                    width="100%",
                ),
                padding="2rem",
                background="white",
                border_radius="12px",
                box_shadow="0 8px 32px rgba(0,0,0,0.2)",
                max_width="600px",
                width="100%",
            ),
            position="fixed",
            top="0", left="0", right="0", bottom="0",
            background="rgba(0,0,0,0.4)",
            display="flex",
            align_items="center",
            justify_content="center",
            z_index="100",
        ),
    )


def softwares_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="softwares",
        children=[
            rx.hstack(
                rx.heading("Softwares & Tutoriais", **PAGE_HEADING),
                rx.spacer(),
                rx.select(
                    SoftwareState.area_names,
                    placeholder="Filtrar por área",
                    value=SoftwareState.filter_area,
                    on_change=SoftwareState.filter_by_area,
                    width="200px",
                ),
                rx.link(rx.button("+ Novo Software", color_scheme="blue"), href="/softwares/novo"),
                width="100%",
                wrap="wrap",
                spacing="3",
            ),
            rx.cond(
                SoftwareState.loading,
                rx.text("Carregando...", color_scheme="gray", size="3"),
                rx.cond(
                    SoftwareState.filtered_softwares,
                    rx.grid(
                        rx.foreach(
                            SoftwareState.filtered_softwares,
                            lambda s, i: _software_card(s, i),
                        ),
                        columns="3",
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("Nenhum software cadastrado.", color_scheme="gray", size="3",
                            margin_top="2rem"),
                ),
            ),
            _software_modal(),
        ],
    )
