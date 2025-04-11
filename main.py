import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
np.random.seed(42)

villes = ["Paris", "Lyon", "Marseille", "Toulouse", "Bordeaux"]
dates = pd.date_range(start="2023/01/01", periods=100, freq="D")

data = {
    "Ville": np.random.choice(villes, size=100),
    "Date": dates[:100],
    "Temperature": np.random.uniform(-5, 35, 100)
}

df = pd.DataFrame(data)

print(df.head(10))
print("\n\n\nStatistiques descriptives :")
print(df.describe())

paris_data = df[df["Ville"] == "Paris"]

print("\n\n\nDonnées pour la ville de Paris :")
print(paris_data.head())


df_sorted = df.sort_values(by="Date")

print("\n\n\nDonnées triées par date :")
print(df_sorted.head(10))


# Température moyenne par ville
moyennes_par_ville = df.groupby("Ville")["Temperature"].mean()

print("\nTempérature moyenne par ville :")
print(moyennes_par_ville)


# Filtrer les données pour janvier 2023
mask_janvier = (df["Date"] >= "2023-01-01") & (df["Date"] <= "2023-01-31")
df_janvier = df[mask_janvier]

print("\nDonnées pour janvier 2023 :")
print(df_janvier.head())


print(df["Ville"].value_counts())


df["Mois"] = df["Date"].dt.to_period("M")


moyenne_par_mois = df.groupby("Mois")["Temperature"].mean()

print("\nTempérature moyenne par mois :")
print(moyenne_par_mois)




plt.figure(figsize = (12,6))
sns.lineplot(data=df, x="Date", y="Temperature", hue="Ville" , marker="o")
plt.title("Evolution des tempratures moyennes  par ville")
plt.xticks(rotation=45)
plt.show()

