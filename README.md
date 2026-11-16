# Automated-Marksheet-Generator
A Python program that reads student marks from `marks.csv` using Pandas and prints a neat marksheet with total (out of 300), percentage, grade and result (PASS/FAIL).

## Features
- Reads `marks.csv` with Pandas and handles a missing file
- Validates that each mark is between 0 and 100; invalid rows are skipped with a warning
- Calculates total and percentage (2 decimal places)
- Assigns grade: 90+ A+, 80 A, 70 B, 60 C, 50 D, 40 E, below 40 F
- Result is FAIL if any subject is below 40
- Shows a single marksheet by roll number

## Requirements
- Python 3
- Pandas

## How to Run
pip3 install pandas
python3 marksheet.py

Choose option 1 from the menu and enter a roll number.

## Sample Input (marks.csv)
RollNo,Name,Maths,Physics,Programming
101,Anita,85,90,80
102,Rahul,40,45,50
103,Suman,35,70,60
104,Vikas,100,100,100

## Sample Output
Roll No: 101 | Name: Anita
Maths: 85 | Physics: 90 | Programming: 80
Total: 255/300 | Percentage: 85.00%
Grade: A | Result: PASS

## Author
Ashutosh Kumar
B.Tech Computer Science and Engineering
Rungta International Skills University

