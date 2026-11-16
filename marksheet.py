# Project no: 85
# Automated Marksheet Generator
# #Name: Ashutosh Kumar
# ERP: RU-26-01189


import pandas as pd

FILE_NAME = "marks.csv"
SUBJECTS = ["Maths", "Physics", "Programming"]
MAX_TOTAL = 300

def load_data(filename):
    """Read the csv file and return only the valid rows."""
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print("Error: " + filename + " not found. Please keep it in the same folder.")
        return None
    except Exception as e:
        print("Error while reading file:", e)
        return None

    good_rows = []
    for i in range(len(df)):
        row = df.iloc[i]
        roll = row["RollNo"]
        ok = True

        for sub in SUBJECTS:
            # agar number nahi hai to NaN ban jayega
            m = pd.to_numeric(row[sub], errors="coerce")
            if pd.isna(m) or m < 0 or m > 100:
                ok = False
                break

        if ok:
            good_rows.append(row)
        else:
            print("Warning: Row for roll " + str(roll) +
                  " skipped - marks must be between 0 and 100.")

    if len(good_rows) == 0:
        return pd.DataFrame(columns=df.columns)

    clean = pd.DataFrame(good_rows).reset_index(drop=True)
    for sub in SUBJECTS:
        clean[sub] = pd.to_numeric(clean[sub])
    return clean


def get_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    elif percent >= 40:
        return "E"
    else:
        return "F"


def get_result(marks):
    """FAIL if any one subject is below 40."""
    failed = []
    for sub in SUBJECTS:
        if marks[sub] < 40:
            failed.append(sub)
    if len(failed) > 0:
        return "FAIL (" + ", ".join(failed) + " below 40)"
    return "PASS"


def show_marksheet(student):
    marks = {}
    total = 0
    for sub in SUBJECTS:
        marks[sub] = int(student[sub])
        total = total + marks[sub]

    percent = total / MAX_TOTAL * 100
    grade = get_grade(percent)
    result = get_result(marks)

    print()
    print("Roll No: " + str(int(student["RollNo"])) + " | Name: " + str(student["Name"]))
    print("Maths: " + str(marks["Maths"]) + " | Physics: " + str(marks["Physics"]) +
          " | Programming: " + str(marks["Programming"]))
    print("Total: " + str(total) + "/" + str(MAX_TOTAL) + " | Percentage: " + format(percent, ".2f") + "%")
    print("Grade: " + grade + " | Result: " + result)


def single_marksheet(df):
    roll_text = input("Enter roll no: ").strip()

    if not roll_text.isdigit():
        print("Invalid roll number.")
        return

    roll = int(roll_text)
    found = df[df["RollNo"] == roll]

    if found.empty:
        print("Roll number " + str(roll) + " not found.")
    else:
        show_marksheet(found.iloc[0])


def main():
    df = load_data(FILE_NAME)
    if df is None:
        return

    while True:
        print("\n===== MARKSHEET MENU =====")
        print("1. Single marksheet")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            single_marksheet(df)
        elif choice == "2":
            print("Thank you!")
            break
        else:
            print("Wrong choice, try again.")


main()