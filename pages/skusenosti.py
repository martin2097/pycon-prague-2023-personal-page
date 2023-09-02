from dash import register_page
import dash_mantine_components as dmc
from utils import responzivny_stlpec_uprostred

register_page(__name__)

pracovne_skusenosti = [
    {
        "id": "code_tech_solutions",
        "logo": "/assets/codetech-solutions-logo.png",
        "nazov": "CodeTech Solutions - Django Vývojár",
        "popis": "Júl 2021 - súčasnosť",
        "obsah": [
            "Vývoj a údržba komplexných webových aplikácií v rámci Django frameworku.",
            "Implementácia backendových funkcií a optimalizácia výkonu.",
            "Spolupráca s frontendovým tímom na dosiahnutí plnej funkcionality a vizuálnej súladnosti.",
        ],
    },
    {
        "id": "datawave_analytics",
        "logo": "/assets/datawave-analytics-logo.png",
        "nazov": "DataWave Analytics - Datový Analytik",
        "popis": "Február 2019 - Jún 2021",
        "obsah": [
            "Vytvorenie automatizovaného systému spracovania a analýzy dát pre klientov.",
            "Implementácia algoritmov na identifikáciu vzorov a odchýlok v dátach.",
            "Spolupráca s tímom na zdokonaľovaní metód analytického modelovania.",
        ],
    },
    {
        "id": "bytecraft_technologies",
        "logo": "/assets/bytecraft-technologies-logo.png",
        "nazov": "ByteCraft Technologies - API vývojár",
        "popis": "August 2016 - Január 2019",
        "obsah": [
            "Vývoj backendu pre softvérové riešenia v oblasti riadenia procesov.",
            "Návrh a implementácia REST API pre komunikáciu medzi systémami.",
            "Úzka spolupráca s tímom pre zabezpečenie interoperability a bezchybného behu systému.",
        ],
    },
]

vzdelanie = [
    {
        "id": "magister",
        "logo": "/assets/tu-vyvojoville-logo.png",
        "nazov": "Technická Univerzita Vývojoville - Softvérové Inžinierstvo",
        "popis": "2015 - 2017 - Magisterské štúdium",
        "obsah": [
            "Hlbšie štúdium softvérového inžinierstva vrátane agilných metodológií vývoja, softvérového návrhu a "
            "testovania.",
            "Diplomová práca sa zaoberala optimalizáciou algoritmov pre analýzu dát a ich implementáciou v prostredí "
            "Python.",
        ],
    },
    {
        "id": "bakalar",
        "logo": "/assets/univerzita-kodujov-logo.png",
        "nazov": "Univerzita Kódujov - Informatika",
        "popis": "2011 - 2015 - Bakalárske štúdium",
        "obsah": [
            "Zameranie na teoretické základy programovania, algoritmov a dátových štruktúr.",
            "Praktické skúsenosti získané v rámci projektov využívajúcich jazyk Python a C++",
        ],
    },
]


def vytvor_nazov_akordeonu(nazov, logo, popis):
    return dmc.AccordionControl(
        dmc.Grid(
            [
                dmc.Col(
                    [
                        dmc.Avatar(src=logo, radius="xl", size="lg"),
                    ],
                    span="content",
                ),
                dmc.Col(
                    [
                        dmc.Text(nazov),
                        dmc.Text(popis, size="sm", weight=400, color="dimmed"),
                    ],
                    span="auto",
                ),
            ]
        )
    )


def vytvor_obsah_akordeonu(list_s_obsahom):
    return dmc.AccordionPanel(
        dmc.List(
            [
                dmc.ListItem(dmc.Text([dmc.Text(obsah, size="sm")]))
                for obsah in list_s_obsahom
            ],
            pl=10,
            pr=30,
            pb=10,
        )
    )


def vytvor_akordeon(data_pre_akordeon):
    return [
        dmc.AccordionItem(
            [
                vytvor_nazov_akordeonu(
                    jedna_polozka["nazov"],
                    jedna_polozka["logo"],
                    jedna_polozka["popis"],
                ),
                vytvor_obsah_akordeonu(jedna_polozka["obsah"]),
            ],
            value=jedna_polozka["id"],
        )
        for jedna_polozka in data_pre_akordeon
    ]


layout = responzivny_stlpec_uprostred(
    dmc.Accordion(
        chevronPosition="left",
        variant="filled",
        radius="lg",
        children=[
            dmc.Divider(
                label="Pracovné skúsenosti",
                size="sm",
                styles={"label": {"font-size": "25px", "font-weight": 600}},
                mt=20,
                mb=10,
            ),
        ]
        + vytvor_akordeon(pracovne_skusenosti)
        + [
            dmc.Divider(
                label="Vzdelanie",
                size="sm",
                styles={"label": {"font-size": "25px", "font-weight": 600}},
                mt=20,
                mb=10,
            ),
        ]
        + vytvor_akordeon(vzdelanie),
    )
)
