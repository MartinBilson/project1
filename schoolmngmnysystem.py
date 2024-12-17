# Key Components
# Students: Represented by a Student class.
# Teachers: Represented by a Teacher class.
# Courses: Represented by a Course class.
# Classrooms: Represented by a Classroom class.
# School: Acts as a container for all components.


# Student Enrollment: Students can enroll in courses.
# Teacher Assignment: Each course has an assigned teacher.
# Classroom Capacity: Classroom tracks the number of students.
# School Overview: Display the school's summary, including all entities.

# Define a Student class
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __str__(self):
        courses = ', '.join([course.name for course in self.courses])
        return f"Student: {self.name}, Grade: {self.grade}, Enrolled Courses: {courses}"


# Define a Teacher class
class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"


# Define a Course class
class Course:
    def __init__(self, course_id, name, teacher):
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        student_names = ', '.join([student.name for student in self.students])
        return f"Course: {self.name}, Teacher: {self.teacher.name}, Students: {student_names}"


# Define a Classroom class
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


# Define a School class
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

    def __str__(self):
        return f"School: {self.name}, Students: {len(self.students)}, Teachers: {len(self.teachers)}, Courses: {len(self.courses)}, Classrooms: {len(self.classrooms)}"


# Example Usage
if __name__ == "__main__":
    # Create a school
    my_school = School("Green Valley High")

    # Create some teachers
    teacher_1 = Teacher(1, "Mr. Smith", "Math")
    teacher_2 = Teacher(2, "Ms. Johnson", "English")

    # Add teachers to the school
    my_school.add_teacher(teacher_1)
    my_school.add_teacher(teacher_2)

    # Create some courses
    math_course = Course(101, "Algebra", teacher_1)
    english_course = Course(102, "Literature", teacher_2)

    # Add courses to the school
    my_school.add_course(math_course)
    my_school.add_course(english_course)

    # Create some students
    student_1 = Student(1, "Alice", "10th")
    student_2 = Student(2, "Bob", "10th")

    # Enroll students in courses
    student_1.enroll(math_course)
    student_2.enroll(english_course)
    math_course.add_student(student_1)
    english_course.add_student(student_2)

    # Add students to the school
    my_school.add_student(student_1)
    my_school.add_student(student_2)

    # Create classrooms
    classroom_1 = Classroom(101, 30)
    classroom_1.add_student(student_1)
    classroom_1.add_student(student_2)

    # Add classrooms to the school
    my_school.add_classroom(classroom_1)

    # Display information
    print(my_school)
    print(student_1)
    print(student_2)
    print(math_course)
    print(english_course)
    print(classroom_1)
