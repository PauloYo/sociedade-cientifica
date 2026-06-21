import reflex as rx

from ..components.layout import page_wrapper
from ..styles import PAGE_HEADING


def pesquisas_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="pesquisas",
        children=[
            rx.hstack(
                rx.heading("Pesquisas", **PAGE_HEADING),
                rx.spacer(),
                rx.button("+ Nova Pesquisa", color_scheme="blue"),
                width="100%",
            ),
            rx.text("Carregando pesquisas...", color_scheme="gray", size="3"),
        ],
    )
