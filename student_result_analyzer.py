# Student Result Analyzer - Teacher Input Version
# Made by Ghulam Rasool - Very Easy for Beginners

import pandas as pd

print("=== Student Result Analyzer ===")
print("Teacher will enter Name and Marks - System calculates everything!\n")

students_list = []  # To store all students

# Ask how many students
num = int(input("How many students? Enter number: "))

for i in range(num):
    print(f"\n--- Student {i+1} ---")
    name = input("Enter Name: ")
    math = int(input("Enter Math marks (0-100): "))
    science = int(input("Enter Science marks (0-100): "))
    english = int(input("Enter English marks (0-100): "))

    # AUTO CALCULATION - Teacher doesn't need to do anything
    total = math + science + english
    percentage = total / 300 * 100

    # Auto Grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Auto Pass/Fail
    if percentage >= 50:
        result = "Pass"
    else:
        result = "Fail"

    # Save
    students_list.append({
        "Name": name,
        "Math": math,
        "Science": science,
        "English": english,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade,
        "Result": result
    })

# Convert to Excel table
df = pd.DataFrame(students_list)

print("\n========== FINAL RESULTS ==========")
print(df)

print("\n--- TOP 3 Students ---")
print(df.sort_values(by="Percentage", ascending=False).head(3)[["Name","Percentage","Grade"]])

print("\n--- Failed Students ---")
failed = df[df["Result"] == "Fail"]
if len(failed) == 0:
    print("All Passed!")
else:
    print(failed[["Name","Percentage"]])

# Auto save
df.to_excel("Final_Results.xlsx", index=False)
print("\n✅ File saved automatically: Final_Results.xlsx")
print("Teacher work finished in 5 seconds!")