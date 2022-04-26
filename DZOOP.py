class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lectors(self, lector, course, grade):
        if isinstance(lector, Lecturer) and lector in \
                lector.courses_attached and course in \
                self.courses_in_progress and course in \
                self.finished_courses:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        all_grades = []

        for course in self.grades:
            all_grades.extend(self.grades[course])

        if len(all_grades) > 0:
            avg_grade = round(sum(all_grades) / len(all_grades), 1)
        else:
            avg_grade = 0

        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)

        some_student = f"Имя:{self.name}\nФамилия:{self.surname}\n"
        some_student += f"Средняя оценка за домашние задание:{avg_grade}\n"
        some_student += f"Курсы в процессе изучения:{courses_in_progress_str}\n"
        some_student += f"Завершенные курсы:{finished_courses_str}"
        return some_student

    def __lt__(self, other):
        if isinstance(other, Student):
            self_grades = []
            other_grades = []

            for course in self.grades:
                self_grades.extend(self.grades[course])

            for course in other.grades:
                other_grades.extend(other.grades[course])

            if len(self_grades) > 0:
                self_avg_grade = sum(self_grades) / len(self_grades)
            else:
                self_avg_grade = 0

            if len(other_grades) > 0:
                other_avg_grade = sum(other_grades) / len(other_grades)
            else:
                other_avg_grade = 0

            return self_avg_grade < other_avg_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        all_grades = []

        for course in self.grades:
            all_grades.extend(self.grades[course])

        if len(all_grades) > 0:
            avg_grade = round(sum(all_grades) / len(all_grades), 1)
        else:
            avg_grade = 0

        some_lecturer = f"Имя:{self.name}\nФамилия:{self.surname}\n"
        some_lecturer += f"Средняя оценка за лекции:{avg_grade}"
        return some_lecturer

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            self_grades = []
            other_grades = []

            for course in self.grades:
                self_grades.extend(self.grades[course])

            for course in other.grades:
                other_grades.extend(other.grades[course])

            if len(self_grades) > 0:
                self_avg_grade = sum(self_grades) / len(self_grades)
            else:
                self_avg_grade = 0

            if len(other_grades) > 0:
                other_avg_grade = sum(other_grades) / len(other_grades)
            else:
                other_avg_grade = 0

            return self_avg_grade < other_avg_grade


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f"Имя:{self.name}\nФамилия:{self.surname}\n"
        return some_reviewer


def student_avg_course_grade(students, course):
    all_grades = []

    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])

    if len(all_grades) > 0:
        avg_grade = round(sum(all_grades) / len(all_grades), 1)
    else:
        return f"За курс {course} студенты ещё не получали оценок."

    return f"Средняя оценка студентов за курс {course}: {avg_grade}"


def lecturer_avg_course_grade(lecturers, course):
    all_grades = []

    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])

    if len(all_grades) > 0:
        avg_grade = round(sum(all_grades) / len(all_grades), 1)
    else:
        return f"За курс {course} лекторы ещё не получали оценок."

    return f"Средняя оценка лекторов за курс {course}: {avg_grade}"


def main():
    valera = Student("Валера", "Хренова", "муж")
    nikita = Student("Гадя", "Петрович", "алк")
    reviewer1 = Reviewer("Василий", "Пупкин")
    reviewer2 = Reviewer("Баста", "Гагарина")
    lecturer1 = Lecturer("Дочка", "Снегурочка")
    lecturer2 = Lecturer("Дед", "Мороз")

    valera.finished_courses += ["Java"]
    valera.courses_in_progress += ["Python", "SQL", "D"]

    nikita.finished_courses += ["Java"]
    nikita.courses_in_progress += ["Python", "D"]

    lecturer1.courses_attached += ["Java", "Python", "D", "SQL"]
    lecturer2.courses_attached += ["SQL", "D"]

    reviewer1.courses_attached += ["Java", "Python", "D", "SQL"]
    reviewer2.courses_attached += ["Java", "Python", "SQL", "D"]

    valera.rate_lectors(lecturer1, "Java", 5)
    valera.rate_lectors(lecturer1, "Python", 4)
    valera.rate_lectors(lecturer1, "D", 10)
    valera.rate_lectors(lecturer1, "SQL", 7)
    valera.rate_lectors(lecturer2, "D", 10)
    valera.rate_lectors(lecturer2, "SQL", 6)

    nikita.rate_lectors(lecturer1, "Java", 8)
    nikita.rate_lectors(lecturer1, "Python", 2)
    nikita.rate_lectors(lecturer1, "D", 10)
    nikita.rate_lectors(lecturer2, "D", 9)

    reviewer1.rate_hw(valera, "Python", 4)
    reviewer1.rate_hw(valera, "D", 3)
    reviewer1.rate_hw(valera, "SQL", 8)
    reviewer1.rate_hw(nikita, "Python", 7)
    reviewer1.rate_hw(nikita, "D", 9)

    reviewer2.rate_hw(valera, "Python", 10)
    reviewer2.rate_hw(valera, "D", 2)
    reviewer2.rate_hw(valera, "SQL", 10)

    reviewer2.rate_hw(nikita, "Python", 4)
    reviewer2.rate_hw(nikita, "D", 3)

    print("Студенты:\n")
    print(valera, '\n')
    print(nikita, '\n')
    print("Лекторы:\n")
    print(lecturer1, '\n')
    print(lecturer2, '\n')
    print("Проверяющие:\n")
    print(reviewer1, '\n')
    print(reviewer2, '\n')

    if lecturer1 > lecturer2:
        print(f"Средняя оценка у {lecturer1.name} {lecturer1.surname} выше.")
    elif lecturer1 == lecturer2:
        prompt = f"Средняя оценка у лекторов {lecturer1.surname} и "
        prompt += f"{lecturer2.surname} равна."
        print(prompt)
    else:
        print(f"Средняя оценка у {lecturer2.name} {lecturer2.surname} выше.")

    if valera > nikita:
        print(f"Средняя оценка у {valera.name} {valera.surname} выше.")
    elif valera == nikita:
        prompt = f"Средняя оценка у студнтов {valera.surname} и "
        prompt += f"{nikita.surname} равна."
        print(prompt)
    else:
        print(f"Средняя оценка у {nikita.name} {nikita.surname} выше.")

    print()

    students = [valera, nikita]
    lecturers = [lecturer1, lecturer2]
    courses = ["Python", "Java", "D", "SQL"]

    for course in courses:
        print(lecturer_avg_course_grade(lecturers, course))
        print(student_avg_course_grade(students, course), "\n")


main()