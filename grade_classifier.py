def grade_classifier():
    student_name = input("What is your name? ").title()
    english = float(input("Enter your grades for English: "))
    maths = float(input("Enter your grades for Maths: "))
    biology = float(input("Enter your grades for Biology: "))

    grades_average = (english *0.4) + (maths *0.3) + (biology *0.3)

    if maths < 40 and english < 40 and biology < 40:
        print("You need to pull up your socks!")
    
    if grades_average >= 80:
        print("Grade : A")
    elif 70 <= grades_average <= 79:
        print("Grade : B")
    elif 60 <= grades_average <= 69:
        print("Grade : C")
    elif 50 <= grades_average <= 59:
        print("Grade : D")
    else:
        print("Grade : F")

    Report = f"{student_name}: your average grading for {english} English, {maths} Maths, {biology} Biology is ({grades_average})"
    print(Report)

grade_classifier()