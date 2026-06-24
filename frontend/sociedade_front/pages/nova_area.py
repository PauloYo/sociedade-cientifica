import reflex as rx

from ..components.layout import page_wrapper
from ..utils.api import post
from ..styles import PAGE_HEADING


class NovaAreaState(rx.State):
    nomArea: str = ""
    success: bool = False
    error: str = ""

    def change_nomArea(self, v: str):
        self.nomArea = v

    async def submit(self):
        self.success = False
        self.error = ""
        yield
        try:
            resp = await post("/area", {"nomArea": self.nomArea})
            if resp.get("status") == "ok":
                self.success = True
                self.nomArea = ""
            else:
                self.error = "Erro ao criar área"
        except Exception as e:
            self.error = str(e)
        yield


def nova_area_page() -> rx.Component:
    s = NovaAreaState
    return page_wrapper(
        breadcrumbs_items=[("Áreas", "/areas"), ("Nova Área", None)],
        children=[
            rx.heading("Nova Área", **PAGE_HEADING),
            rx.cond(s.success,
                    rx.callout("Área cadastrada com sucesso!", icon="check",
                               color_scheme="green", width="100%")),
            rx.cond(s.error,
                    rx.callout(s.error, color_scheme="red", width="100%")),
            rx.vstack(
                rx.text("Nome da Área", weight="bold", size="2"),
                rx.input(placeholder="Ex: Ciência da Computação",
                         on_change=s.change_nomArea, value=s.nomArea),
                rx.hstack(
                    rx.button("Salvar", color_scheme="blue", on_click=s.submit),
                    rx.link(rx.button("Cancelar", variant="soft", color_scheme="gray"),
                            href="/areas"),
                    spacing="4", margin_top="1rem",
                ),
                spacing="4", width="100%",
            ),
        ],
    )
