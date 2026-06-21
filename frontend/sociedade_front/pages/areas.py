import reflex as rx

from ..components.layout import page_wrapper
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
            rx.text("Carregando áreas...", color_scheme="gray", size="3"),
        ],
    )
