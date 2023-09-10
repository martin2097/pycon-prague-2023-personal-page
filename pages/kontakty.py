from dash import register_page, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from utils import responzivny_stlpec_uprostred, ikona_s_odkazom

register_page(__name__)

layout = responzivny_stlpec_uprostred(
    dmc.Center(
        dmc.Stack(
            [
                dmc.Text("Kontaktujte Ma", size=40),
                dmc.Space(h=40),
                dmc.Text(
                    "Pokiaľ máte akékoľvek otázky, nápady alebo spätnú väzbu, neváhajte ma kontaktovať.",
                ),
                dmc.Space(h=20),
                dmc.Stack(
                    [
                        dmc.Group(
                            [
                                ikona_s_odkazom(
                                    "mailto:levo@fake.mail",
                                    "material-symbols:mail",
                                ),
                                dmc.Text("levo@fake.mail"),
                            ],
                        ),
                        dmc.Group(
                            [
                                ikona_s_odkazom(
                                    "https://linkedin.com/in/levo",
                                    "mdi:linkedin",
                                ),
                                dmc.Text("/in/levo/"),
                            ],
                        ),
                    ],
                    spacing=0,
                ),
            ],
            spacing=0,
            align="center",
            id="contact-stack",
        ),
        style={"height": "calc(100vh - 48px)"},
    )
)
