if __name__ == '__main__':
    students = []
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        grades.append(score)
        students.append([name, score])
    


    grades = sorted(grades, reverse=True)
    lowest_grade = grades[-1]
    sec_low_grade = grades[0]

    for grade in grades:
        if grade < sec_low_grade and grade > lowest_grade:
            sec_low_grade = grade

    sec_low_grade_stud_names = []

    for student in students:
        if student[1] == sec_low_grade:
            sec_low_grade_stud_names.append(student[0])
            
    for name in sorted(sec_low_grade_stud_names):
        print(name)