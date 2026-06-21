import reflex as rx

from ..styles import SIDEBAR_WIDTH
from .sidebar import sidebar
from .breadcrumbs import breadcrumbs as breadcrumbs_comp
from .footer import footer as footer_comp


BREADCRUMBS_MAP: dict[str, list[tuple[str, str | None]]] = {
    "dashboard": [("Dashboard", None)],
    "areas": [("Áreas", None)],
    "pesquisas": [("Pesquisas", None)],
    "publicacoes": [("Publicações", None)],
    "softwares": [("Softwares & Tutoriais", None)],
}


def page_wrapper(
    *children: rx.Component,
    breadcrumbs_key: str | None = None,
    breadcrumbs_items: list[tuple[str, str | None]] | None = None,
) -> rx.Component:
    crumbs = breadcrumbs_items
    if crumbs is None and breadcrumbs_key is not None:
        crumbs = BREADCRUMBS_MAP.get(breadcrumbs_key, [("Página", None)])

    return rx.hstack(
        sidebar(),
        rx.vstack(
            rx.container(
                rx.vstack(
                    breadcrumbs_comp(crumbs) if crumbs else rx.fragment(),
                    *children,
                    spacing="4",
                    width="100%",
                ),
                padding="1.5rem 2rem",
                max_width="1200px",
            ),
            footer_comp(),
            width=f"calc(100% - {SIDEBAR_WIDTH})",
            margin_left=SIDEBAR_WIDTH,
            min_height="100vh",
            spacing="0",
        ),
        spacing="0",
    )
