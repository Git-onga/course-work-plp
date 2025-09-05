# ========================
# Task 1: Load and Explore the Dataset
# ========================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
try:
    iris_data = load_iris()
    df = pd.DataFrame(
        data=iris_data.data,
        columns=iris_data.feature_names
    )
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: Dataset not found!")
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Check data types and missing values
print("Data Types and Missing Values:")
print(df.info(), "\n")
print("Missing Values per column:")
print(df.isnull().sum(), "\n")

# Clean dataset
df = df.fillna(df.mean(numeric_only=True))

# ========================
# Task 2: Basic Data Analysis
# ========================

# Compute basic statistics
print("Basic Statistics:")
print(df.describe(), "\n")

# Group by species and compute mean for each numeric column
species_group = df.groupby("species").mean()
print("Average measurements per species:")
print(species_group, "\n")

# Identifying patterns
print("Interesting Findings:")
print("- Iris-virginica has the largest petal and sepal sizes overall.")
print("- Iris-setosa has the smallest petal lengths and widths, making it most distinct.\n")

# ========================
# Task 3: Data Visualization
# ========================

# Set seaborn style
sns.set(style="darkgrid")

# 1. Line chart (for demonstration, plotting sepal length across index per species)
plt.figure(figsize=(8,5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.plot(subset.index, subset['sepal length (cm)'], label=species)
plt.title("Line Chart: Sepal Length Trend per Species")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(6,5))
sns.barplot(x="species", y="petal length (cm)", data=df, estimator="mean", palette="viridis")
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(6,5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(7,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
