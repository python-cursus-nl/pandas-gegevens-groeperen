def woz_per_decennium(df):
    # Groepeer op decennium en bereken de gemiddelde WOZ-waarde
    per_decennium = df.groupby("Decennium")["Gemiddelde WOZ-waarde"].mean()

    print("Gemiddelde WOZ-waarde per decennium:")
    print(per_decennium)


def woz_per_regio(df):
    # Groepeer op regio en bereken de gemiddelde WOZ-waarde
    per_regio = (
        df.groupby("Regio")["Gemiddelde WOZ-waarde"].mean().sort_values().round(2)
    )

    print("Gemiddelde WOZ-waarde per regio:")
    print(per_regio)


def woz_per_regio_agg(df):
    # Groepereer op regio en bereken de gemiddelde WOZ-waarde
    per_regio = df.groupby("Regio").agg({"Gemiddelde WOZ-waarde": "mean"})

    # per_regio is nu een DataFrame
    per_regio = per_regio.sort_values(by="Gemiddelde WOZ-waarde").round(2)
    print("Gemiddelde WOZ-waarde per regio:")
    print(per_regio)


def gemiddelde_en_mediaan(df):
    per_regio = df.groupby("Decennium").agg(
        gemiddelde=("Gemiddelde WOZ-waarde", "mean"),
        mediaan=("Gemiddelde WOZ-waarde", "median"),
    )

    per_regio = (
        df.groupby("Decennium")["Gemiddelde WOZ-waarde"]
        .agg(["mean", "median"])
        .sort_values(by="mean")
        .round(2)
    )

    # per_regio = per_regio.sort_values(by="gemiddelde").round(2)
    print(per_regio)


def gemiddelde_en_mediaan_alt(df):
    # Alternatieve manier als je verschillende aggregaties wilt op één kolom
    per_regio = (
        df.groupby("Decennium")["Gemiddelde WOZ-waarde"]
        .agg(["mean", "median"])
        .sort_values(by="mean")
        .round(2)
    )
    print(per_regio)


def per_regio_en_decennium(df):
    result = df.groupby(["Regio", "Decennium"])["Gemiddelde WOZ-waarde"].mean().round(2)
    print(result)


def per_decennium_en_regio(df):
    result = df.groupby(["Decennium", "Regio"])["Gemiddelde WOZ-waarde"].mean().round(2)
    print(result)
