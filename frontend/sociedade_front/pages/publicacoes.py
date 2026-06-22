import reflex as rx

from ..components.layout import page_wrapper
from ..state.app_state import AppState
from ..styles import PAGE_HEADING


def publicacoes_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="publicacoes",
        children=[
            rx.hstack(
                rx.heading("Publicações", **PAGE_HEADING),
                rx.spacer(),
                rx.button("+ Nova Publicação", color_scheme="blue"),
                width="100%",
            ),
            rx.cond(
                AppState.loading_publicacoes,
                rx.text("Carregando...", color_scheme="gray", size="3"),
                rx.text("Nenhuma publicação cadastrada.", color_scheme="gray", size="3"),
            ),
        ],
    )
