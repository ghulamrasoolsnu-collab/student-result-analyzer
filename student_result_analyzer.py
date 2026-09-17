# Student Result Analyzer - Made by Ghulam Rasool
# Simple code for beginners - Lahore Pakistan

import pandas as pd  # This library reads Excel files

print("Welcome to Student Result Analyzer")
print("-----------------------------------")

# STEP 1: Create sample data (if you don't have excel file)
# This will create marks.csv for 20 students
print("Step 1: Creating student data...")

students = {
    'Name': ['Ali', 'Ahmed', 'Sara', 'Ayesha', 'Bilal', 'Fatima', 'Hassan', 'Zainab', 'Usman', 'Mariam',
             'Omar', 'Sana', 'Hamza', 'Noor', 'Imran', 'Khadija', 'Yasir', 'Laiba', 'Tariq', 'Hira'],
    'Math': [85, 78, 92, 65, 55, 88, 76, 90, 45, 82, 70, 95, 60, 77, 83, 91, 58, 86, 73, 80],
    'Science': [80, 82, 89, 70, 60, 85, 79, 88, 50, 85, 75, 92, 65, 80, 78, 89, 62, 84, 76, 83],
    'English': [75, 80, 85, 68, 58, 82, 74, 85, 48, 80, 72, 90, 62, 78, 80, 87, 60, 82, 70, 79]
}

# Convert to table (DataFrame)
df = pd.DataFrame(students)

# STEP 2: Calculate Total Marks
# Each subject is 100 marks, total 300
print("Step 2: Calculating results...")
df['Total'] = df['Math'] + df['Science'] + df['English']  # Add all subjects

# STEP 3: Calculate Percentage
# Formula: Percentage = Total / 300 * 100
df['Percentage'] = df['Total'] / 300 * 100

# STEP 4: Calculate Grade - Simple logic
# 90%+ = A+, 80%+ = A, 70%+ = B, 60%+ = C, 50%+ = D, Below 50 = F
def find_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

df['Grade'] = df['Percentage'].apply(find_grade)

# STEP 5: Pass or Fail - 50% is passing
def check_pass_fail(percentage):
    if percentage >= 50:
        return "Pass"
    else:
        return "Fail"

df['Result'] = df['Percentage'].apply(check_pass_fail)

# STEP 6: Show results
print("\n=== FINAL RESULTS ===")
print(df)

# STEP 7: Find Top 3 students
print("\n=== TOP 3 STUDENTS ===")
top_3 = df.sort_values(by='Percentage', ascending=False).head(3)
print(top_3[['Name', 'Percentage', 'Grade']])

# STEP 8: Count Pass and Fail
pass_count = len(df[df['Result'] == 'Pass'])
fail_count = len(df[df['Result'] == 'Fail'])
print(f"\nTotal Students: {len(df)}")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")

# STEP 9: Show Failed students
print("\n=== FAILED STUDENTS ===")
failed = df[df['Result'] == 'Fail']
if len(failed) == 0:
    print("All students passed! No failures.")
else:
    print(failed[['Name', 'Percentage']])

# STEP 10: Save to Excel
df.to_excel('Final_Results.xlsx', index=False)
print("\n✅ File saved: Final_Results.xlsx")
print("✅ Project completed! 10 hours work done in 5 seconds!")