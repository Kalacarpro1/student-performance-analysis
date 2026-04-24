# 📌 Project Title

## Student Performance Analysis System

---

## 📌 Objective

This project analyzes student academic data to understand how study hours and attendance influence overall performance. It applies data preprocessing, feature engineering, and statistical analysis to extract meaningful insights from the dataset, helping educators identify top performers and students who need additional support.

---

## 📌 Dataset Description

The dataset (`data/student_dataset.csv`) contains the following attributes:

| Column | Description |
|---|---|
| **StudentID** | Unique identifier for each student |
| **StudyHours** | Number of hours studied per day |
| **Attendance** | Attendance percentage (0–100) |
| **Marks** | Final marks obtained by the student |

---

## 📌 Steps Performed

### 1. Data Loading
- Loaded the dataset using `pandas`.
- Displayed first few rows, dataset shape, and column details.

### 2. Data Cleaning
- Identified and handled missing values:
  - Missing `Marks` → filled with **mean**
  - Missing `StudyHours` → filled with **median**
  - Missing `Attendance` → filled with **median**
- Removed outliers: rows where `StudyHours > 15` or `Marks > 100`.

### 3. Feature Engineering
- Created **Performance** column:
  - `Excellent` → Marks ≥ 80
  - `Good` → Marks between 60 and 79
  - `Needs Improvement` → Marks < 60
- Created **EffortScore** = `StudyHours × Attendance`

### 4. Data Analysis
- Computed basic statistics (mean, std, min, max).
- Found top 5 students by Marks.
- Found students scoring below 50.
- Analyzed correlation: StudyHours vs Marks and Attendance vs Marks.
- Performed group-based analysis by attendance level and study category.

---

## 📌 Key Insights

1. **High attendance strongly improves marks** — students with ≥85% attendance score significantly higher on average than those below 65%.
2. **More study hours lead to better marks** — students studying ≥6 hours/day consistently outperform those studying less than 4 hours/day.
3. **Attendance is a stronger predictor of marks than study hours alone** — showing up regularly has a higher correlation with performance.
4. **EffortScore (StudyHours × Attendance) has the highest correlation with marks** — students who combine both consistent attendance and study hours achieve the best results.
5. **Study hours alone are not sufficient** — students with high study hours but poor attendance still underperform, showing both factors must work together.
6. **A significant portion of students need improvement** — targeted academic intervention for low performers is recommended.

---

## 📌 How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📁 Project Structure

```
student-performance-analysis/
│
├── data/
│   └── student_dataset.csv
│
├── src/
│   ├── preprocess.py
│   └── analysis.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 👤 Author

Student Performance Analysis — Data Analysis Project
