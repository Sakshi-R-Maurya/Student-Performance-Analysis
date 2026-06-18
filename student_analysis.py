import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep=";")

print("===== DATASET INFO =====")
print("Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)


print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

avg_grade = df["G3"].mean()
print("\nAverage Final Grade (G3):", round(avg_grade, 2))


above_15 = df[df["G3"] > 15].shape[0]
print("Students Scoring Above 15:", above_15)

correlation = df["studytime"].corr(df["G3"])
print("Correlation between Study Time and G3:", round(correlation, 3))

gender_avg = df.groupby("sex")["G3"].mean()

print("\nAverage Score by Gender:")
print(gender_avg)


plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=10)
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["studytime"], df["G3"])
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.show()


plt.figure(figsize=(6, 5))
gender_avg.plot(kind="bar")
plt.title("Average Final Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average G3")
plt.show()