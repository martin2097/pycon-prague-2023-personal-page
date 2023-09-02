import dash_mantine_components as dmc
from dash import dcc, html
from dash_iconify import DashIconify


def responzivny_stlpec_uprostred(obsah):
    return (
        dmc.Grid(
            dmc.Col(
                obsah,
                span=10,
                sm=8,
                xl=6,
                offset=1,
                offsetSm=2,
                offsetXl=3,
                p=0,
            ),
            m=0,
        ),
    )


def navigacny_panel(odkazy, logo):
    return dmc.Header(
        children=[
            dmc.Stack(
                dmc.Group(
                    [
                        dcc.Link(
                            dmc.ActionIcon(
                                DashIconify(
                                    icon=logo,
                                    height=35,
                                    width=35,
                                ),
                                variant="transparent",
                                id={"type": "odkaz-menu", "index": "logo"},
                            ),
                            href="/",
                        ),
                        dmc.Group(
                            [
                                dmc.MediaQuery(
                                    dmc.NavLink(
                                        label=odkazy[link]["label"],
                                        href=link,
                                        style={
                                            "padding": "7px",
                                            "width": "auto",
                                        },
                                        styles={
                                            "label": {
                                                "color": "#868E96",
                                                "font-weight": "500",
                                                "font-size": "16px",
                                            },
                                        },
                                    ),
                                    smallerThan="sm",
                                    styles={"display": "none"},
                                )
                                for link in odkazy
                            ]
                            + [
                                dmc.ActionIcon(
                                    DashIconify(
                                        icon="radix-icons:blending-mode",
                                        width=25,
                                    ),
                                    variant="transparent",
                                    id="tlacidlo-zmena-temy",
                                ),
                            ]
                            + [
                                dmc.MediaQuery(
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="radix-icons:hamburger-menu",
                                            width=25,
                                        ),
                                        variant="transparent",
                                        id="tlacidlo-menu",
                                    ),
                                    largerThan="sm",
                                    styles={"display": "none"},
                                ),
                            ],
                            position="right",
                        ),
                    ],
                    position="apart",
                    style={"margin-right": "2vh", "margin-left": "2vh"},
                ),
                justify="center",
                style={"height": "100%"},
            ),
            dmc.Drawer(
                id="vysuvacie-menu",
                overlayOpacity=0.55,
                overlayBlur=3,
                size=300,
                children=dmc.Stack(
                    [
                        html.A(
                            dmc.NavLink(
                                label=odkazy[link]["label"],
                                href=link,
                                style={
                                    "padding": "7px",
                                    "width": "auto",
                                },
                                styles={
                                    "label": {
                                        "color": "#868E96",
                                        "font-weight": "500",
                                        "font-size": "24px",
                                    },
                                },
                            ),
                            id={
                                "type": "odkaz-menu",
                                "index": link,
                            },
                        )
                        for link in odkazy
                    ],
                    align="center",
                    spacing=5,
                ),
            ),
        ],
        height=40,
        fixed=True,
        style={"margin-bottom": "3px"},
        withBorder=False,
    )
