"""
Student Performance Analysis System
====================================
Main entry point — calls all preprocessing and analysis steps in order.
"""

import os
import sys

# Allow imports from src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from preprocess import load_dataset, handle_missing_values, remove_outliers, feature_engineering
from analysis import (
    basic_statistics,
    top_students,
    low_performers,
    group_analysis,
    study_vs_marks,
    attendance_vs_marks,
    extract_insights,
)

DATASET_PATH = os.path.join(os.path.dirname(__file__), 'data', 'student_dataset.csv')


def main():
    print("\n" + "🎓" * 25)
    print("   STUDENT PERFORMANCE ANALYSIS SYSTEM")
    print("🎓" * 25)

    
    df = load_dataset(DATASET_PATH)

    
    df = handle_missing_values(df)

    
    df = remove_outliers(df)


    df = feature_engineering(df)

    
    basic_statistics(df)

    
    top_students(df, n=5)


    low_performers(df, threshold=50)


    study_vs_marks(df)

    
    attendance_vs_marks(df)

    
    group_analysis(df)


    extract_insights(df)

    print("\n" + "=" * 50)
    print("✅  ANALYSIS COMPLETE")
    print("=" * 50 + "\n")


if __name__ == '__main__':
    main()
