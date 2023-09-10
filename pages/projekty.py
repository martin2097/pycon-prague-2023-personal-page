from dash import register_page, html
import dash_mantine_components as dmc
from utils import responzivny_stlpec_uprostred, karta_projekt

register_page(__name__)


layout = responzivny_stlpec_uprostred(
    [
        dmc.Divider(
            label="Realizované projekty",
            size="sm",
            styles={"label": {"font-size": "25px", "font-weight": 600}},
            mt=20,
            mb=10,
        ),
        dmc.Grid(
            [
                dmc.Col(
                    [
                        karta_projekt(
                            image="/assets/analyza-vzdelania.png",
                            title="Analýza úrovne vzdelania v ČR",
                            description="Interaktívny dashboard k úrovni vzdelania v ČR z dát štatistického úradu zo "
                            "sčítania obyvateľstva v roku 2021.",
                            odkaz="analyza-scitanie",
                        )
                    ],
                    sm=6,
                )
            ],
            gutterSm=30,
            gutter=0,
            style={"margin": "0px"},
        ),
    ]
)
