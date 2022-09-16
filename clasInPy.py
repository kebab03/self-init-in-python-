class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class SPerson:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = SPerson("Johpn", 366)°
p1.myfunc()

class TPerson:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = TPerson("Tohn", 36)
p1.myfunc()

class YPerson:
  def __init__(clsVar, name, age):
    clsVar.name = name
    clsVar.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = YPerson("clsVarPao", 36)
p1.myfunc()


class F9999Person:
  pass
