import reflex as rx

from ..components.layout import page_wrapper
from ..utils.api import get, post
from ..styles import PAGE_HEADING


class NovoSoftwareState(rx.State):
    codArea: str = ""
    nomSoft: str = ""
    dscSoft: str = ""
    nomRespSoft: str = ""
    dscEquipSoft: str = ""
    dscUrlSoft: str = ""
    areas: list[dict] = []
    success: bool = False
    error: str = ""

    @rx.var
    def area_names(self) -> list[str]:
        return [a.get("nomArea", "") for a in self.areas]

    async def load_areas(self):
        try:
            resp = await get("/areas")
            self.areas = resp.get("response", [])
        except Exception as e:
            self.error = f"Erro ao carregar áreas: {e}"

    def change_area(self, v: str):
        for a in self.areas:
            if a.get("nomArea") == v:
                self.codArea = a.get("codArea", "")
                break

    def change_nomSoft(self, v: str):
        self.nomSoft = v

    def change_dscSoft(self, v: str):
        self.dscSoft = v

    def change_nomRespSoft(self, v: str):
        self.nomRespSoft = v

    def change_dscEquipSoft(self, v: str):
        self.dscEquipSoft = v

    def change_dscUrlSoft(self, v: str):
        self.dscUrlSoft = v

    async def submit(self):
        self.success = False
        self.error = ""
        yield
        try:
            resp = await post("/softwares-tutoriais", {
                "codArea": self.codArea,
                "nomSoft": self.nomSoft,
                "dscSoft": self.dscSoft,
                "nomRespSoft": self.nomRespSoft,
                "dscEquipSoft": self.dscEquipSoft,
                "dscUrlSoft": self.dscUrlSoft,
                "arqvs": [],
            })
            if resp.get("status") == "ok":
                self.success = True
                self._reset()
            else:
                self.error = "Erro ao criar software"
        except Exception as e:
            self.error = str(e)
        yield

    def _reset(self):
        self.codArea = ""
        self.nomSoft = ""
        self.dscSoft = ""
        self.nomRespSoft = ""
        self.dscEquipSoft = ""
        self.dscUrlSoft = ""


def _field(label: str, handler, placeholder: str = "", **kwargs) -> rx.Component:
    return rx.vstack(
        rx.text(label, weight="bold", size="2"),
        rx.input(placeholder=placeholder, on_change=handler, **kwargs),
        width="100%",
        spacing="1",
    )


def novo_software_page() -> rx.Component:
    s = NovoSoftwareState
    return page_wrapper(
        breadcrumbs_items=[("Softwares", "/softwares"), ("Novo Software", None)],
        children=[
            rx.heading("Novo Software / Tutorial", **PAGE_HEADING),
            rx.cond(s.success,
                    rx.callout("Software cadastrado com sucesso!", icon="check",
                               color_scheme="green", width="100%")),
            rx.cond(s.error,
                    rx.callout(s.error, icon="alert_circle",
                               color_scheme="red", width="100%")),
            rx.vstack(
                rx.text("Área", weight="bold", size="2"),
                rx.select(s.area_names, on_change=s.change_area,
                          placeholder="Selecione a área", width="100%"),
                _field("Nome do Software", s.change_nomSoft),
                _field("Descrição", s.change_dscSoft),
                _field("Responsável", s.change_nomRespSoft),
                _field("Equipamento", s.change_dscEquipSoft),
                _field("URL", s.change_dscUrlSoft, placeholder="https://..."),
                rx.hstack(
                    rx.button("Salvar", color_scheme="blue", on_click=s.submit),
                    rx.link(rx.button("Cancelar", variant="soft", color_scheme="gray"),
                            href="/softwares"),
                    spacing="4", margin_top="1rem",
                ),
                spacing="4", width="100%",
            ),
        ],
    )
