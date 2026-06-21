import reflex as rx


def footer() -> rx.Component:
    return rx.box(
        rx.text(
            "© Sociedade Científica — Sistema de Cadastro de Pesquisas",
            size="1",
            color_scheme="gray",
        ),
        padding="1.5rem 0",
        margin_top="3rem",
        border_top="1px solid",
        border_color=rx.color("gray", 5),
        width="100%",
    )
