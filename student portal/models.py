class Student :    
    # для добавления оценки по курсу.
    courses = {}
    name = ""
    age = 0

    def add_grade(self, course, grade):
        self.courses[course] = grade
    #Метод get_grades() для возврата всех курсов и оценок студента.
    def get_grades(self):
        return self.courses
    
    def get_avarage_grade():
        avarage_grade = sum(grade)/len(courses)
        return avarage_grade

#Класс  с атрибутами для названия курса и списка студентов.
class Course:
    students = {}
    # Метод add_student(student) для добавления студента на курс.
    def add_student(self, student):
        students[student.name] = student
    # Метод get_student_grades(student_name) для получения оценок
    def get_student_grades(self,student_name):
        return students[student_name].get_grades()
    
    def get_top_students(nubmer_of_top_students):
        nubmer_of_top_students = 3
        top_students = sorted(avarage_grade)[0, nubmer_of_top_students]
        return top_students