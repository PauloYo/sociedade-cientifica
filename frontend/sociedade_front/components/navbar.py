import reflex as rx


NAV_ITEMS = [
    ("Dashboard", "/"),
    ("Áreas", "/areas"),
    ("Pesquisas", "/pesquisas"),
    ("Publicações", "/publicacoes"),
    ("Softwares", "/softwares"),
]


def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.text("🔬", font_size="1.5rem"),
            rx.text("Sociedade Científica", font_weight="bold", font_size="1.1rem"),
            spacing="3",
        ),
        rx.hstack(
            *[
                rx.link(label, href=href, color_scheme="gray", size="2")
                for label, href in NAV_ITEMS
            ],
            spacing="5",
        ),
        rx.color_mode.button(),
        justify="between",
        align="center",
        padding="0.75rem 2rem",
        border_bottom="1px solid",
        border_color=rx.color("gray", 5),
        background=rx.color("gray", 1),
        position="sticky",
        top="0",
        z_index="10",
    )
