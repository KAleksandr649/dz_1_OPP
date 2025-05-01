class Student:
    def __init__(self, name, surname, gender):
        self.name = name #имя
        self.surname = surname #фамилия
        self.gender = gender #пол
        self.finished_courses = [] #курсы,которые он прошел
        self.courses_in_progress = [] #курсы в прогрессе
        self.grades = {} #оценки

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    #добавляет cours_name в список finished_courses
    def rate_for_mentor(self,lectoring,coursing,grading):
            if isinstance(lectoring,Lecturer) and coursing in self.courses_in_progress and coursing in lectoring.courses_attached :
                if coursing in lectoring.ozenka:
                    lectoring.ozenka[coursing] += [grading]
                else:
                    lectoring.ozenka[coursing] = [grading]
            else:
                return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #список закрепленных курсов
        self.ozenki = {} #в этом словаре будут храниться оценки, поставленные учениками лекторам
        self.kyrs_for_ozenok=[] # для self.ozenki
class Lecturer(Mentor): # лекторы
    def ozen(self,kyrs_for_ozenok,ozenka): #метод обьединяет курс и оценку и добавляет в словарь ozenki
        self.ozenki[kyrs_for_ozenok] = [ozenka]

class Reviewer(Mentor): #эксперты,проверяющие дз
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
ychenik = Student("peta","ivanov","man")
lector = Lecturer("stepa","Petrov")
lector.ozen("C++","5")
revi = Reviewer("12","23")
ychenik.courses_in_progress += ['C++']
revi.courses_attached += ['C++']
revi.rate_hw(ychenik,"C++","5")
ychenik.rate_for_mentor(lector,"C++","5")
print(lector.ozenki)
print(ychenik.grades)


