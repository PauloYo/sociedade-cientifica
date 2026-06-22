import reflex as rx

from ..components.layout import page_wrapper
from ..state.app_state import AppState
from ..styles import PAGE_HEADING


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
                AppState.loading_areas,
                rx.text("Carregando...", color_scheme="gray", size="3"),
                rx.text("Nenhuma área cadastrada.", color_scheme="gray", size="3"),
            ),
        ],
    )
