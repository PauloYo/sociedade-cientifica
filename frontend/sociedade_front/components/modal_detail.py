import reflex as rx


def pesquisa_modal(pesquisa: dict, show: rx.Var[bool], on_close) -> rx.Component:
    crdn = pesquisa.get("crdn", {}) if isinstance(pesquisa.get("crdn"), dict) else {}
    endr = crdn.get("endr", {}) if isinstance(crdn.get("endr"), dict) else {}

    return rx.cond(
        show,
        rx.box(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.heading(pesquisa.get("nomPesq", "Detalhes"), size="5"),
                        rx.spacer(),
                        rx.button("✕", on_click=on_close, variant="ghost", size="1"),
                        width="100%",
                    ),
                    rx.text(pesquisa.get("dscPesq", ""), size="2", color_scheme="gray"),
                    rx.divider(),
                    rx.hstack(rx.text("Coordenador", weight="bold", size="3"),
                              rx.text(crdn.get("nomCrdn", "-"), size="3"), width="100%"),
                    rx.hstack(rx.text("E-mail", weight="bold", size="3"),
                              rx.text(crdn.get("dscEmailCrdn", "-"), size="3"), width="100%"),
                    rx.hstack(rx.text("Instituição", weight="bold", size="3"),
                              rx.text(crdn.get("nomInstCrdn", "-"), size="3"), width="100%"),
                    rx.hstack(rx.text("Início", weight="bold", size="3"),
                              rx.text(pesquisa.get("datInicPesq", "-"), size="3"), width="100%"),
                    rx.hstack(rx.text("Término Previsto", weight="bold", size="3"),
                              rx.text(pesquisa.get("datFimPrevPesq", "-"), size="3"), width="100%"),
                    rx.cond(
                        endr.get("dscLogradEndr"),
                        rx.box(
                            rx.text("Endereço (embutido)", weight="bold", size="3"),
                            rx.text(
                                f"{endr.get('dscLogradEndr', '')}, {endr.get('numLogradEndr', '')} - "
                                f"{endr.get('nomBairroEndr', '')}, "
                                f"{endr.get('nomCidEndr', '')}/{endr.get('sglUfEndr', '')}",
                                size="2", color_scheme="gray",
                            ),
                            width="100%",
                        ),
                    ),
                    rx.button("Fechar", on_click=on_close, color_scheme="gray",
                              margin_top="1rem"),
                    spacing="3",
                    align="start",
                    width="100%",
                ),
                padding="2rem",
                background="white",
                border_radius="12px",
                box_shadow="0 8px 32px rgba(0,0,0,0.2)",
                max_width="600px",
                width="100%",
            ),
            position="fixed",
            top="0", left="0", right="0", bottom="0",
            background="rgba(0,0,0,0.4)",
            display="flex",
            align_items="center",
            justify_content="center",
            z_index="100",
        ),
    )
