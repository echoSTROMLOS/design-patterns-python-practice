from logger_object import SingletonObject 
from logger import Logger
print("--------------------")
obj1 = SingletonObject()
obj1.val = "Object value 1"
print(obj1)
print("--------------------")
obj2 = SingletonObject()
obj2.val = "Object value 2"
print(obj2)
print("--------------------")
obj3 = SingletonObject()
obj3.val = "Object value 3"
print(obj3)
print("--------------------")