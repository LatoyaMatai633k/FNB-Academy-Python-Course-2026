# grade_report.py

students = [
    {"name": "Yaya", "maths": 75, "english": 80, "science": 70},
    {"name": "John", "maths": 65, "english": 72, "science": 68},
    {"name": "Sarah", "maths": 90, "english": 85, "science": 88},
    {"name": "Peter", "maths": 45, "english": 50, "science": 40},
    {"name": "Thabo", "maths": 55, "english": 60, "science": 58}
]


results = []


# Go through each student
for student in students:

    average = (
        student["maths"] +
        student["english"] +
        student["science"]
    ) / 3

    # Grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Status
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Add the result to the results list
    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })


# Calculate class statistics
total = 0
highest = 0
lowest = 100

for result in results:
    total = total + result["average"]

    if result["average"] > highest:
        highest = result["average"]

    if result["average"] < lowest:
        lowest = result["average"]


class_average = total / len(results)


# Display report
print("\n========== CLASS REPORT ==========")

for result in results:
    print(f"Name: {result['name']}")
    print(f"Average: {result['average']:.2f}")
    print(f"Grade: {result['grade']}")
    print(f"Status: {result['status']}")
    print("---------------------------------")


print(f"Class Average: {class_average:.2f}")
print(f"Highest Average: {highest:.2f}")
print(f"Lowest Average: {lowest:.2f}")


# Search for a student
while True:

    search_name = input(
        "\nEnter a student name to search, or type 'stop': "
    ).title()

    if search_name.lower() == "stop":
        print("Goodbye!")
        break

    found = False

    for result in results:
        if result["name"] == search_name:
            print("\nStudent Found!")
            print(f"Name: {result['name']}")
            print(f"Average: {result['average']:.2f}")
            print(f"Grade: {result['grade']}")
            print(f"Status: {result['status']}")

            found = True
            break

    if not found:
        print("Student not found.")