class Worker:

    def __init__(self, name, info):

        self.name = name
        self.department = info["department"]
        self.position = info["position"]
        self.birth = info["birth"]
        self.experience = info["experience"]

    def show(self):

        print(self.name, self.department, self.position, self.birth, self.experience)


class Company:

    def __init__(self):

        self.workers = {}

    def add(self, worker):

        self.workers[worker.name] = worker

    def remove(self, name):

        del self.workers[name]

    def search(self, key, value):

        result = []

        for worker in self.workers.values():

            if getattr(worker, key) == value:

                result.append(worker)

        return result


w = Worker("Максим Васильович",
           {"department": "IT", "position": "Programmer", "birth": 2000, "experience": 3})

company = Company()

company.add(w)

for worker in company.search("department", "IT"):
    worker.show()