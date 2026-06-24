import reflex as rx

from ..components.layout import page_wrapper
from ..utils.api import get, post
from ..styles import PAGE_HEADING


class NovaPublicacaoState(rx.State):
    codArea: str = ""
    nomTitPubl: str = ""
    numAnoPubl: str = ""
    dscTipoPubl: str = "artigo"
    autrs: str = ""
    artg_nomPeriodArtg: str = ""
    artg_numVolumeArtg: str = ""
    artg_numEdicArtg: str = ""
    tese_dscGrauTese: str = ""
    tese_nomInstTese: str = ""
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

    def change_nomTitPubl(self, v: str):
        self.nomTitPubl = v

    def change_numAnoPubl(self, v: str):
        self.numAnoPubl = v

    def change_autrs(self, v: str):
        self.autrs = v

    def set_tipo(self, v: str):
        self.dscTipoPubl = v

    def change_artg_nomPeriodArtg(self, v: str):
        self.artg_nomPeriodArtg = v

    def change_artg_numVolumeArtg(self, v: str):
        self.artg_numVolumeArtg = v

    def change_artg_numEdicArtg(self, v: str):
        self.artg_numEdicArtg = v

    def change_tese_dscGrauTese(self, v: str):
        self.tese_dscGrauTese = v

    def change_tese_nomInstTese(self, v: str):
        self.tese_nomInstTese = v

    async def submit(self):
        self.success = False
        self.error = ""
        yield
        data = {
            "codArea": self.codArea,
            "nomTitPubl": self.nomTitPubl,
            "numAnoPubl": self.numAnoPubl,
            "dscTipoPubl": self.dscTipoPubl,
            "autrs": [{"nomAutr": a.strip()}
                      for a in self.autrs.split(",") if a.strip()],
        }
        tipo = self.dscTipoPubl
        if tipo == "artigo":
            data["artg"] = {
                "nomPeriodArtg": self.artg_nomPeriodArtg,
                "numVolumeArtg": self.artg_numVolumeArtg,
                "numEdicArtg": self.artg_numEdicArtg,
            }
        elif tipo == "tese":
            data["tese"] = {
                "dscGrauTese": self.tese_dscGrauTese,
                "nomInstTese": self.tese_nomInstTese,
            }
        elif tipo == "livro":
            data["livr"] = {}
        try:
            resp = await post("/publicacao", data)
            if resp.get("status") == "ok":
                self.success = True
                self._reset()
            else:
                self.error = "Erro ao criar publicação"
        except Exception as e:
            self.error = str(e)
        yield

    def _reset(self):
        self.codArea = ""
        self.nomTitPubl = ""
        self.numAnoPubl = ""
        self.dscTipoPubl = "artigo"
        self.autrs = ""
        self.artg_nomPeriodArtg = ""
        self.artg_numVolumeArtg = ""
        self.artg_numEdicArtg = ""
        self.tese_dscGrauTese = ""
        self.tese_nomInstTese = ""


def _field(label: str, handler, placeholder: str = "", **kwargs) -> rx.Component:
    return rx.vstack(
        rx.text(label, weight="bold", size="2"),
        rx.input(placeholder=placeholder, on_change=handler, **kwargs),
        width="100%",
        spacing="1",
    )


def nova_publicacao_page() -> rx.Component:
    s = NovaPublicacaoState
    return page_wrapper(
        breadcrumbs_items=[("Publicações", "/publicacoes"), ("Nova Publicação", None)],
        children=[
            rx.heading("Nova Publicação", **PAGE_HEADING),
            rx.cond(s.success,
                    rx.callout("Publicação cadastrada com sucesso!", icon="check",
                               color_scheme="green", width="100%")),
            rx.cond(s.error,
                    rx.callout(s.error, icon="alert_circle",
                               color_scheme="red", width="100%")),
            rx.vstack(
                rx.text("Área", weight="bold", size="2"),
                rx.select(s.area_names, on_change=s.change_area,
                          placeholder="Selecione a área", width="100%"),
                _field("Título", s.change_nomTitPubl),
                _field("Ano", s.change_numAnoPubl, placeholder="AAAA"),
                _field("Autores (separados por vírgula)", s.change_autrs),
                rx.text("Tipo", weight="bold", size="2"),
                rx.select(["artigo", "tese", "livro"],
                          value=s.dscTipoPubl,
                          on_change=s.set_tipo, width="100%"),
                rx.cond(s.dscTipoPubl == "artigo",
                        rx.vstack(
                            rx.divider(),
                            rx.text("Dados do Artigo", weight="bold", size="3"),
                            _field("Periódico", s.change_artg_nomPeriodArtg),
                            rx.hstack(
                                _field("Volume", s.change_artg_numVolumeArtg),
                                _field("Edição", s.change_artg_numEdicArtg),
                                spacing="4", width="100%",
                            ),
                            spacing="4", width="100%",
                        ),
                ),
                rx.cond(s.dscTipoPubl == "tese",
                        rx.vstack(
                            rx.divider(),
                            rx.text("Dados da Tese", weight="bold", size="3"),
                            _field("Grau", s.change_tese_dscGrauTese),
                            _field("Instituição", s.change_tese_nomInstTese),
                            spacing="4", width="100%",
                        ),
                ),
                rx.hstack(
                    rx.button("Salvar", color_scheme="blue", on_click=s.submit),
                    rx.link(rx.button("Cancelar", variant="soft", color_scheme="gray"),
                            href="/publicacoes"),
                    spacing="4", margin_top="1rem",
                ),
                spacing="4", width="100%",
            ),
        ],
    )
