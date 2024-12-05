import pandas as pd


def clean_data():
    # Laad de data met de juiste parameters
    df = pd.read_csv(
        "woz.csv",
        sep=";",  # gebruik puntkomma als scheidingsteken
        quotechar='"',  # verwijder aanhalingstekens
        na_values="       .",  # Vervang '       .' door NaN voor missende waarden
        encoding="utf-8",
    )  # gebruik UTF-8 encoding

    # Hernoem de kolommen
    df = df.rename(
        columns={
            "RegioS": "Regio_Code",
            "Eigendom": "Type Eigendom",
            "GemiddeldeWOZWaardeVanWoningen_1": "Gemiddelde WOZ-waarde",
        }
    )

    # Maak de jaartallen bruikbaar door de 'JJ00' te verwijderen
    df["Jaar"] = df.loc[:, "Perioden"].str[:4].astype(int)

    # Maak een kolom decennium
    df["Decennium"] = df.loc[:, "Jaar"] // 10 * 10

    # Maak de codes leesbaar
    # Maak een mapping voor regio codes naar namen
    regio_mapping = {
        "NL01  ": "Nederland",
        "LD01  ": "Noord-Nederland",
        "LD02  ": "Oost-Nederland",
        "LD03  ": "West-Nederland",
        "LD04  ": "Zuid-Nederland",
        "PV20  ": "Groningen",
        "PV21  ": "Fryslân",
        "PV22  ": "Drenthe",
        "PV23  ": "Overijssel",
        "PV24  ": "Flevoland",
        "PV25  ": "Gelderland",
        "PV26  ": "Utrecht",
        "PV27  ": "Noord-Holland",
        "PV28  ": "Zuid-Holland",
        "PV29  ": "Zeeland",
        "PV30  ": "Noord-Brabant",
        "PV31  ": "Limburg",
    }

    # Filter de data op alleen de regio's die we willen behouden
    # Dus: NL, vier regio's en alle provincies.
    df = df[df["Regio_Code"].isin(regio_mapping.keys())]

    # Vervang regio codes door namen
    df["Regio"] = df["Regio_Code"].map(regio_mapping)

    # Vervang de eigendom codes
    eigendom_mapping = {
        "T001132": "Totaal",
        "1014800": "Koopwoningen",
        "A047047": "Huurwoning in bezit woningcorporatie",
        "A047048": "Eigendom overige verhuurders",
    }
    df["Type Eigendom"] = df["Type Eigendom"].map(eigendom_mapping)

    # Drop columns die niet meer nodig zijn
    df = df.drop(["Regio_Code", "Perioden", "ID"], axis=1)

    # Verander volgorde kolommen
    volgorde = ["Regio", "Decennium", "Jaar", "Gemiddelde WOZ-waarde"]
    df = df[volgorde]

    # Sla het opgeschoonde bestand op
    df.to_csv("woz_opgeschoond.csv", sep=";", index=False)


def load_data():
    df = pd.read_csv(
        "woz_opgeschoond.csv",
        sep=";",
        dtype={
            "Regio": "string",
            "Type Eigendom": "string",
        },
    )

    return df
