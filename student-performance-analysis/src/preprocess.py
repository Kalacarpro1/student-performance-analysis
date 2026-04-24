import pandas as pd
import numpy as np


def load_dataset(filepath):
    """Load the student dataset from a CSV file."""
    df = pd.read_csv(filepath)
    print("=" * 50)
    print("DATASET LOADED SUCCESSFULLY")
    print("=" * 50)
    print(f"\nFirst 5 rows:\n{df.head()}")
    print(f"\nDataset Shape: {df.shape}")
    print(f"\nColumn Details:\n{df.dtypes}")
    print(f"\nBasic Info:")
    df.info()
    return df


def handle_missing_values(df):
    """Identify and fill missing values."""
    print("\n" + "=" * 50)
    print("HANDLING MISSING VALUES")
    print("=" * 50)

    print(f"\nMissing values before cleaning:\n{df.isnull().sum()}")

    # Fill missing Marks with mean
    marks_mean = df['Marks'].mean()
    df['Marks'] = df['Marks'].fillna(round(marks_mean, 2))
    print(f"\n✅ Filled missing 'Marks' with mean: {round(marks_mean, 2)}")

    # Fill missing StudyHours with median
    study_median = df['StudyHours'].median()
    df['StudyHours'] = df['StudyHours'].fillna(study_median)
    print(f"✅ Filled missing 'StudyHours' with median: {study_median}")

    # Fill missing Attendance with median
    att_median = df['Attendance'].median()
    df['Attendance'] = df['Attendance'].fillna(att_median)
    print(f"✅ Filled missing 'Attendance' with median: {att_median}")

    print(f"\nMissing values after cleaning:\n{df.isnull().sum()}")
    return df


def remove_outliers(df):
    """Remove outliers based on project rules."""
    print("\n" + "=" * 50)
    print("REMOVING OUTLIERS")
    print("=" * 50)

    initial_count = len(df)
    df = df[df['StudyHours'] <= 15]
    df = df[df['Marks'] <= 100]
    removed = initial_count - len(df)

    print(f"\n✅ Removed {removed} outlier row(s).")
    print(f"   Rows before: {initial_count} | Rows after: {len(df)}")
    df = df.reset_index(drop=True)
    return df


def feature_engineering(df):
    """Create new features: Performance and EffortScore."""
    print("\n" + "=" * 50)
    print("FEATURE ENGINEERING")
    print("=" * 50)

    # Performance category based on Marks
    def categorize_performance(marks):
        if marks >= 80:
            return 'Excellent'
        elif marks >= 60:
            return 'Good'
        else:
            return 'Needs Improvement'

    df['Performance'] = df['Marks'].apply(categorize_performance)
    print("\n✅ Created 'Performance' column:")
    print(df['Performance'].value_counts())

    # EffortScore = StudyHours x Attendance
    df['EffortScore'] = df['StudyHours'] * df['Attendance']
    print(f"\n✅ Created 'EffortScore' = StudyHours × Attendance")
    print(f"   Range: {df['EffortScore'].min():.2f} – {df['EffortScore'].max():.2f}")

    return df
