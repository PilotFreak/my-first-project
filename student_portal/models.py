class Student :    
    # для добавления оценки по курсу.
    courses={}
    name=""
    age=0

    def  add_grade(self,course, grade):
        self.courses[course]=grade
    #Метод get_grades() для возврата всех курсов и оценок студента.
    def get_grades(self):
        return self.courses

#Класс  с атрибутами для названия курса и списка студентов.
class Course:
    students={}
    # Метод add_student(student) для добавления студента на курс.
    def add_student(self,student) :
        students[student.name]=student
    # Метод get_student_grades(student_name) для получения оценок
    def get_student_grades(self,student_name) :
        return students[student_name].get_grades()

