#programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for student_name in student_scores:
    if student_scores[student_name] >=91 and student_scores[student_name] <=100:
        student_grades[student_name]="outstanding"
    elif student_scores[student_name] >=81 and student_scores[student_name] <=90:
        student_grades[student_name]="Exceeds Expectation"
    else:
        student_scores[student_name] < 80
        student_grades[student_name] = "Fail"

print(student_grades)
        
