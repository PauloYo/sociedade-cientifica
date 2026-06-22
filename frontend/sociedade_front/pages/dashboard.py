import reflex as rx

from ..components.layout import page_wrapper
from ..components.stat_card import stat_card
from ..state.app_state import AppState
from ..styles import PAGE_HEADING


def dashboard_page() -> rx.Component:
    return page_wrapper(
        breadcrumbs_key="dashboard",
        children=[
            rx.heading("Visão Geral", **PAGE_HEADING),
            rx.cond(
                AppState.loading,
                rx.text("Carregando...", color_scheme="gray", size="3"),
                rx.grid(
                    stat_card("Áreas", AppState.areas_count, "📂"),
                    stat_card("Pesquisas", AppState.pesquisas_count, "🔬"),
                    stat_card("Publicações", AppState.publicacoes_count, "📄"),
                    stat_card("Softwares", AppState.softwares_count, "💻"),
                    columns="4",
                    spacing="4",
                    width="100%",
                ),
            ),
            rx.cond(
                AppState.recent_pesquisas,
                rx.card(
                    rx.vstack(
                        rx.heading("Últimas Pesquisas", size="5"),
                        rx.foreach(
                            AppState.recent_pesquisas,
                            lambda p: rx.text(p.get("nomPesq", ""), size="2"),
                        ),
                        spacing="3",
                        padding="1.5rem",
                        align="start",
                        width="100%",
                    ),
                    margin_top="2rem",
                    width="100%",
                ),
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
