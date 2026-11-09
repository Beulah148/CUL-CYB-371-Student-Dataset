import csv
import random

random.seed(42)

departments = ["Computer Science", "Mathematics", "Physics", "Chemistry",
               "Biology", "Economics", "Engineering", "Statistics"]
levels = [100, 200, 300, 400]

students = []
for i in range(1, 51):
    students.append({
        "Student_ID": f"STU{1000 + i}",
        "Department": random.choice(departments),
        "Level": random.choice(levels),
        "Attendance_Percentage": round(random.uniform(40.0, 100.0), 1),
        "Average_Exam_Score": round(random.uniform(30.0, 100.0), 1)
    })

with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)

print(f"✅ Done! {len(students)} students saved to students.csv")