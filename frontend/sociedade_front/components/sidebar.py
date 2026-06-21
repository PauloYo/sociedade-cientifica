import reflex as rx

from ..styles import SIDEBAR_WIDTH, SIDEBAR_BG, ALURA_BLUE, ALURA_DARK

NAV_ITEMS = [
    ("Dashboard", "/", "◆"),
    ("Áreas", "/areas", "📂"),
    ("Pesquisas", "/pesquisas", "🔬"),
    ("Publicações", "/publicacoes", "📄"),
    ("Softwares", "/softwares", "💻"),
]


def sidebar() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text("SC", font_size="1.5rem", font_weight="bold", color=SIDEBAR_BG,
                     background="white", padding="0.4rem 0.8rem", border_radius="8px"),
            padding="1.5rem 1rem 2rem",
            width="100%",
        ),
        rx.vstack(
            *[
                rx.link(
                    rx.hstack(
                        rx.text(icon, font_size="1.2rem"),
                        rx.text(label, font_size="0.95rem"),
                        spacing="3",
                        align="center",
                    ),
                    href=href,
                    color="white",
                    padding="0.6rem 1rem",
                    border_radius="8px",
                    width="100%",
                    _hover={"background": ALURA_BLUE, "text_decoration": "none"},
                    _active_link={"background": ALURA_BLUE, "text_decoration": "none"},
                    underline="none",
                )
                for label, href, icon in NAV_ITEMS
            ],
            spacing="2",
            width="100%",
            padding_x="0.5rem",
        ),
        rx.spacer(),
        rx.hstack(
            rx.color_mode.button(),
            rx.text("Sistema v1.0", font_size="0.7rem", color="white", opacity="0.6"),
            spacing="3",
            align="center",
            justify="center",
            width="100%",
        ),
        padding_y="1rem",
        width=SIDEBAR_WIDTH,
        height="100vh",
        background=SIDEBAR_BG,
        position="fixed",
        left="0",
        top="0",
        z_index="20",
    )
