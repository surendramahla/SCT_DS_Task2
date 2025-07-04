# SCT_DS_Task2
# 🚢 Titanic Survival Analysis with Python

This repository contains a comprehensive exploratory data analysis (EDA) on the Titanic dataset. It includes visualizations and insights about survival patterns based on passenger attributes such as **sex, age, class, and fare**.

---

## 📁 Dataset Used

- **Source:** [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)
- **File:** `train.csv`

---

## 📊 Visualizations Included

1. **Survival Count**  
   Overview of how many passengers survived vs. did not survive.

2. **Survival by Sex**  
   Comparison of survival rate across genders.

3. **Survival by Passenger Class**  
   Analysis of survival by 1st, 2nd, and 3rd class passengers.

4. **Age Distribution by Survival**  
   Distribution of ages among survivors and non-survivors.

5. **Fare Distribution by Survival**  
   How ticket price (fare) relates to survival.

6. **Correlation Heatmap**  
   Shows relationships between numeric variables such as Age, Fare, Pclass, and encoded categorical variables.

---

## 🛠 Data Preprocessing

- Filled missing `Age` values with the median.
- Filled missing `Embarked` values with the mode.
- Dropped the `Cabin` column due to high number of missing values.
- Encoded categorical columns `Sex` and `Embarked` for correlation heatmap.

---

## 🧪 How to Run

1. Clone the repository or download the code.
2. Make sure the Titanic dataset (`train.csv`) is available in the specified path.
3. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
