import reflex as rx

from rxconfig import config as rx_config

from .pages.dashboard import dashboard_page
from .pages.areas import areas_page
from .pages.area_detail import area_detail_page, AreaDetailState
from .pages.pesquisas import pesquisas_page
from .pages.publicacoes import publicacoes_page
from .pages.softwares import softwares_page
from .state.app_state import AppState
from .state.area_state import AreaState
from .state.pesquisa_state import PesquisaState

app = rx.App()

app.add_page(dashboard_page, route="/", title="Dashboard | Sociedade Científica",
             on_load=AppState.load_dashboard)
app.add_page(areas_page, route="/areas", title="Áreas | Sociedade Científica",
             on_load=AreaState.load_areas)
app.add_page(area_detail_page, route="/areas/[area_id]",
             title="Detalhe da Área | Sociedade Científica",
             on_load=AreaDetailState.load_area)
app.add_page(pesquisas_page, route="/pesquisas", title="Pesquisas | Sociedade Científica",
             on_load=PesquisaState.load_pesquisas)
app.add_page(publicacoes_page, route="/publicacoes", title="Publicações | Sociedade Científica",
             on_load=AppState.load_publicacoes)
app.add_page(softwares_page, route="/softwares", title="Softwares | Sociedade Científica",
             on_load=AppState.load_softwares)
