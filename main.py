import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sklearn.cluster as kmeans

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

ville_counts = df['Ville'].value_counts()
plt.figure(figsize = (8,8))
plt.pie(ville_counts , labels = ville_counts.index , autopct="%1.1f%%" , startangle= 140)
plt.title("Reparation des enregistrement par ville")
plt.show()



df['Jour'] = (df['Date'] - df(['Date']).min()).dt.days

x = df['Jour' , 'Temperature']
km = kmeans.KMeans( n_clusters=3, random_state =42, n_init=10)
df['Cluster'] = km.fit_predict(x)
plt.figure(figsize = (10,6))
sns.scatterplot(data = df , x = "Jour" , y = "Temperature", hue = "Cluster" , palette = "viridis" , s=100)
plt.title("clustering des temperatures par jours K-MEANS")
plt.xlabel("Jour ecoulé")
plt.ylabel("Temperature")
plt.legend(title= "cluster")
plt.show()

future_day = np.array([120])
predicted_cluster = km.predict(np.hstack((future_day, df['Temperature'].mean())))[0]
predicted_temp = df[df['Cluster'] == predicted_cluster]['Temperature'].mean()
print(f"Temp estimé pour le jour 120 : {predicted_temp:.2f}°C")