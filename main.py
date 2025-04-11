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

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Date", y="Temperature", hue="Ville", marker="o")
plt.title("Evolution des températures moyennes par ville")
plt.xticks(rotation=45)
plt.show()

ville_counts = df['Ville'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(ville_counts, labels=ville_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("Répartition des enregistrements par ville")
plt.show()

# Adding 'Jour' column as the number of days since the first date
df['Jour'] = (df['Date'] - df['Date'].min()).dt.days

# Prepare the data for KMeans clustering
x = df[['Jour', 'Temperature']]  # Make sure to select the correct columns

# Perform KMeans clustering
km = kmeans.KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = km.fit_predict(x)

# Plot the clustering results
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Jour", y="Temperature", hue="Cluster", palette="viridis", s=100)
plt.title("Clustering des températures par jours (K-Means)")
plt.xlabel("Jour écoulé")
plt.ylabel("Température")
plt.legend(title="Cluster")
plt.show()

# Predicting the cluster and estimated temperature for a future day (day 120)
future_day = np.array([[120, df['Temperature'].mean()]])  # Reshaped as 2D array
predicted_cluster = km.predict(future_day)[0]

# Estimate temperature based on the cluster
predicted_temp = df[df['Cluster'] == predicted_cluster]['Temperature'].mean()

print(f"Température estimée pour le jour 120 : {predicted_temp:.2f}°C")
