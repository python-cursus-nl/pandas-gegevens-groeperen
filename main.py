from data import load_data, clean_data
from berekeningen import (
    woz_per_decennium,
    woz_per_regio,
    woz_per_regio_agg,
    gemiddelde_en_mediaan,
    per_regio_en_decennium,
    per_decennium_en_regio,
)

if __name__ == "__main__":
    clean_data()

    # Laad de data
    df = load_data()

    # Inspecteer de data
    print(df.head())
    print(df.tail())
    print(df.info())

    # Voer de verschillende berekeningen uit
    woz_per_decennium(df=df)
    woz_per_regio(df=df)
    woz_per_regio_agg(df=df)
    gemiddelde_en_mediaan(df=df)
    per_regio_en_decennium(df=df)
    per_decennium_en_regio(df=df)
