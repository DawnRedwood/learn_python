'''enum'''

# from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# from enum import Enum, unique
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# day1 = Weekday.Mon
# print(day1)
# print(Weekday.Tue)
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(day1 == Weekday.Mon)
# print(day1 == Weekday.Tue)
# print(Weekday(1))
# print(day1 == Weekday(1))
# # Weekday(7)
# for name, member in Weekday.__members__.items():
#     print(name, '=>', member)

# from enum import Enum, unique
# @unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# # 测试
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过！')
# else:
#     print('测试失败！')