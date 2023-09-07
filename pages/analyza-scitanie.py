import pandas as pd
from dash import register_page, callback, Input, Output, State, dcc, html
import dash_mantine_components as dmc
from utils import responzivny_stlpec_uprostred
from plotly.express import bar
import dash_ag_grid as dag
import numpy as np

register_page(__name__)

df = pd.read_csv("sldb2021_vzdelani_vek2_pohlavi_iba_kraje.csv")
df = df[
    (df["uzemi_txt"].isin(["Česká republika", "Kraj Vysočina", "Hlavní město Praha"]))
    | (df["uzemi_txt"].str.contains("kraj$"))
]
df = df[df["pohlavi_txt"].isin(["muž", "žena"])]

vzdelanie_mapovanie = {
    "Bez vzdělání": "Iné",
    "Nezjištěno": "Iné",
    "Neúplné základní vzdělání": "Základné",
    "Nižší střední a střední vzdělání": "SŠ (bez maturity)",
    "Nástavbové vzdělání": "Stredoškolské",
    "Pomaturitní studium": "Stredoškolské",
    "Vysokoškolské bakalářské vzdělání": "Vysokoškolské",
    "Vysokoškolské doktorské vzdělání": "Vysokoškolské",
    "Vysokoškolské magisterské vzdělání": "Vysokoškolské",
    "Vyšší odborné vzdělání": "Stredoškolské",
    "Vyšší odborné vzdělání v konzervatoři": "Stredoškolské",
    "Základní vzdělání": "Základné",
    "Úplné střední odborné vzdělání": "Stredoškolské",
    "Úplné střední všeobecné vzdělání": "Stredoškolské",
}

df.replace({"vzdelani_txt": vzdelanie_mapovanie}, inplace=True)


def stat_card(id, label):
    return dmc.Card(
        dmc.Stack(
            [dmc.Text(label, weight=600, size=15), dmc.Text(id=id)],
            align="center",
            spacing="xs",
        ),
        withBorder=True,
        shadow="sm",
        radius="lg",
        p=8,
    )


layout = responzivny_stlpec_uprostred(
    dmc.Stack(
        [
            dmc.Divider(
                label="Úroveň vzdelania v ČR",
                size="sm",
                styles={"label": {"font-size": "25px", "font-weight": 600}},
                mt=20,
            ),
            dmc.Select(
                id="vyber-uzemi",
                value="Česká republika",
                label="Vyberte oblasť:",
                data=[
                    {"value": moznost, "label": moznost}
                    for moznost in df["uzemi_txt"].drop_duplicates().sort_values()
                ],
                styles={"label": {"margin-bottom": "7px"}},
            ),
            dmc.Grid(
                [
                    dmc.Col(
                        [
                            stat_card(
                                id="pocet-obyvatel", label="Celkový počet obyvateľov"
                            )
                        ],
                        sm=6,
                    ),
                    dmc.Col(
                        [
                            stat_card(
                                id="podiel-vs", label="Podiel vysokoškolsky vzdelaných"
                            )
                        ],
                        sm=6,
                    ),
                ]
            ),
            dmc.Divider(
                label="Prehľad",
                size="sm",
                styles={"label": {"font-size": "18px", "font-weight": 600}},
            ),
            dmc.Card(
                dcc.Graph(
                    id="graf-vzdelanie",
                    config={
                        "displayModeBar": False,
                        "scrollZoom": False,
                        "doubleClick": False,
                        "showAxisDragHandles": False,
                    },
                ),
                withBorder=True,
                shadow="sm",
                radius="lg",
                p=30,
            ),
            dmc.Divider(
                label="Porovnanie podľa pohlaví",
                size="sm",
                styles={"label": {"font-size": "18px", "font-weight": 600}},
            ),
            html.Div(id="tabulka-vzdelanie-detail"),
        ],
        spacing="md",
    )
)


@callback(
    Output("pocet-obyvatel", "children"),
    Output("podiel-vs", "children"),
    Input("vyber-uzemi", "value"),
)
def pocet_obyvatelov(uzemie):
    pocet = df[df["uzemi_txt"] == uzemie]["hodnota"].sum()
    podiel = (
        df[(df["uzemi_txt"] == uzemie) & (df["vzdelani_txt"] == "Vysokoškolské")][
            "hodnota"
        ].sum()
        / df[df["uzemi_txt"] == uzemie]["hodnota"].sum()
    )
    return "{:,d}".format(pocet), "{:.2%}".format(podiel)


@callback(
    Output("graf-vzdelanie", "figure"),
    Input("vyber-uzemi", "value"),
    Input("ulozisko-temy", "modified_timestamp"),
    State("ulozisko-temy", "data"),
)
def data_do_grafu(uzemie, timestamp, theme):
    w_df = df.copy()
    w_df = w_df[w_df["uzemi_txt"] == uzemie]
    w_df = w_df.groupby(by=["vzdelani_txt"])["hodnota"].sum().reset_index()
    w_df["podiel"] = w_df["hodnota"] / w_df["hodnota"].sum()

    fig = bar(
        w_df,
        x="vzdelani_txt",
        y="hodnota",
        custom_data="podiel",
        category_orders={
            "vzdelani_txt": [
                "Základné",
                "SŠ (bez maturity)",
                "Stredoškolské",
                "Vysokoškolské",
                "Iné",
            ]
        },
    )

    fig.update_traces(
        marker_color="rgb(207,219,137)",
        hovertemplate="%{x}<br>%{y:,.0f} obyvateľov<br>%{customdata[0]:.2%} obyvateľstva",
    )

    fig.update_layout(
        height=300,
        yaxis_title=None,
        xaxis_title=None,
        dragmode=False,
        bargap=0.4,
        yaxis=dict(
            gridcolor="whitesmoke" if theme["colorScheme"] == "light" else "#484848",
            gridwidth=0.2,
            zeroline=False,
            color="#444" if theme["colorScheme"] == "light" else "#FFFFFF",
            nticks=5,
        ),
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(
            family="Segoe UI",
            size=14,
        ),
        margin=dict(r=0, b=10, t=0, l=0),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            color="#444" if theme["colorScheme"] == "light" else "#FFFFFF",
        ),
    )
    return fig


@callback(
    Output("tabulka-vzdelanie-detail", "children"),
    Input("vyber-uzemi", "value"),
    Input("ulozisko-temy", "modified_timestamp"),
    State("ulozisko-temy", "data"),
)
def obnov_tabulku(uzemie, timestamp, theme):
    w_df = df.copy()
    w_df = w_df[w_df["uzemi_txt"] == uzemie]

    w_df = pd.crosstab(
        index=w_df["vzdelani_txt"],
        columns=w_df["pohlavi_txt"],
        values=w_df["hodnota"],
        aggfunc=np.sum,
        normalize="columns",
    ).reset_index()

    columnDefs = [
        {"headerName": "Vzdelanie", "field": "vzdelani_txt", "minWidth": 150},
        {
            "headerName": "Muži",
            "field": "muž",
            "valueFormatter": {"function": "d3.format(',.1%')(params.value)"},
        },
        {
            "headerName": "Ženy",
            "field": "žena",
            "valueFormatter": {"function": "d3.format(',.1%')(params.value)"},
        },
    ]
    defaultColDef = {
        "resizable": True,
        "sortable": True,
        "editable": False,
        "filter": False,
    }

    grid = dag.AgGrid(
        className="ag-theme-alpine-dark"
        if theme["colorScheme"] == "dark"
        else "ag-theme-alpine",
        columnDefs=columnDefs,
        rowData=w_df.to_dict("records"),
        columnSize="sizeToFit",
        defaultColDef=defaultColDef,
        dashGridOptions={
            "suppressCellFocus": True,
            "enableCellTextSelection": True,
            "animateRows": True,
            "domLayout": "autoHeight",
        },
    )
    return grid
