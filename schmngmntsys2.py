class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.courses = []
        self.fees_paid = 0.0
        self.grades = {}

    def enroll(self, course):
        self.courses.append(course)

    def pay_fees(self, amount):
        self.fees_paid += amount
        print(f"{self.name} paid ${amount}. Total fees paid: ${self.fees_paid}")

    def add_grade(self, course, grade):
        self.grades[course.name] = grade

    def __str__(self):
        courses = ', '.join([course.name for course in self.courses])
        grades = ', '.join([f"{course}: {grade}" for course, grade in self.grades.items()])
        return (f"Student: {self.name}, Grade: {self.grade}, Enrolled Courses: {courses}, "
                f"Fees Paid: ${self.fees_paid}, Grades: {grades}")


class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def assign_grade(self, student, course, grade):
        student.add_grade(course, grade)
        print(f"{self.name} assigned grade {grade} to {student.name} for {course.name}")

    def __str__(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"


class Course:
    def __init__(self, course_id, name, teacher, fee):
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.fee = fee
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        student_names = ', '.join([student.name for student in self.students])
        return f"Course: {self.name}, Teacher: {self.teacher.name}, Students: {student_names}, Fee: ${self.fee}"


class Classroom:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
        else:
            print(f"Classroom {self.room_number} is full!")

    def __str__(self):
        student_names = ', '.join([student.name for student in self.students])
        return f"Classroom: {self.room_number}, Capacity: {self.capacity}, Students: {student_names}"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []
        self.classrooms = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def total_fees_collected(self):
        return sum(student.fees_paid for student in self.students)

    def __str__(self):
        return (f"School: {self.name}, Students: {len(self.students)}, Teachers: {len(self.teachers)}, "
                f"Courses: {len(self.courses)}, Classrooms: {len(self.classrooms)}")
        

# Example Usage
if __name__ == "__main__":
    # Create a school
    my_school = School("Green Valley High")

    # Create teachers
    teacher_1 = Teacher(1, "Mr. Smith", "Math")
    teacher_2 = Teacher(2, "Ms. Johnson", "English")

    # Add teachers to the school
    my_school.add_teacher(teacher_1)
    my_school.add_teacher(teacher_2)

    # Create courses
    math_course = Course(101, "Algebra", teacher_1, 500)
    english_course = Course(102, "Literature", teacher_2, 300)

    # Add courses to the school
    my_school.add_course(math_course)
    my_school.add_course(english_course)

    # Create students
    student_1 = Student(1, "Alice", "10th")
    student_2 = Student(2, "Bob", "10th")

    # Enroll students in courses and manage fees
    student_1.enroll(math_course)
    math_course.add_student(student_1)
    student_1.pay_fees(500)

    student_2.enroll(english_course)
    english_course.add_student(student_2)
    student_2.pay_fees(300)

    # Assign grades
    teacher_1.assign_grade(student_1, math_course, "A")
    teacher_2.assign_grade(student_2, english_course, "B+")

    # Add students to the school
    my_school.add_student(student_1)
    my_school.add_student(student_2)

    # Display information
    print(my_school)
    print(student_1)
    print(student_2)
    print(math_course)
    print(english_course)
    print(f"Total Fees Collected: ${my_school.total_fees_collected()}")
