import reflex as rx

from ..components.layout import page_wrapper
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
            rx.text("Carregando softwares...", color_scheme="gray", size="3"),
        ],
    )
