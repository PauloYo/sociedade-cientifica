import reflex as rx

from rxconfig import config as rx_config

from .pages.dashboard import dashboard_page
from .pages.areas import areas_page
from .pages.area_detail import area_detail_page, AreaDetailState
from .pages.pesquisas import pesquisas_page
from .pages.publicacoes import publicacoes_page
from .pages.softwares import softwares_page
from .pages.nova_pesquisa import nova_pesquisa_page, NovaPesquisaState
from .pages.nova_publicacao import nova_publicacao_page, NovaPublicacaoState
from .pages.novo_software import novo_software_page, NovoSoftwareState
from .pages.nova_area import nova_area_page, NovaAreaState
from .pages.busca import busca_page
from .state.app_state import AppState
from .state.area_state import AreaState
from .state.pesquisa_state import PesquisaState
from .state.publicacao_state import PublicacaoState
from .state.software_state import SoftwareState

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
             on_load=PublicacaoState.load_publicacoes)
app.add_page(softwares_page, route="/softwares", title="Softwares & Tutoriais | Sociedade Científica",
             on_load=SoftwareState.load_softwares)
app.add_page(nova_pesquisa_page, route="/pesquisas/nova", title="Nova Pesquisa | Sociedade Científica",
             on_load=NovaPesquisaState.load_areas)
app.add_page(nova_publicacao_page, route="/publicacoes/nova",
             title="Nova Publicação | Sociedade Científica",
             on_load=NovaPublicacaoState.load_areas)
app.add_page(novo_software_page, route="/softwares/novo",
             title="Novo Software | Sociedade Científica",
             on_load=NovoSoftwareState.load_areas)
app.add_page(busca_page, route="/busca", title="Busca | Sociedade Científica")
app.add_page(nova_area_page, route="/areas/nova", title="Nova Área | Sociedade Científica")
