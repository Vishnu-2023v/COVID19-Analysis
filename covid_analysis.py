import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("covid_19_india.csv")

# Remove extra spaces from state names
df["State/UnionTerritory"] = df["State/UnionTerritory"].str.strip()

# Remove * symbols from state names
df["State/UnionTerritory"] = (
    df["State/UnionTerritory"]
    .str.replace("*", "", regex=False)
)

# Find total confirmed cases for each state
state_cases = df.groupby("State/UnionTerritory")["Confirmed"].max()

# Get top 10 states
top_states = state_cases.sort_values(ascending=False).head(10)

print("Top 10 States/UTs by Confirmed COVID-19 Cases:")
print(top_states)

# Create graph
plt.figure(figsize=(12, 6))

top_states.sort_values().plot(kind="barh")

plt.title("Top 10 States/UTs by Confirmed COVID-19 Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("State/Union Territory")

plt.tight_layout()
plt.savefig("top_10_states_cleaned.png")
plt.show()




# Final Project Summary

print("\n==============================")
print("COVID-19 DATA ANALYSIS SUMMARY")
print("==============================")

print("Total Confirmed Cases:", df["Confirmed"].max())
print("Total Recovered Cases:", df["Cured"].max())
print("Total Deaths:", df["Deaths"].max())

print("\nHighest affected State/UT:")
print(state_cases.idxmax())

print("\nHighest Confirmed Cases in a State/UT:")
print(state_cases.max())

print("\nProject completed successfully!")