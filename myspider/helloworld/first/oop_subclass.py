#!/usr/bin/env python
# -*- coding:utf-8 -*-

#继承的使用
class SchoolMember:
    """学校里的成员"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(initialized schoolMember: {}'.format(self.name))
    def tell(self):
        """我的细节"""
        print('name:{} age:{}'.format(self.name, self.age),end="... ")


class Teacher(SchoolMember):
    '''a teacher'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(initialzaed teacher:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary: {:d}'.format(self.salary))


class Student(SchoolMember):
    """a student"""
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('initialized student: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('marks: {:d} '.format(self.marks))

t = Teacher('mrs.shrividya', 40, 30000)
s = Student('swaroop', 25, 75)

print()
members  = [t,s]
for member in members:
    member.tell()