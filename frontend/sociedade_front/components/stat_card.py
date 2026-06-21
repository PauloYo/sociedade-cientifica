import reflex as rx


def stat_card(title: str, value: str, icon: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(icon, font_size="2rem"),
            rx.heading(value, size="7", weight="bold"),
            rx.text(title, size="2", color_scheme="gray"),
            align="center",
            spacing="2",
            padding="1.5rem",
        ),
        width="100%",
        _hover={"box_shadow": "0 4px 12px rgba(0,0,0,0.1)",
                "transform": "translateY(-2px)",
                "transition": "all 0.2s ease"},
    )
