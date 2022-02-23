class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def getFullName(self):
        return "%s %s" % (self.first_name, self.last_name)
    
class Student(Person):
    def __init__(self, first_name, last_name, subject):
        super(Student, self).__init__(first_name, last_name)
        self.subject = subject
    def printNameSubject(self):
        return print("%s, %s" % (super(Student, self).getFullName(), self.subject))

class Teacher(Person):
    def __init__(self, first_name, last_name, course):
        super(Teacher, self).__init__(first_name, last_name)
        self.course = course
    def printNameCourse(self):
        return print("%s, %s" % (super(Teacher, self).getFullName(), self.course))
    
