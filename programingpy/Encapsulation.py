class Person():

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Age(self):
        return self.__age
    
    @Age.setter
    def Age(self, val):
        print('he',val)
        if val < 18 and val > 0:
            self.__age = 'neplatny vek'
        elif val >= 18:
            self.__age = 'platny vek'
    
    # @property # turns it into a property
    # def Name(self):
    #     return self.__name
    
    # @Name.setter
    # def Name(self, value): # we can control stuff in the setter # thanks to this we can control the variable that is later passed on for example make it possible so that age can not be negative
    #     self.__name = value  # we sort of have public acces to the variable



p1 = Person('Mike', 4, 'm')

p1.Age = 14
print(p1.Age)