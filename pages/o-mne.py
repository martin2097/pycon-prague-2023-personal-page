from dash import register_page
import dash_mantine_components as dmc
from utils import responzivny_stlpec_uprostred

register_page(__name__)

o_mne_text = (
    "Prvý kontakt s programovaním som mal ešte v študentských časoch a odvtedy sa moje kódovanie stalo "
    "súčasťou môjho DNA. Mojím poslaním je prinášať riešenia prostredníctvom kódu, ktoré majú skutočný dopad na svet. "
    "Vo svojej voľnej chvíli ma nájdete buď hlboko ponoreného do nového projektu alebo hľadajúceho inšpiráciu v "
    "prírode a technológii."
)

tech_schopnosti = [
    "Python",
    "Django",
    "Pandas",
    "Matplotlib",
    "Scikit-learn",
]

makke_schopnosti = [
    "Silné analytické a riešiteľské schopnosti",
    "Komunikačné zručnosti",
    "Schopnosť efektívne pracovať v tíme",
    "Flexibilita a schopnosť rýchlo sa prispôsobiť novým technológiám",
    "Kreativita pri hľadaní neštandardných riešení",
]

layout = responzivny_stlpec_uprostred(
    dmc.Stack(
        [
            dmc.Divider(
                label="Kto som?",
                size="sm",
                styles={"label": {"font-size": "25px", "font-weight": 600}},
            ),
            dmc.Grid(
                [
                    dmc.Col([dmc.Text(o_mne_text, align="justify")], sm=8),
                    dmc.Col(
                        [dmc.Image(src="/assets/profile_picture_pingu.svg")],
                        sm=4,
                    ),
                ],
                m=0,
            ),
            dmc.Divider(
                label="Moje schopnosti",
                size="sm",
                styles={"label": {"font-size": "25px", "font-weight": 600}},
            ),
            dmc.Grid(
                [
                    dmc.Col(
                        [
                            dmc.Text("Technické schopnosti:", mb=5),
                            dmc.List([dmc.ListItem(item) for item in tech_schopnosti]),
                        ],
                        sm=6,
                    ),
                    dmc.Col(
                        [
                            dmc.Text("Mäkké schopnosti:", mb=5),
                            dmc.List([dmc.ListItem(item) for item in makke_schopnosti]),
                        ],
                        sm=6,
                    ),
                ],
                m=0,
            ),
        ],
        spacing=10,
        mt=20,
    )
)
