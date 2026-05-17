class Student2:

    def __init__(self, name, settings):

        self.name = name

        self.lecture_count = settings["lecture_count"]
        self.max_lab = settings["max_lab"]
        self.lab_count = settings["lab_count"]

        self.labs = [0] * self.lab_count
        self.lectures = 0

    def set_lab(self, number, score):

        self.labs[number] = score

    def set_lectures(self, count):

        self.lectures = count

    def total(self):

        return sum(self.labs) + self.lectures


s2 = Student2("Anna", {"lecture_count": 10, "max_lab": 10, "lab_count": 3})

s2.set_lab(0, 10)
s2.set_lab(1, 9)

s2.set_lectures(8)

print("Total:", s2.total())