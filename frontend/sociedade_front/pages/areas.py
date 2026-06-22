import reflex as rx

from ..components.layout import page_wrapper
from ..state.area_state import AreaState
from ..styles import PAGE_HEADING


def _area_card(area: dict) -> rx.Component:
    return rx.link(
        rx.card(
            rx.vstack(
                rx.text("📂", font_size="2rem"),
                rx.heading(area.get("nomArea", ""), size="4", weight="bold"),
                rx.text(f"Área de interesse", size="2", color_scheme="gray"),
                align="center",
                spacing="2",
                padding="1.5rem",
                width="100%",
            ),
            width="100%",
            _hover={"box_shadow": "0 4px 12px rgba(0,0,0,0.1)",
                    "transform": "translateY(-2px)",
                    "transition": "all 0.2s ease"},
        ),
        href=f"/areas/{area.get('codArea', '')}",
        underline="none",
        width="100%",
    )


def areas_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="areas",
        children=[
            rx.hstack(
                rx.heading("Áreas de Interesse", **PAGE_HEADING),
                rx.spacer(),
                rx.button("+ Nova Área", color_scheme="blue"),
                width="100%",
            ),
            rx.cond(
                AreaState.loading,
                rx.text("Carregando...", color_scheme="gray", size="3"),
                rx.cond(
                    AreaState.areas,
                    rx.grid(
                        rx.foreach(AreaState.areas, _area_card),
                        columns="3",
                        spacing="4",
                        width="100%",
                    ),
                    rx.text("Nenhuma área cadastrada.", color_scheme="gray", size="3"),
                ),
            ),
        ],
    )
