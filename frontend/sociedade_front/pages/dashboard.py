import reflex as rx

from ..components.layout import page_wrapper
from ..components.stat_card import stat_card
from ..styles import PAGE_HEADING


def dashboard_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="dashboard",
        children=[
            rx.heading("Visão Geral", **PAGE_HEADING),
            rx.grid(
                stat_card("Áreas", "--", "📂"),
                stat_card("Pesquisas", "--", "🔬"),
                stat_card("Publicações", "--", "📄"),
                stat_card("Softwares", "--", "💻"),
                columns="4",
                spacing="4",
                width="100%",
            ),
            rx.card(
                rx.vstack(
                    rx.heading("Sobre", size="5"),
                    rx.text(
                        "Sistema de cadastro de pesquisas, publicações e softwares "
                        "da Sociedade Científica. Os dados são organizados por área "
                        "de interesse em modelo document-based (MongoDB).",
                    ),
                    rx.text(
                        "Use o menu lateral para navegar entre as seções.",
                        color_scheme="gray",
                    ),
                    spacing="3",
                    padding="1.5rem",
                ),
                margin_top="2rem",
            ),
        ],
    )
