import reflex as rx

from ..components.layout import page_wrapper
from ..utils.api import get, post
from ..styles import PAGE_HEADING


class NovaPesquisaState(rx.State):
    codArea: str = ""
    nomPesq: str = ""
    dscPesq: str = ""
    datInicPesq: str = ""
    datFimPrevPesq: str = ""
    nomCrdn: str = ""
    dscEmailCrdn: str = ""
    nomInstCrdn: str = ""
    dscLogradEndr: str = ""
    numLogradEndr: str = ""
    nomBairroEndr: str = ""
    nomCidEndr: str = ""
    sglUfEndr: str = ""
    numCepEndr: str = ""
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

    def change_nomPesq(self, v: str):
        self.nomPesq = v

    def change_dscPesq(self, v: str):
        self.dscPesq = v

    def change_datInicPesq(self, v: str):
        self.datInicPesq = v

    def change_datFimPrevPesq(self, v: str):
        self.datFimPrevPesq = v

    def change_nomCrdn(self, v: str):
        self.nomCrdn = v

    def change_dscEmailCrdn(self, v: str):
        self.dscEmailCrdn = v

    def change_nomInstCrdn(self, v: str):
        self.nomInstCrdn = v

    def change_dscLogradEndr(self, v: str):
        self.dscLogradEndr = v

    def change_numLogradEndr(self, v: str):
        self.numLogradEndr = v

    def change_nomBairroEndr(self, v: str):
        self.nomBairroEndr = v

    def change_nomCidEndr(self, v: str):
        self.nomCidEndr = v

    def change_sglUfEndr(self, v: str):
        self.sglUfEndr = v

    def change_numCepEndr(self, v: str):
        self.numCepEndr = v

    async def submit(self):
        self.success = False
        self.error = ""
        yield
        try:
            resp = await post("/pesquisa", {
                "codArea": self.codArea,
                "nomPesq": self.nomPesq,
                "dscPesq": self.dscPesq,
                "datInicPesq": self.datInicPesq,
                "datFimPrevPesq": self.datFimPrevPesq,
                "nomCrdn": self.nomCrdn,
                "dscEmailCrdn": self.dscEmailCrdn,
                "nomInstCrdn": self.nomInstCrdn,
                "dscLogradEndr": self.dscLogradEndr,
                "numLogradEndr": self.numLogradEndr,
                "nomBairroEndr": self.nomBairroEndr,
                "nomCidEndr": self.nomCidEndr,
                "sglUfEndr": self.sglUfEndr,
                "numCepEndr": self.numCepEndr,
            })
            if resp.get("status") == "ok":
                self.success = True
                self._reset()
            else:
                self.error = "Erro ao criar pesquisa"
        except Exception as e:
            self.error = str(e)
        yield

    def _reset(self):
        self.codArea = ""
        self.nomPesq = ""
        self.dscPesq = ""
        self.datInicPesq = ""
        self.datFimPrevPesq = ""
        self.nomCrdn = ""
        self.dscEmailCrdn = ""
        self.nomInstCrdn = ""
        self.dscLogradEndr = ""
        self.numLogradEndr = ""
        self.nomBairroEndr = ""
        self.nomCidEndr = ""
        self.sglUfEndr = ""
        self.numCepEndr = ""


def _field(label: str, handler, placeholder: str = "", **kwargs) -> rx.Component:
    return rx.vstack(
        rx.text(label, weight="bold", size="2"),
        rx.input(placeholder=placeholder, on_change=handler, **kwargs),
        width="100%",
        spacing="1",
    )


def nova_pesquisa_page() -> rx.Component:
    s = NovaPesquisaState
    return page_wrapper(
        breadcrumbs_items=[("Pesquisas", "/pesquisas"), ("Nova Pesquisa", None)],
        children=[
            rx.heading("Nova Pesquisa", **PAGE_HEADING),
            rx.cond(s.success,
                    rx.callout("Pesquisa cadastrada com sucesso!", icon="check",
                               color_scheme="green", width="100%")),
            rx.cond(s.error,
                    rx.callout(s.error,
                               color_scheme="red", width="100%")),
            rx.vstack(
                rx.text("Área", weight="bold", size="2"),
                rx.select(s.area_names, on_change=s.change_area,
                          placeholder="Selecione a área", width="100%"),
                _field("Nome da Pesquisa", s.change_nomPesq),
                _field("Descrição", s.change_dscPesq, placeholder="Descrição da pesquisa"),
                rx.hstack(
                    _field("Data de Início", s.change_datInicPesq, placeholder="AAAA-MM-DD"),
                    _field("Término Previsto", s.change_datFimPrevPesq, placeholder="AAAA-MM-DD"),
                    spacing="4", width="100%",
                ),
                rx.divider(),
                rx.text("Coordenador (dados embutidos)", weight="bold", size="3"),
                _field("Nome", s.change_nomCrdn),
                _field("E-mail", s.change_dscEmailCrdn),
                _field("Instituição", s.change_nomInstCrdn),
                rx.text("Endereço do Coordenador", weight="bold", size="2"),
                _field("Logradouro", s.change_dscLogradEndr),
                rx.hstack(
                    _field("Número", s.change_numLogradEndr),
                    _field("Bairro", s.change_nomBairroEndr),
                    spacing="4", width="100%",
                ),
                rx.hstack(
                    _field("Cidade", s.change_nomCidEndr),
                    _field("UF", s.change_sglUfEndr, max_length=2),
                    _field("CEP", s.change_numCepEndr),
                    spacing="4", width="100%",
                ),
                rx.hstack(
                    rx.button("Salvar", color_scheme="blue", on_click=s.submit),
                    rx.link(rx.button("Cancelar", variant="soft", color_scheme="gray"),
                            href="/pesquisas"),
                    spacing="4", margin_top="1rem",
                ),
                spacing="4", width="100%",
            ),
        ],
    )
