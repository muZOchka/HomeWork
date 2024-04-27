class Human:
    height = 170


class Student(Human):
    height = 175
    maind = 90
    force = 100


class Worker(Human):
    height = 170
    maind = 100
    force = 50

class Derector(Human):
    height = 172
    maind = 110
    force = 70
    Glavnost = 100



vasya = Student()
lilya = Worker()
Bova = Derector()


print('Вася -', vasya.height, vasya.maind,vasya.force)
print('Лілія - ', lilya.height, lilya.maind, lilya.force)
print('Вова - ', Bova.height, Bova.maind, Bova.force, Bova.Glavnost)