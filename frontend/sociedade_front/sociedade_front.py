import reflex as rx

from rxconfig import config as rx_config

from .pages.dashboard import dashboard_page
from .pages.areas import areas_page
from .pages.pesquisas import pesquisas_page
from .pages.publicacoes import publicacoes_page
from .pages.softwares import softwares_page
from .styles import THEME

app = rx.App(
    theme=THEME,
)

app.add_page(dashboard_page, route="/", title="Dashboard | Sociedade Científica")
app.add_page(areas_page, route="/areas", title="Áreas | Sociedade Científica")
app.add_page(pesquisas_page, route="/pesquisas", title="Pesquisas | Sociedade Científica")
app.add_page(publicacoes_page, route="/publicacoes", title="Publicações | Sociedade Científica")
app.add_page(softwares_page, route="/softwares", title="Softwares | Sociedade Científica")
