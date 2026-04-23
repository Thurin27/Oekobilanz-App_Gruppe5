# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "marimo",
#   "pandas",
#   "altair",
# ]
# ///

import marimo

__generated_with = "0.19.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair as alt
    # Weitere Imports hier ergänzen (z.B. plotly)
    return alt, mo, pd


@app.cell
def _(mo):
    mo.md(r"""
    # 🌱 Ökobilanz-App für Erneuerbare Energien

    **Entwickelt von: [Gruppe 5]**

    Unsere App ermöglicht es Nutzern, die CO₂-Bilanz verschiedener erneuerbarer Energiequellen wie z. B. Solar-, Wind- und Wasserkraft zu berechnen und miteinander zu vergleichen. Ziel ist es, ein besseres Verständnis für die Umweltwirkungen nachhaltiger Energieformen zu vermitteln.
    Die App dient zudem der Analyse und anschaulichen Visualisierung der CO₂-Bilanz erneuerbarer Energiesysteme. Durch die Eingabe verschiedener Parameter lassen sich Emissionen, Einsparpotenziale und Umweltwirkungen berechnen.

    ---
    """)
    return


@app.cell
def _():
    # =================================================================
    # DATEN
    # =================================================================
    # Hier eure Daten einfügen
    # 
    # Tipp: Recherchiert auf https://www.probas.umweltbundesamt.de
    # 
    # Beispielstruktur:
    # energietraeger_daten = pd.DataFrame({
    #     "Energieträger": ["Photovoltaik", "Windkraft", ...],
    #     "CO2_eq_g_kWh": [40, 10, ...],
    #     ...
    # })

    # TODO: Eure Daten hier einfügen
    #energietraeger_daten = pd.DataFrame({
    #    "Energieträger": ["Beispiel 1", "Beispiel 2"],
    #    "CO2_eq_g_kWh": [0, 0],
        # Weitere Spalten ergänzen...
    #})
    return


@app.cell
def _(pd):
    # Beispieldaten angelehnt an ProBas/GEMIS-Werte
    # Quelle: Typische Werte aus Lebenszyklusanalysen

    energietraeger_daten = pd.DataFrame({
        "Energieträger": [
            "Photovoltaik (Dach)", 
            "Photovoltaik (Freifläche)",
            "Windkraft (Onshore)", 
            "Windkraft (Offshore)",
            "Wasserkraft (Laufwasser)",
            "Biomasse (Holz-HKW)",
            "Biogas (landw.)",
            "Solarthermie",
            "Geothermie"
        ],
        "CO2_eq_g_kWh": [40, 35, 10, 12, 4, 30, 170, 25, 38],  # g CO2-eq/kWh
        "KEA_MJ_kWh": [0.45, 0.40, 0.08, 0.10, 0.02, 0.15, 0.85, 0.30, 0.42],  # MJ/kWh kumulierter Energieaufwand
        "Flaechenbedarf_m2_kW": [7, 20, 30, 15, 0.5, 500, 300, 3, 2],  # m²/kW installierte Leistung
        "Lebensdauer_Jahre": [25, 25, 20, 25, 80, 20, 15, 20, 30],
        "Erntefaktor": [10, 12, 50, 45, 200, 8, 3, 15, 12],  # Energy Return on Investment
        "Kategorie": [
            "Solar", "Solar", "Wind", "Wind", "Wasser", 
            "Biomasse", "Biomasse", "Solar", "Geothermie"
        ]
    })
    energietraeger_daten
    return (energietraeger_daten,)


@app.cell
def _(alt, energietraeger_daten):
    # Diagramm erstellen, Code mit dataframe gui erstellt
    _chart = (
        alt.Chart(energietraeger_daten)
        .mark_point()
        .encode(
            x=alt.X(field='Energieträger', type='nominal'),
            y=alt.Y(field='CO2_eq_g_kWh', type='quantitative', aggregate='mean'),
            tooltip=[
                alt.Tooltip(field='Energieträger'),
                alt.Tooltip(field='CO2_eq_g_kWh', aggregate='mean', format=',.0f')
            ]
        )
        .properties(
            height=290,
            width='container',
            config={
                'axis': {
                    'grid': True
                }
            }
        )
    )
    _chart
    return


@app.cell
def _(energietraeger_daten, mo):
    # =================================================================
    # BENUTZEROBERFLÄCHE (UI)
    # =================================================================
    # Hier interaktive Elemente erstellen
    #
    # Beispiele:
    # - Dropdown: mo.ui.dropdown(options=[...], label="...")
    # - Slider:   mo.ui.slider(start=0, stop=100, value=50, label="...")
    # - Checkbox: mo.ui.checkbox(label="...")
    #
    # Dokumentation: https://docs.marimo.io/api/inputs/

    # TODO: Eure UI-Elemente hier erstellen

    # Beispiel Dropdown:
    energie_auswahl = mo.ui.dropdown(
        options=energietraeger_daten["Energieträger"].tolist(),
        value=energietraeger_daten["Energieträger"].iloc[0],
        label="Energieträger auswählen"
    )

    # Beispiel Slider:
    leistung_slider = mo.ui.slider(start=1, stop=1000, value=100, label="Leistung (kW)")
    return energie_auswahl, leistung_slider


@app.cell
def _(energie_auswahl, leistung_slider, mo):
    mo.md(f"""
    ## ⚙️ Parameter einstellen

    {mo.hstack([energie_auswahl, leistung_slider], justify="start", gap=2)}
    """)
    return


@app.cell
def _(energie_auswahl, energietraeger_daten, leistung_slider):
    # =================================================================
    # BERECHNUNGEN
    # =================================================================
    # Hier die Berechnungen basierend auf der Auswahl durchführen
    #
    # Beispiel:
    # ausgewaehlter_traeger = energie_auswahl.value
    # daten = energietraeger_daten[energietraeger_daten["Energieträger"] == ausgewaehlter_traeger]
    # co2_wert = daten["CO2_eq_g_kWh"].iloc[0]

    # TODO: Eure Berechnungen hier

    ausgewaehlter_traeger = energie_auswahl.value
    leistung_kw=leistung_slider.value
    jahresertrag_kwh = leistung_kw * 1100 #1000 nur als Beispiel

    # Beispiel: Daten für ausgewählten Träger holen
    daten = energietraeger_daten[
        energietraeger_daten["Energieträger"] == ausgewaehlter_traeger
    ].iloc[0]
    return ausgewaehlter_traeger, jahresertrag_kwh, leistung_kw


@app.cell
def _(ausgewaehlter_traeger, jahresertrag_kwh, leistung_kw, mo):
    mo.md(f"""
    ## 📊 Ergebnisse für {ausgewaehlter_traeger}

    ### Energieertrag
    | Kennzahl | Wert |
    |----------|------|
    | Installierte Leistung | **{leistung_kw:,.0f} kW** |
    | Jahresertrag | **{jahresertrag_kwh:,.0f} kWh/a** |
    """)
    return


@app.cell
def _():
    # =================================================================
    # VISUALISIERUNG
    # =================================================================
    # Hier Diagramme erstellen
    #
    # Möglichkeiten:
    # - plotly: Interaktive Diagramme (empfohlen)
    #   import plotly.express as px
    #   fig = px.bar(df, x="...", y="...")
    #   mo.ui.plotly(fig)
    #
    # - matplotlib: Statische Diagramme
    #   import matplotlib.pyplot as plt
    #   plt.bar(...)
    #   plt.gcf()
    #
    # Dokumentation: https://docs.marimo.io/api/plotting/

    # TODO: Eure Visualisierungen hier
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---

    ## ℹ️ Hinweise

    **Datenquellen:**

    Bundesnetzagentur (BNetzA)
    → Offizielle Stromerzeugung nach Energiequellen

    SMARD.de (Plattform der Bundesnetzagentur)
    → Sehr verbreitet für kWh/MWh Daten (Solar, Wind, Wasser etc.)

    Methodik:
    In diesem Projekt wurde eine interaktive Anwendung entwickelt, um den CO₂-Ausstoß und die Stromkosten unterschiedlicher Energiequellen zu berechnen. Die Methodik umfasst folgende Schritte:

    Auswahl der Energiequellen:
    Der Nutzer kann zwischen Solarenergie, Windenergie und Wasserkraft wählen. Jede Energiequelle ist mit spezifischen CO₂-Faktoren und Strompreisen verknüpft, die auf realen Durchschnittswerten basieren.

    Eingabe des Energieverbrauchs:
    Der Nutzer gibt die Menge an Stromverbrauch in Kilowattstunden (kWh) ein, für die die Berechnung durchgeführt werden soll.

    Berechnung des CO₂-Ausstoßes:
    Für die gewählte Energiequelle wird der CO₂-Ausstoß in kg berechnet. Zusätzlich wird der CO₂-Ausstoß eines durchschnittlichen Strommixes als Referenzwert berechnet, um die Einsparung zu ermitteln.

    Berechnung der Stromkosten:
    Auf Basis der kWh und des spezifischen Strompreises der gewählten Energiequelle werden die Kosten berechnet. Außerdem wird die Ersparnis gegenüber dem durchschnittlichen Strommix dargestellt.

    Darstellung der Ergebnisse:
    Die Ergebnisse werden in einer übersichtlichen, interaktiven Benutzeroberfläche angezeigt. Sowohl CO₂-Werte als auch Kosten und Einsparungen werden klar und verständlich präsentiert.

    Reaktivität der App:
    Die Anwendung ist so programmiert, dass Änderungen an den Eingabewerten sofort aktualisierte Ergebnisse liefern, ohne dass die Anwendung neu gestartet werden muss.

    ---

    *Entwickelt für die Fachschule für Umweltschutztechnik*
    """)
    return


@app.cell
def _(pd):
    energiedaten = pd.DataFrame({
        "Energieträger": [
            "Solar",
            "Wind",
            "Wasserkraft",
            "Strommix",
            "Biogas",
            "Solarthermie",
            "Erdgas"
        ],
        "CO2_kg_kWh": [0.041, 0.011, 0.013, 0.380, 0.180, 0.025, 0.490],
        "KEA_MJ_kWh": [0.40, 0.08, 0.02, 3.50, 0.85, 0.30, 2.50],
        "Flaechenbedarf_m2_kW": [10, 30, 0.5, 1, 300, 3, 1],
        "Lebensdauer_Jahre": [25, 20, 80, 40, 15, 20, 30],
        "Erntefaktor": [12, 50, 200, 8, 3, 15, 10]
    })

    energiedaten
    return (energiedaten,)


@app.cell
def _(mo):
    energiequelle = mo.ui.dropdown(
        options=["Solar", "Wind", "Wasserkraft", "Strommix", "Biogas", "Solarthermie", "Erdgas"],
        label="Energiequelle"
    )

    kwh = mo.ui.number(
        label="Energie in kWh",
        value=1000
    )
    kosten = mo.ui.number(
        label="Kosten pro kWh (€)",
        value=0.30
    )
    kosten = mo.ui.slider(
        start=0.05,
        stop=0.60,
        step=0.01,
        value=0.30,
        label="💶 Strommix Kosten (€/kWh)"
    )

    mo.vstack([energiequelle, kwh, kosten])
    return energiequelle, kosten, kwh


@app.cell
def _(energiequelle, kosten, kwh, mo):
    co2_faktoren = {
        "Solar": 0.041,
        "Wind": 0.011,
        "Wasserkraft": 0.013,
        "Strommix" : 0.380,
        "Biogas": 0.180,
        "Solarthermie": 0.025,
        "Erdgas": 0.49
    }
    kosten_faktoren = {
        "Solar": 0.10,
        "Wind": 0.08,
        "Wasserkraft": 0.07,
        "Strommix": 0.40,
        "Biogas": 0.12,
        "Solarthermie": 0.09,
        "Erdgas": 0.15
    }
    def ergebnis():
        if energiequelle.value is None:
            return mo.md("⚠️ Bitte Energiequelle auswählen.")

        kosten_faktoren["Strommix"] = kosten.value

        co2_erneuerbar = kwh.value * co2_faktoren[energiequelle.value]
        co2_strommix = kwh.value * co2_faktoren["Strommix"]
        einsparung_co2 = co2_strommix - co2_erneuerbar

        kosten_erneuerbar = kwh.value * kosten_faktoren[energiequelle.value]
        kosten_strommix = kwh.value * kosten_faktoren["Strommix"]
        einsparung_kosten = kosten_strommix - kosten_erneuerbar

        return mo.md(f"""
    ## Ergebnisse fuer {energiequelle.value}

    ### CO2
    - CO2 ({energiequelle.value}): **{co2_erneuerbar:.1f} kg**
    - CO2 (Strommix): **{co2_strommix:.1f} kg**
    - Einsparung: **{einsparung_co2:.1f} kg CO2**

    ### Kosten
    - Strommix Preis: **{kosten.value:.2f} EUR/kWh**
    - Gesamtkosten ({energiequelle.value}): **{kosten_erneuerbar:.2f} EUR**
    - Gesamtkosten (Strommix): **{kosten_strommix:.2f} EUR**
    - Kosteneinsparung: **{einsparung_kosten:.2f} EUR**
    """)

    ergebnis()
    ergebnis()
    return co2_faktoren, kosten_faktoren


@app.cell
def _(alt, co2_faktoren, energiequelle, kwh, mo, pd):
    def co2_plot():
        if energiequelle.value is None:
            return mo.md("⚠️ Bitte Energiequelle auswählen.")

        co2_erneuerbar = kwh.value * co2_faktoren[energiequelle.value]
        co2_strommix = kwh.value * co2_faktoren["Strommix"]

        df = pd.DataFrame({
            "Quelle": ["Erneuerbar", "Strommix"],
            "CO2": [co2_erneuerbar, co2_strommix]
        })

        return alt.Chart(df).mark_bar().encode(
            x=alt.X("Quelle", title="Energiequelle"),
            y=alt.Y("CO2", title="CO₂-Emissionen (kg)"),
            color="Quelle"
        )

    co2_plot()
    return


@app.cell
def _(alt, co2_faktoren, energiequelle, kwh, mo, pd):
    def co2_pie_plot():
        if energiequelle.value is None:
            return mo.md("⚠️ Bitte Energiequelle auswählen.")

        co2_erneuerbar = kwh.value * co2_faktoren[energiequelle.value]
        co2_strommix = kwh.value * co2_faktoren["Strommix"]
        gesamt = co2_erneuerbar + co2_strommix

        df = pd.DataFrame({
            "Quelle": [energiequelle.value, "Strommix"],
            "CO2": [co2_erneuerbar, co2_strommix],
            "Prozent": [
                round(co2_erneuerbar / gesamt * 100, 1),
                round(co2_strommix / gesamt * 100, 1)
            ]
        })

        base = alt.Chart(df)

        pie = base.mark_arc(outerRadius=120).encode(
            theta=alt.Theta("CO2:Q"),
            color=alt.Color("Quelle:N", title="Energiequelle"),
            tooltip=[
                "Quelle",
                alt.Tooltip("CO2:Q", title="CO₂ (kg)", format=".2f"),
                alt.Tooltip("Prozent:Q", title="Anteil (%)")
            ]
        )

        text = base.mark_text(radius=150, size=14).encode(
            theta=alt.Theta("CO2:Q", stack=True),
            text=alt.Text("Prozent:Q", format=".1f"),
            color=alt.Color("Quelle:N")
        )

        return (pie + text).properties(title="CO₂-Emissionen im Vergleich")

    co2_pie_plot()
    return


@app.cell
def _(alt, energiequelle, kosten_faktoren, kwh, mo, pd):
    def kosten_pie_plot_v2():
        if energiequelle.value is None:
            return mo.md("⚠️ Bitte Energiequelle auswählen.")

        kosten_erneuerbar = kwh.value * kosten_faktoren[energiequelle.value]
        kosten_strommix = kwh.value * kosten_faktoren["Strommix"]
        gesamt = kosten_erneuerbar + kosten_strommix

        df = pd.DataFrame({
            "Quelle": [energiequelle.value, "Strommix"],
            "Kosten": [kosten_erneuerbar, kosten_strommix],
            "Prozent": [
                round(kosten_erneuerbar / gesamt * 100, 1),
                round(kosten_strommix / gesamt * 100, 1)
            ]
        })

        base = alt.Chart(df)

        pie = base.mark_arc(outerRadius=120).encode(
            theta=alt.Theta("Kosten:Q"),
            color=alt.Color("Quelle:N", title="Energiequelle"),
            tooltip=[
                "Quelle",
                alt.Tooltip("Kosten:Q", title="Kosten (€)", format=".2f"),
                alt.Tooltip("Prozent:Q", title="Anteil (%)")
            ]
        )

        text = base.mark_text(radius=150, size=14).encode(
            theta=alt.Theta("Kosten:Q", stack=True),
            text=alt.Text("Prozent:Q", format=".1f"),
            color=alt.Color("Quelle:N")
        )

        return (pie + text).properties(title="Kosten im Vergleich")

    kosten_pie_plot_v2()
    return


@app.cell
def _(energiedaten, mo):
    # =================================================================
    # BENUTZEROBERFLÄCHE (UI)
    # =================================================================

    ui_energie = mo.ui.dropdown(
        options=energiedaten["Energieträger"].tolist(),
        value=energiedaten["Energieträger"].iloc[0],
        label="⚡ Energiequelle auswählen"
    )

    ui_kwh = mo.ui.slider(
        start=100,
        stop=100000,
        step=100,
        value=1000,
        label="🔋 Energieverbrauch (kWh)"
    )

    ui_leistung = mo.ui.slider(
        start=1,
        stop=1000,
        step=1,
        value=100,
        label="⚙️ Leistung (kW)"
    )

    mo.vstack([
        mo.md("## 🌱 Energievergleich Rechner"),
        mo.md("### Einstellungen"),
        ui_energie,
        ui_kwh,
        ui_leistung,
    ])
    return ui_energie, ui_kwh, ui_leistung


@app.cell
def _(
    co2_faktoren,
    energiedaten,
    energiequelle,
    kosten,
    kosten_faktoren,
    mo,
    ui_energie,
    ui_kwh,
    ui_leistung,
):
    def ergebnis_v2():
        if ui_energie.value is None:
            return mo.md("⚠️ Bitte Energiequelle auswählen.")

        co2_erneuerbar = ui_kwh.value * co2_faktoren[ui_energie.value]
        co2_strommix = ui_kwh.value * co2_faktoren["Strommix"]
        einsparung_co2 = co2_strommix - co2_erneuerbar

        kosten_erneuerbar = ui_kwh.value * kosten_faktoren[ui_energie.value]
        kosten_strommix = ui_kwh.value * kosten_faktoren["Strommix"]
        einsparung_kosten = kosten_strommix - kosten_erneuerbar

        row = energiedaten[energiedaten["Energieträger"] == ui_energie.value].iloc[0]

        return mo.md(f"""
    ## 📊 Ergebnisse für **{ui_energie.value}**

    ### ⚡ Anlage
    - Leistung: **{ui_leistung.value} kW**
    - Lebensdauer: **{row['Lebensdauer_Jahre']} Jahre**
    - Erntefaktor: **{row['Erntefaktor']}**
    - Flächenbedarf: **{row['Flaechenbedarf_m2_kW'] * ui_leistung.value:.1f} m²**

    ### 🌿 CO₂
    - CO₂ ({ui_energie.value}): **{co2_erneuerbar:.1f} kg**
    - CO₂ (Strommix): **{co2_strommix:.1f} kg**
    - Einsparung: **{einsparung_co2:.1f} kg CO₂**

    ### Kosten
    - Strommix Preis: **{kosten.value:.2f} EUR/kWh**
    - Gesamtkosten ({energiequelle.value}): **{kosten_erneuerbar:.2f} EUR**
    - Gesamtkosten (Strommix): **{kosten_strommix:.2f} EUR**
    - Kosteneinsparung: **{einsparung_kosten:.2f} EUR**
    """)

    ergebnis_v2()
    return


if __name__ == "__main__":
    app.run()
