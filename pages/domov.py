from dash import register_page
import dash_mantine_components as dmc
from utils import responzivny_stlpec_uprostred

register_page(__name__, path="/")


def gradient_text(text, **kwargs):
    return dmc.Text(
        text,
        variant="gradient",
        gradient={"from": "blue", "to": "teal", "deg": 45},
        **kwargs
    )


layout = responzivny_stlpec_uprostred(
    dmc.Center(
        dmc.Stack(
            [
                dmc.Text("Vitajte na mojich osobných stránkach!"),
                gradient_text("Som Levo,", size=40, weight=600),
                dmc.Text(
                    [
                        "váš cestovateľ digitálnym priestorom. S piatimi rokmi skúseností ako vášnivý ",
                        gradient_text(
                            "PYTHON",
                            size=20,
                            weight=600,
                            span=True,
                        ),
                        " programátor, sa pohybujem medzi kódovaním a tvorbou so ",
                        gradient_text(
                            "ZÁPALOM",
                            size=20,
                            weight=600,
                            span=True,
                        ),
                        " a nekonečnou ",
                        gradient_text(
                            "KREATIVITOU",
                            size=20,
                            weight=600,
                            span=True,
                        ),
                        ".",
                    ],
                ),
            ],
            spacing=0,
            id="home-stack",
        ),
        style={"height": "calc(100vh - 48px)"},
    )
)
