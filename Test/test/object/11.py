class Student:
    """学生类"""
    studentSum =0
    a = 1

    def __init__(self, name, className):
        self.name = name
        self.className = className
        Student.studentSum += 1

    def introdution(self):
        print("Hello,everyone!I'm " + self.name + " from " + self.className + ".Nice to meet you.")

    # def __del__(self):
    #     class_name = self.__class__.__name__
    #     print(class_name, "销毁")

    def say(self):
        print("yes")


class Student1(Student):

    def introdution(self):
        print("你好，我是" + self.className + "班的" + self.name + "。")




lili = Student1('lili', "计算机1181")
shiry = Student('shiry', "计算机1181")
cary = Student1('cary', "软件1191")

# print(Student1.studentSum)
#
# lili.introdution()


class Runoob:
    __site = "www.runoob.com"



print(Runoob()._Runoob__site)