import pandas as pd

df = pd.read_csv("metrics.csv")

growth = df["followers"].iloc[-1] - df["followers"].iloc[0]
avg_engagement = df["engagement_rate"].mean()

print("📈 Crescimento de seguidores:", growth)
print("❤️ Engagement médio:", round(avg_engagement, 2), "%")
