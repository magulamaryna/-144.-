class Student:

    def __init__(self, name, settings):

        self.name = name

        self.max_project = settings["max_project"]
        self.max_lab = settings["max_lab"]
        self.lab_count = settings["lab_count"]

        self.labs = [0] * self.lab_count
        self.project = 0

    def set_lab(self, number, score):

        if 0 <= number < self.lab_count:
            self.labs[number] = score

    def set_project(self, score):

        self.project = score

    def total(self):

        return sum(self.labs) + self.project


s = Student("Ivan", {"max_project": 20, "max_lab": 10, "lab_count": 3})

s.set_lab(0, 8)
s.set_lab(1, 9)
s.set_project(18)

print("Total:", s.total())