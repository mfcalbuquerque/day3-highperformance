class Person:

    def __init__(self, name, surn):
        self.name = name
        self.surn = surn

    def fullname(self):
        return "%s %s" % (self.name, self.surn)


class Student(Person):
    def __init__(self, name, surn, area):
        Person.__init__(self, name, surn)
#        super(Person, self).__init__(name, surn)
        self.area = area

    def personinfo(self):
        print("Name and Subject: " + self.fullname() + ", " + self.area)




class Teacher(Person):
    def __init__(self, name, surn, course):
        #Person.__init__(self, name, surn)
        super(Teacher, self).__init__(name, surn)
        self.course = course

    def personinfo(self):
        print("Teacher's name and course: " + self.fullname() + ", " + self.course + " course.")
