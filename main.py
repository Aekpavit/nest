from grade_calculator import GradeCalculator

calculator = GradeCalculator()

name = input("ชื่อนักเรียน: ")
score = int(input("คะแนน: "))

grade = calculator.calculate_grade(score)

print(f"นักเรียน {name} ได้เกรด {grade}")
