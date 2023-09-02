from dash import (
    Dash,
    html,
    dcc,
    page_container,
    Output,
    Input,
    State,
    clientside_callback,
    ALL,
)
from utils import navigacny_panel
import dash_mantine_components as dmc

app = Dash(__name__, use_pages=True)
server = app.server

links = {
    "o-mne": {"label": "O mne"},
    "skusenosti": {"label": "Skúsenosti"},
    "projekty": {"label": "Projekty"},
    "kontakty": {"label": "Kontaktuj ma"},
}


app.layout = dmc.MantineProvider(
    [
        dcc.Store(id="ulozisko-temy", storage_type="local"),
        navigacny_panel(links, "tabler:square-rounded-letter-l"),
        html.Div(page_container, style={"margin-top": "40px"}),
    ],
    theme={"colorScheme": "dark"},
    withGlobalStyles=True,
    id="provider-temy",
)


clientside_callback(
    """function(n_clicks, opened) { return !opened }""",
    Output("vysuvacie-menu", "opened"),
    Input("tlacidlo-menu", "n_clicks"),
    State("vysuvacie-menu", "opened"),
    prevent_initial_call=True,
)


clientside_callback(
    """function(n_clicks, data) {
        if (data) {
            if (n_clicks) {
                const scheme = data["colorScheme"] == "dark" ? "light" : "dark"
                return { colorScheme: scheme } 
            }
            return dash_clientside.no_update
        } else {
            return { colorScheme: "dark" }
        }
    }""",
    Output("ulozisko-temy", "data"),
    Input("tlacidlo-zmena-temy", "n_clicks"),
    State("ulozisko-temy", "data"),
)


clientside_callback(
    """ function(data) { return data } """,
    Output("provider-temy", "theme"),
    Input("ulozisko-temy", "data"),
)


clientside_callback(
    """
        function (i) {
            return false
        }
    """,
    Output("vysuvacie-menu", "opened", allow_duplicate=True),
    Input({"index": ALL, "type": "odkaz-menu"}, "n_clicks"),
    prevent_initial_call=True,
)


if __name__ == "__main__":
    app.run(debug=False)
