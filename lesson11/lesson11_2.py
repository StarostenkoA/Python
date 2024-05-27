class Student:
    surname  = ""
    name  = ""
    group  = ''
    grads = []

    def __init__(self, surname, name, group, grads) -> None:
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads
    
    def add_grade(self, new_grade):
        self.grade.append(new_grade)
    
    def average_grade(self) -> float:
       if len(self.grads)==0:
           return 0
       else:
           return sum(self.grads)/len(self.grads)
    
    def __eq__(self, other_Student ) -> bool:
        return self.average_grade() == other_Student.average_grade()

    def __ne__(self, other_Student ) -> bool:
        return self.average_grade() != other_Student.average_grade()

    def __lt__(self, other_Student ) -> bool:
        return self.average_grade() < other_Student.average_grade()

    def __gt__(self, other_Student ) -> bool:
        return self.average_grade() > other_Student.average_grade()

    def __le__(self, other_Student ) -> bool:
        return self.average_grade() <= other_Student.average_grade()

    def __ge__(self, other_Student ) -> bool:
        return self.average_grade() >= other_Student.average_grade()

    def __str__(self):    
        return f"average_grade: {self.average_grade()}"


students = [
    Student("Ivanov", "Ivan", '6',[7,3,9,7]),
    Student("Ivanov", "Vasia", '3',[7,10,8,9]),
    Student("Stepanov", "Kolia", '1',[2,3,5,4]),
    Student("Fedorov", "Jan", '2',[8,8,8,8]),
    Student("Kozlov", "Leha", '5',[10,9,8,7])
]

students_SORT=sorted(students)
students_SORT_rev=sorted(students,reverse=True)
students_up8=list(filter(lambda x:x.average_grade()>8, students))



print(students_up8[0])
