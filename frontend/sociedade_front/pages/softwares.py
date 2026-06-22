import reflex as rx

from ..components.layout import page_wrapper
from ..state.app_state import AppState
from ..styles import PAGE_HEADING


def softwares_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="softwares",
        children=[
            rx.hstack(
                rx.heading("Softwares & Tutoriais", **PAGE_HEADING),
                rx.spacer(),
                rx.button("+ Novo Software", color_scheme="blue"),
                width="100%",
            ),
            rx.cond(
                AppState.loading_softwares,
                rx.text("Carregando...", color_scheme="gray", size="3"),
                rx.text("Nenhum software cadastrado.", color_scheme="gray", size="3"),
            ),
        ],
    )
