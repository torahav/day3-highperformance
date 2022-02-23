#!/usr/bin/env python
from classroom import Person
from classroom import Student
from classroom import Teacher

p1 = Person('Tora', 'Hävermark')
p1.getFullName()

p2 = Student('Anna', 'Anka', 'Biology')
p2.printNameSubject()

p3 = Teacher('Tom', 'Waits', 'Programming')
p3.printNameCourse()
