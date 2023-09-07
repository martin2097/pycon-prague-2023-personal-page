from dash import register_page, html
import dash_mantine_components as dmc
from utils import responzivny_stlpec_uprostred

register_page(__name__)


def karta_projekt(image, title, description, odkaz):
    return dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Image(
                    src=image,
                    height=160,
                )
            ),
            dmc.Stack(
                [
                    dmc.Text(title, weight=500),
                    dmc.Text(
                        description,
                        size="sm",
                        color="dimmed",
                        style={"height": "65px"},
                    ),
                    dmc.Anchor(
                        dmc.Button(
                            "Navštíviť projekt",
                            variant="light",
                            fullWidth=True,
                            mt="md",
                            radius="md",
                        ),
                        href=odkaz,
                    ),
                ],
                spacing=5,
                mt=5,
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"height": "330px"},
    )


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
