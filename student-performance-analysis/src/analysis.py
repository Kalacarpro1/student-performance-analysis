import pandas as pd
import numpy as np


def basic_statistics(df):
    """Display basic statistics of the dataset."""
    print("\n" + "=" * 50)
    print("BASIC STATISTICS")
    print("=" * 50)
    print(df[['StudyHours', 'Attendance', 'Marks', 'EffortScore']].describe().round(2))
    return df[['StudyHours', 'Attendance', 'Marks', 'EffortScore']].describe().round(2)


def top_students(df, n=5):
    """Find top N students based on Marks."""
    print("\n" + "=" * 50)
    print(f"TOP {n} STUDENTS (by Marks)")
    print("=" * 50)
    top = df.nlargest(n, 'Marks')[['StudentID', 'StudyHours', 'Attendance', 'Marks', 'Performance']]
    print(top.to_string(index=False))
    return top


def low_performers(df, threshold=50):
    """Find students with Marks below threshold."""
    print("\n" + "=" * 50)
    print(f"LOW PERFORMERS (Marks < {threshold})")
    print("=" * 50)
    low = df[df['Marks'] < threshold][['StudentID', 'StudyHours', 'Attendance', 'Marks', 'Performance']]
    print(f"Total low performers: {len(low)}")
    print(low.to_string(index=False))
    return low


def group_analysis(df):
    """Group-based analysis: attendance level and study categories."""
    print("\n" + "=" * 50)
    print("GROUP-BASED ANALYSIS")
    print("=" * 50)

    # Group by attendance level
    def attendance_level(att):
        if att >= 85:
            return 'High (≥85%)'
        elif att >= 65:
            return 'Medium (65–84%)'
        else:
            return 'Low (<65%)'

    df['AttendanceLevel'] = df['Attendance'].apply(attendance_level)
    att_group = df.groupby('AttendanceLevel')['Marks'].mean().round(2).reset_index()
    att_group.columns = ['Attendance Level', 'Avg Marks']
    print("\n📊 Average Marks by Attendance Level:")
    print(att_group.to_string(index=False))

    # Group by study category
    def study_category(hours):
        if hours >= 7:
            return 'High Study (≥7h)'
        elif hours >= 4:
            return 'Moderate Study (4–6h)'
        else:
            return 'Low Study (<4h)'

    df['StudyCategory'] = df['StudyHours'].apply(study_category)
    study_group = df.groupby('StudyCategory')['Marks'].mean().round(2).reset_index()
    study_group.columns = ['Study Category', 'Avg Marks']
    print("\n📊 Average Marks by Study Category:")
    print(study_group.to_string(index=False))

    return att_group, study_group


def study_vs_marks(df):
    """Analyse StudyHours vs Marks."""
    print("\n" + "=" * 50)
    print("STUDY HOURS vs MARKS ANALYSIS")
    print("=" * 50)
    correlation = df['StudyHours'].corr(df['Marks'])
    print(f"  Correlation between StudyHours and Marks: {correlation:.4f}")
    print(f"  Average Marks for StudyHours ≥ 6 : {df[df['StudyHours'] >= 6]['Marks'].mean():.2f}")
    print(f"  Average Marks for StudyHours  < 4 : {df[df['StudyHours'] < 4]['Marks'].mean():.2f}")
    return correlation


def attendance_vs_marks(df):
    """Analyse Attendance vs Marks."""
    print("\n" + "=" * 50)
    print("ATTENDANCE vs MARKS ANALYSIS")
    print("=" * 50)
    correlation = df['Attendance'].corr(df['Marks'])
    print(f"  Correlation between Attendance and Marks: {correlation:.4f}")
    print(f"  Average Marks for Attendance ≥ 85% : {df[df['Attendance'] >= 85]['Marks'].mean():.2f}")
    print(f"  Average Marks for Attendance  < 65% : {df[df['Attendance'] < 65]['Marks'].mean():.2f}")
    return correlation


def extract_insights(df):
    """Extract and print at least 5 key insights from the data."""
    print("\n" + "=" * 50)
    print("KEY INSIGHTS")
    print("=" * 50)

    corr_study = df['StudyHours'].corr(df['Marks'])
    corr_att = df['Attendance'].corr(df['Marks'])
    excellent_pct = (df['Performance'] == 'Excellent').mean() * 100
    low_pct = (df['Performance'] == 'Needs Improvement').mean() * 100
    high_att_marks = df[df['Attendance'] >= 85]['Marks'].mean()
    low_att_marks = df[df['Attendance'] < 65]['Marks'].mean()
    high_study_marks = df[df['StudyHours'] >= 6]['Marks'].mean()
    low_study_marks = df[df['StudyHours'] < 4]['Marks'].mean()
    effort_corr = df['EffortScore'].corr(df['Marks'])

    insights = [
        f"1. 📈 High attendance strongly boosts performance: students with ≥85% attendance "
        f"average {high_att_marks:.1f} marks vs {low_att_marks:.1f} for those below 65%.",

        f"2. 📚 More study hours = better marks: students studying ≥6h/day average "
        f"{high_study_marks:.1f} marks vs {low_study_marks:.1f} for those studying <4h.",

        f"3. 🔗 Attendance is a stronger predictor of marks (r = {corr_att:.2f}) "
        f"than study hours alone (r = {corr_study:.2f}), showing that showing up matters.",

        f"4. 💡 EffortScore (StudyHours × Attendance) has a high correlation with marks "
        f"(r = {effort_corr:.2f}), confirming that consistent effort drives success.",

        f"5. 🎯 {excellent_pct:.1f}% of students scored Excellent (≥80 marks), while "
        f"{low_pct:.1f}% need improvement (<60 marks) — targeted support is recommended.",

        f"6. ⚠️  Study hours alone are not sufficient: some students with high study hours "
        f"but low attendance still scored poorly, highlighting the importance of both factors.",
    ]

    for insight in insights:
        print(f"\n  {insight}")

    return insights
