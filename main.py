import pandas as pd
import string
from numpy.random import choice

# Liste mit allen Buchstaben
buchstaben = list(string.ascii_lowercase)

# Neuer Dataframe mit 1000 zufällig gewählten Buchstaben
df = pd.DataFrame({"Buchstabe": choice(buchstaben, 1000)})

# Die 10 häufigsten finden
g = df.groupby(["Buchstabe"])["Buchstabe"].count().nlargest(10)
print("Die 10 häufigsten sind:", g.index.tolist())

# Alle nicht in der Liste auf "Other" anpassen
df.loc[~df["Buchstabe"].isin(g.index.tolist()), "Buchstabe"] = "Other"
print("Hier das Resultat (20 erste Einträge):", df.head(20))

# Erzeugen eine Dataframes
df2 = pd.DataFrame({"Buchstabe": ["a"] * 15 + ["b"] * 20 + ["c"] * 65})

print(df2[(df2["Buchstabe"] == "a") | (df2["Buchstabe"] == "c")])
