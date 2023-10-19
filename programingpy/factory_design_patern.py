from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):

    @abstractstaticmethod
    def person_method():
        ''' INTERFACE METHOD '''


class Student(IPerson):

    def __init__(self):
        self.name = 'Basic student name'


    def person_method(self):
        print('I am a student')


class Teacher(IPerson):
    def __init__(self):
        self.name = 'Basic teacher name'


    def person_method(self):
        print('I am a teacher')
