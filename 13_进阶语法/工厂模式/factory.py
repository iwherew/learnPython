# 统一创建对象的入口，方便维护
# 当发生修改，仅修改工程类的创建方法就行
class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class PersonFactory:
    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()

pf = PersonFactory()
worker = pf.get_person('w')
student = pf.get_person('s')
teacher = pf.get_person('t')