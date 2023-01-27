# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return f'Pizza({self.ingredients!r})'
#
#     @classmethod
#     def margherita(cls):
#         return cls('mozzarella')
#
#     @classmethod
#     def prosciutto(cls,x):
#         return cls(x+1)
#
# print(Pizza.prosciutto())


class Student:
    name = 'unknown' # class attribute
    def __init__(self, naming, year):
        self.age = 20  # instance attribute
        self.naming = naming
        self.year = year

    @classmethod
    def tostring(cls, last_name):
        print('Student Class Attributes: name=',cls.name, last_name)



print(Student.tostring('tantalidis'))
