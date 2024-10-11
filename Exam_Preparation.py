max_poor_grades = int(input())

poor_grades_count = 0
total_score = 0
problem_count = 0
last_problem = ""

while True:
    problem_name = input()

    if problem_name == "Enough":

        average_score = total_score / problem_count if problem_count > 0 else 0
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {problem_count}")
        print(f"Last problem: {last_problem}")
        break

    grade_input = input()
    while not grade_input.isdigit() or not (2 <= int(grade_input) <= 6):
        print("Invalid input! Please enter an integer grade between 2 and 6.")
        grade_input = input()

    grade = int(grade_input)
    total_score += grade
    problem_count += 1
    last_problem = problem_name

    if grade <= 4:
        poor_grades_count += 1

        if poor_grades_count == max_poor_grades:

            print(f"You need a break, {poor_grades_count} poor grades.")
            break
